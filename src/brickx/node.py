
from abc import ABC
from contextvars import ContextVar
from uuid import uuid4
from copy import deepcopy
from enum import Enum
from typing import cast, Unpack
import html
from brickx.attrs import GlobalAttrs

_with_stack_var: ContextVar[str | None] = ContextVar('_with_stack', default=None)

PREFIXED_ATTRS: tuple[str, ...] = ("aria", "data", "user")

class Node(ABC):
  tag_name: str = "node"
  inline: bool = False

  def __init__(self) -> None:
    self.parent: "Container | None" = None

    if Container._with_stack.get(_with_stack_var.get(), None):
      self.collect() 

  def __str__(self) -> str:
    return self.render_inline()
  
  def __format__(self, format_spec: str) -> str:
    # TODO
    # Used for paragraph composing with f strings in the context of with manager.
    # Usage:
    # with (node := Foo()):
    #  f"bar{Baz()}" >> Text(escape=False) 
    # assert node.render_inline() == "<foo>bar<baz></baz></foo>"

    if (context := Container._with_stack[_with_stack_var.get()]):
      context[-1].remove(self)

    return self.render_inline()
  
  def render(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""
  
  def render_inline(self, level: int = 0) -> str: 
    return self.render(level=level, spaces=None) # TODO: escaping ?
  
  def insert_in(self, parent: "Container", index: int | None = None) -> "Container":
    parent.insert(self, index)

    return parent
  
  def prepend_to(self, container: "Container") -> "Container":
    return self.insert_in(container, 0)  
  
  def append_to(self, container: "Container") -> "Container":
    self.insert_in(container)
    return container 
  
  def collect(self) -> "Node":
    if self.parent is not None:
      raise Exception(f"Node already having a parent. Detach the node before collecting it.")

    Container._with_stack[_with_stack_var.get()][-1].append(self)
    return self
  
  def free(self) -> "Container | None":
    old_parent = self.parent
    if self.parent is not None:
      self.parent._nodes.remove(self)
      self.parent = None  

    return old_parent 
  
  def __rshift__(self, parent: "Container") -> "Container":
    parent.insert(self)
    return parent
  
  def __radd__(self, text: str | int | float | None) -> "Root":
    return Root(text, self)

  def __add__(self, node: "Node | str | int | float | None") -> "Root":
    return Root(self, node)
  
  def __mul__(self, count: int) -> "Root":
    root = Root()
    for _ in range(count):
      root.insert(deepcopy(self))

    return root
  
  def __rmul__(self, count: int) -> "Container":    
    return self.__mul__(count) 
  
class Text(Node):
  def __init__(self, text: str = "", escape=True) -> None:
    super().__init__()
    self.text = text
    self.escape = escape

  @property
  def text(self) -> str:
    return self._text
  
  def __str__(self) -> str:
    return self.text

  @text.setter
  def text(self, text: str) -> None:
    self._text = "" if text is None else str(text)

  def render(self, level: int = 0, spaces: int | None = 2) -> str:
    indent = "" if spaces is None else " " * level * spaces
    text = f"{indent}{html.escape(self.text) if self.escape else self.text}"

    return text  
  
  def insert(self, text: "str | int | float | None", index: int | None = None) -> "Text": 
    self.text += str(text)

    return self
  
  def __rrshift__(self, text: "str | int | float | bool | None | Text") -> "Text":
    self.text += str(text) if text else ""
    return self
  
class Element(Node): 
  tag_name: str = "element"

  def __init__(self, **attrs: Unpack[GlobalAttrs]) -> None:
    super().__init__()

    self._attrs: dict[str, str | dict[str, str]] = {}

    for attr in attrs:
      if attr.startswith(("h_", "data", "aria", "user", "hx_")):
        self._attrs[attr] = attrs[attr]

  @property
  def attrs(self) -> GlobalAttrs:
    return cast(GlobalAttrs, self._attrs)  
  
  def render_attr(self, name: str, value: str | bool | None | dict[str, str], remove_prefix: bool = True) -> str:
    name = name.removeprefix("h_") if remove_prefix else name
    name = name.replace("_", "-")

    if type(value) == bool:
      if value:
        return name
      else:
        return ""

    if value is None:
      return ""

    # TODO: review escaping for js and other contexts
    return f'{name}="{html.escape(str(value), quote=True)}"'

  def render_attrs(self) -> str:
    attrs: list[str] = []
    output = ""
    for key, value in self._attrs.items():
      if type(value) == dict:
        if key in PREFIXED_ATTRS:
          l = []
          for k, v in value.items():
            if key == "user":
              l.append(self.render_attr(f'{k}', v, False))
            else:
              l.append(self.render_attr(f'{key}-{k}', v))

            output = " ".join(l)
        else:
          raise TypeError(f"Dict. values not allowed for attribute '{key}'.")
      else:
        output = self.render_attr(key, value)

      attrs.append(output)

    return " ".join(attrs).strip()
  
  def start_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    indent = "" if spaces is None else " " * level * spaces
    
    attrs = self.render_attrs()
    html = f"{indent}<{self.tag_name}{' ' + attrs if attrs != '' else ''}>"
    return html 
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    markup = ""
    markup += self.start_tag(level, spaces)

    return markup

class Container(Element):
  tag_name: str = "container"

  _with_stack: dict[str | None, list[list["Node"]]] = {}

  def __init__(self, *nodes: Node | str | int | float | None, **attrs: Unpack[GlobalAttrs]) -> None:
    super().__init__(**attrs)

    self._nodes: list[Node] = []

    for node in nodes:
      self.insert(node)
    
    if _with_stack_var.get() is None:
      _with_stack_var.set(uuid4().hex)  
      self._with_stack[_with_stack_var.get()] = []

  @property
  def nodes(self) -> list["Node"]:
    return self._nodes

  def __enter__(self): # Let the type checker infer the final return type depending on the calling html element 
    Container._with_stack[_with_stack_var.get()].append([])
    return self

  def __exit__(self, type_, value, traceback):
    if type_:
      self._with_stack[_with_stack_var.get()].pop()
    else:  
      for node in self._with_stack[_with_stack_var.get()].pop():
        if node.parent is None:
          self.insert(node)

  def __iter__(self):
    return iter(self._nodes)   
  
  def __rrshift__(self, text: str | int | float | None) -> "Container":
    self.insert(text)
    return self 
  
  def at(self, index: int) -> "Node | None":
    if len(self._nodes) > index:
      return self._nodes[index]
    
    return None
  
  def first(self) -> "Node | None":
    return self.at(0) 
  
  def last(self) -> "Node | None":
    return self.at(-1)
  
  def take_at(self, index: int) -> "Node | None":
    if len(self._nodes) > index:
      node = self._nodes.pop(index)
      node.parent = None
      return node
    
    return None
  
  def take_first(self) -> "Node | None":
    return self.take_at(0)
  
  def take_last(self) -> "Node | None":
    return self.take_at(-1)

  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    inline = self.inline or spaces is None or not self._nodes

    indent = "" if inline else " " * level * (0 if spaces is None else spaces)
    new_line = "" if inline else "\n"
    end_indent = "" if inline is None else indent

    return f"{new_line}{end_indent}</{self.tag_name}>" 
  
  def inner_html(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    markup = ""
    inline = self.inline or spaces is None or not self._nodes
    new_line = "" if inline else "\n"

    markup += new_line.join(node.render(level, None if inline else spaces) for node in self._nodes)  

    return html.escape(markup) if escape else markup

  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    markup = ""
    
    inline = self.inline or spaces is None or not self._nodes
    new_line = "" if inline else "\n"

    markup += self.start_tag(level, spaces)
    markup += new_line

    markup += self.inner_html(level+1, spaces, escape)
    markup += self.end_tag(level, spaces)

    return markup 
  
  def insert(self, child: "str | int | float | Node | None", index: int | None = None) -> "Node": 
    if type(child) == Root:
      i = -1
      while child._nodes:
        node: Node | None = child.take_first()
        i += 1  
        if index is None:
          self.insert(node)
        else:  
          self.insert(node, index+i)

      return child  
    
    if child is None:
      child_ = Text("") 
    elif type(child) in (str, int, float, bool):
      child_ = Text(str(child)) 
    else:
      child_: Node = cast(Node, child)

    if child_.parent is not None:
      raise Exception(f"Node {type(self)} already having a parent. Free the node before inserting it again.")  

    child_.parent = self 
    if index is None:
      self._nodes.append(child_)
    else:  
      self._nodes.insert(index, child_)

    return child_  
  
  def prepend(self, node: "Node | str | int | float") -> "Node":
    return self.insert(node, 0)   
  
  def append(self, node: "Node | str | int | float") -> "Node":
    return self.insert(node)
    
class Root(Container):
  tag_name: str = "root"

  def start_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return "" 
  
  def end_tag(self, level: int = 0, spaces: int | None = 2) -> str:
    return ""
  
  def render(self, level: int = 0, spaces: int | None = 2, escape: bool = False) -> str:
    return self.inner_html(level, spaces, escape)
  