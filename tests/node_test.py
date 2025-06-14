from brickx.node import Text, Root
from foo_elements import Foo, Bar, Baz, Quux, Fred
import pytest

class TestNodeInsertInParent():
  def test_inserting_return_value(self):
    container = Foo()
    element = Quux()
    assert container == element.insert_in(container)   

  def test_inserting_with_a_zero_index(self):
    node = Foo()
    node.insert(Bar())
    Quux().insert_in(node, 0)

    assert node.render_inline() == "<foo><quux><bar></bar></foo>"

  def test_inserting_with_a_none_index(self):
    node = Foo()
    node.insert(Bar())
    Quux().insert_in(node, None)

    assert node.render_inline() == "<foo><bar></bar><quux></foo>"

  def test_inserting_with_a_positive_index(self):
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    Quux().insert_in(node, 1)

    assert node.render_inline() == "<foo><bar></bar><quux><baz></baz></foo>"

  def test_inserting_with_an_invalid_positive_index(self):
    node = Foo()
    node.insert(Bar())
    Quux().insert_in(node, 10)

    assert node.render_inline() == "<foo><bar></bar><quux></foo>"

  def test_inserting_with_a_reverse_index(self):
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    Quux().insert_in(node, -1)

    assert node.render_inline() == "<foo><bar></bar><quux><baz></baz></foo>"

  def test_inserting_with_an_invalid_reverse_index(self):
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    Quux().insert_in(node, -10)

    assert node.render_inline() == "<foo><quux><bar></bar><baz></baz></foo>"

  def test_inserting_again_in_another_element(self):
    node_a = Foo()
    node_b = Bar()
    void = Quux()
    void.insert_in(node_a)

    with pytest.raises(Exception):
      void.insert_in(node_b)

  def test_inserting_again_in_the_same_element(self):
    node_a = Foo()
    void = Quux()
    void.insert_in(node_a)

    with pytest.raises(Exception):
      void.insert_in(node_a)

  def test_reinserting_from_a_root_in_a_container(self):
    node = Foo()
    root = Root()
    void = Quux()
    void.insert_in(root)
    with pytest.raises(Exception):
      void.insert_in(node)

  # def test_inserting_in_a_void(self):
  #   # Raises a TypeError exception
  #   node = Quux()
  #   void = Quux()
  #   with pytest.raises(TypeError):
  #     void.insert_to(node)

  # def test_inserting_in_a_text(self): # TODO: Allow?!
  #   # Raises a TypeError exception
  #   node = Text("")
  #   void = Quux()
  #   with pytest.raises(TypeError):
  #     void.insert_to(node)

class TestNodeInsertAChild():
  def test_insert_return_value(self):
    node = Foo()
    void = Quux()
    assert void == node.insert(void)

  def test_inserting_from_a_container(self):
    node = Foo()
    node.insert(Quux())

    assert node.render_inline() == "<foo><quux></foo>"

  def test_inserting_a_string(self):
    node = Foo()
    text = node.insert("Bar")
    assert type(text) == Text
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_inserting_an_integer(self):
    node = Foo()
    text = node.insert(1)
    assert type(text) == Text
    assert node.render_inline() == "<foo>1</foo>"

  def test_inserting_a_float(self):
    node = Foo()
    text = node.insert(1.23)
    assert type(text) == Text
    assert node.render_inline() == "<foo>1.23</foo>"

  def test_inserting_a_boolean(self):
    node = Foo()
    text = node.insert(True)
    assert type(text) == Text
    assert node.render_inline() == "<foo>True</foo>"

  def test_inserting_a_none(self):
    node = Foo()
    text = node.insert(None)
    assert type(text) == Text
    assert node.render_inline() == "<foo></foo>"

  def test_inserting_with_index(self):
    node = Foo()
    node.insert(Bar())
    node.insert(Baz())
    node.insert(Quux(), 1)
    assert node.render_inline() == "<foo><bar></bar><quux><baz></baz></foo>"
  
  def test_inserting_a_root_with_index(self):
    root = Root(Quux(), Fred())
    node = Foo(Bar(), Baz())
    node.insert(root, 1)
    assert node.render_inline() == "<foo><bar></bar><quux><fred><baz></baz></foo>"

class TestNodePrependToParent():
  def test_prepend_to_return_value(self):
    node = Foo()
    assert node == Quux().prepend_to(node)

  def test_prepending_in_a_container(self):
    node = Bar().insert_in(Foo())
    Quux().prepend_to(node)
    assert node.render_inline() == "<foo><quux><bar></bar></foo>"

  def test_prepending_a_text_to_a_container(self):
    node = Bar().insert_in(Foo())
    Text("Baz").prepend_to(node)
    assert node.render_inline() == "<foo>Baz<bar></bar></foo>"

class TestNodePrependAChild():
  def test_prepend_return_value(self):
    node = Foo()
    void = Quux()
    assert void == node.prepend(void)

  def test_prepending_a_text_from_a_container(self):
    node = Foo()
    node.prepend("Bar")
    node.prepend(Text("Baz"))
    assert node.render_inline() == "<foo>BazBar</foo>"    

class TestNodeAppendToParent():
  def test_append_to_return_value(self):
    node = Foo()
    assert node == Quux().append_to(node)

  def test_appending_to_a_container(self):
    node = Quux().append_to(Foo())
    assert node.render_inline() == "<foo><quux></foo>"

  def test_appending_a_text_to_a_container(self):
    node = Text("Bar").append_to(Foo())
    assert node.render_inline() == "<foo>Bar</foo>"

class TestNodeAppendAChild():
  def test_append_return_value(self):
    node = Foo()
    void = Quux()
    assert void == node.append(void)

  def test_appending_a_text_from_a_container(self):
    node = Foo()
    node.append("Bar")
    node.append(Text("Baz"))
    assert node.render_inline() == "<foo>BarBaz</foo>"        

  def test_append_from_a_container(self):
    node = Foo()
    node.append(Bar())
    node.append(Quux())
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"

  def test_appending_a_string(self):
    node = Foo()
    text = node.append("Bar")
    assert type(text) == Text
    assert node.render_inline() == "<foo>Bar</foo>"

class TestNodeWithContext():
  def test_creating_a_node_outside_of_with_context(self):
    node = Foo()
    assert list(node._with_stack.values())[0] == []

  def test_appending_nodes_using_a_one_level_with_context(self):
    node = Foo()
    with node:
      bar = Bar()
      quux = Quux()
      assert list(node._with_stack.values())[0] == [[bar, quux]]

    assert list(node._with_stack.values())[0] == []
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"
 
  def test_appending_nodes_using_a_two_level_with_context(self):
    with Foo() as node:
      with Bar() as bar:
        baz = Baz()
        quux = Quux()
      
        assert list(node._with_stack.values())[0] == [[bar], [baz, quux]]
    
    assert node.render_inline() == "<foo><bar><baz></baz><quux></bar></foo>"

  def test_appending_using_with_context_and_manual_appending(self):
    with Foo() as node:
      Bar().append(Quux())

    assert node.render_inline() == "<foo><bar><quux></bar></foo>"

  def test_collecting_a_node_created_outside_of_with_context(self):
    bar = Bar()
    with Foo() as node:
      bar.collect()

    assert node.render_inline() == "<foo><bar></bar></foo>"  

  def test_collecting_a_node_already_inserted_in_another_element(self):
    with Bar() as bar:
      baz = Baz()

    assert bar.render_inline() == "<bar><baz></baz></bar>"   

    with Foo() as node:
      baz.free()
      baz.collect()

    assert bar.render_inline() == "<bar></bar>"    
    assert node.render_inline() == "<foo><baz></baz></foo>"    

  def test_collecting_a_node_again_without_freeing_it(self):
    with Bar() as bar:
      baz = Baz()

    assert bar.render_inline() == "<bar><baz></baz></bar>"   

    with Foo() as node:
      with pytest.raises(Exception):
        baz.collect()

  # def test_using_f_strings_within_a_with_context(self):
  #   with (node := Foo()):
  #     text = Text(f"bar{Baz()}", escape=False) 

  #   assert node.render_inline() == "<foo>bar<baz></baz></foo>"
  #   assert text.text == "bar<baz></baz>"

  # TODO
  # def test_appending_nodes_in_concurrent_threads(self):
  #   pass

class TestNodeIterator():
  def test_interating_a_container_using_for(self):
    node = Foo(Bar(), Baz())
    i = 0
    for n in node:
      assert n == node._nodes[i]
      i += 1 

class TestNodeRightShifting():
  def test_right_shifting_return_value(self):
    node = Foo()
    assert node == Bar() >> node

  def test_right_shifting_a_string_to_a_text(self):
    node = "bar" >> Text("foo")   
    assert node.render_inline() == "foobar"

  def test_right_shifting_an_int_to_a_text(self):
    node = 1 >> Text("foo")   
    assert node.render_inline() == "foo1"

  def test_right_shifting_a_float_to_a_text(self):
    node = 1.23 >> Text("foo")   
    assert node.render_inline() == "foo1.23"

  def test_right_shifting_a_boolean_to_a_text(self):
    node = True >> Text("foo")   
    assert node.render_inline() == "fooTrue"

  def test_right_shifting_none_to_a_text(self):
    node = None >> Text("foo")   
    assert node.render_inline() == "foo"

  def test_right_shifting_a_container_to_a_container(self):
    node = Bar() >> Foo()   
    assert node.render_inline() == "<foo><bar></bar></foo>"

  def test_right_shifting_a_container_to_a_root(self):
    node = Root(Foo())
    Bar() >> node
    assert node.render_inline() == "<foo></foo><bar></bar>"

  def test_right_shifting_a_string_to_a_container(self):
    node = "Bar" >> Foo()   
    assert node.render_inline() == "<foo>Bar</foo>"

  def test_right_shifting_a_number_to_a_container(self):
    node = 1 >> Foo()   
    assert node.render_inline() == "<foo>1</foo>"

  def test_right_shifting_a_float_to_a_container(self):
    node = 1.23 >> Foo()   
    assert node.render_inline() == "<foo>1.23</foo>"

  def test_right_shifting_a_boolean_to_a_container(self):
    node = True >> Foo()         
    assert node.render_inline() == "<foo>True</foo>"

  def test_right_shifting_a_none_to_a_container(self):
    node = None >> Foo()   
    assert node.render_inline() == "<foo></foo>"

  def test_right_shifting_a_text_to_a_container(self):
    node = Text("bar") >> Foo()   
    assert node.render_inline() == "<foo>bar</foo>"

  def test_right_shifting_a_text_to_another_text(self):
    node = Text("bar") >> Text("foo")   
    assert node.render_inline() == "foobar"

  def test_right_shifting_a_text_to_another_text_to_a_container(self):
    node = Text("bar") >> Text("foo") >> Foo()
    assert node.render_inline() == "<foo>foobar</foo>"
  
  def test_chained_right_shifting_with_containers(self):
    node = Baz() >> Bar() >> Foo()
    assert node.render_inline() == "<foo><bar><baz></baz></bar></foo>"   

  def test_chained_right_shifting_with_text(self):
    node = "Baz" >> Bar() >> Foo()
    assert node.render_inline() == "<foo><bar>Baz</bar></foo>"  

  def test_chained_right_shifting_with_void(self):
    node = Quux() >> Bar() >> Foo()
    assert node.render_inline() == "<foo><bar><quux></bar></foo>"    

  def test_right_shifting_using_parenthesis(self):
    node = (Quux() >> Bar()) >> Foo()
    assert node.render_inline() == "<foo><bar><quux></bar></foo>" 

    node = Quux() >> (Bar() >> Foo())
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"    

class TestNodeChildrenGetting():
  def test_getting_child_at_index(self):
    node = Foo(Bar(), Baz(), Quux())
    assert node.at(1).render_inline() == "<baz></baz>" # type: ignore
    assert node.at(3) == None 

  def test_getting_first_child(self):
    node = Foo(Bar(), Baz(), Quux())
    assert node.first().render_inline() == "<bar></bar>" # type: ignore

  def test_getting_last_child(self):
    # Returns the last child
    node = Foo(Bar(), Baz(), Quux())
    assert node.last().render_inline() == "<quux>" # type: ignore

class TestNodeChildrenTaking():
  def test_taking_child_at_index(self):
    node = Foo(Bar(), Baz(), Quux())
    assert node.take_at(1).render_inline() == "<baz></baz>" # type: ignore
    assert node.render_inline() == "<foo><bar></bar><quux></foo>"
    assert node.take_at(3) == None
  def test_taking_first_child(self):
    node = Foo(Bar(), Baz(), Quux())
    assert node.take_first().render_inline() == "<bar></bar>" # type: ignore
    assert node.render_inline() == "<foo><baz></baz><quux></foo>"

  def test_taking_last_child(self):
    node = Foo(Bar(), Baz(), Quux())
    assert node.take_last().render_inline() == "<quux>" # type: ignore
    assert node.render_inline() == "<foo><bar></bar><baz></baz></foo>"

class TestNodeAdding():
  def test_adding_return_value(self):
    left, right = "Foo", Text("Bar")
    node = left + right
    assert type(node) == Root

  def test_adding_a_string_and_a_text(self):
    node = "Foo" + Text("Bar")
    assert node.render_inline() == "FooBar"

    node = Text("Bar") + "Foo"
    assert node.render_inline() == "BarFoo"

  def test_adding_an_int_and_a_text(self):
    node = 1 + Text("Bar")
    assert node.render_inline() == "1Bar"

    node = Text("Bar") + 1
    assert node.render_inline() == "Bar1"

  def test_adding_a_float_and_a_text(self):
    node = 1.23 + Text("Bar")
    assert node.render_inline() == "1.23Bar"

    node = Text("Bar") + 1.23
    assert node.render_inline() == "Bar1.23"

  def test_adding_a_text_and_a_text(self):
    node = Text("Foo") + Text("Bar")
    assert node.render_inline() == "FooBar"

  def test_adding_none_and_a_text(self):
    node = None + Text("Bar")
    assert node.render_inline() == "Bar"

    node = Text("Bar") + None
    assert node.render_inline() == "Bar"

  def test_adding_a_string_and_an_element(self):
    node = "Foo" + Quux()
    assert node.render_inline() == "Foo<quux>"

    node = Quux() + "Foo"
    assert node.render_inline() == "<quux>Foo"

  def test_adding_a_string_and_a_container(self):
    node = "Foo" + Bar()
    assert node.render_inline() == "Foo<bar></bar>"

    node = Bar() + "Foo"
    assert node.render_inline() == "<bar></bar>Foo"

  def test_adding_a_string_and_a_root(self):
    node = "Foo" + Root()
    assert node.render_inline() == "Foo"

    node = "Foo" + Root("Bar")
    assert node.render_inline() == "FooBar"

    node = Root() + "Foo"
    assert node.render_inline() == "Foo"

    node = Root("Bar") + "Foo"
    assert node.render_inline() == "BarFoo"

  def test_adding_an_element_and_another_element(self):
    node = Quux() + Fred()
    assert node.render_inline() == "<quux><fred>"

  def test_adding_an_element_and_a_container(self):
    node = Quux() + Bar()
    assert node.render_inline() == "<quux><bar></bar>"

    node = Bar() + Quux()
    assert node.render_inline() == "<bar></bar><quux>"

  def test_adding_an_element_and_a_root(self):
    node = Quux() + Root()
    assert node.render_inline() == "<quux>"

    node = Root() + Quux()
    assert node.render_inline() == "<quux>"

    node = Root(Bar()) + Quux()
    assert node.render_inline() == "<bar></bar><quux>"

    node = Quux() + Root(Bar()) 
    assert node.render_inline() == "<quux><bar></bar>"

  def test_adding_a_container_and_a_container(self):
    node = Foo() + Bar()
    assert node.render_inline() == "<foo></foo><bar></bar>"

  def test_adding_a_container_and_a_root(self):
    node = Foo() + Root()
    assert node.render_inline() == "<foo></foo>"

    node = Root() + Foo()
    assert node.render_inline() == "<foo></foo>"

    node = Root(Bar()) + Foo()
    assert node.render_inline() == "<bar></bar><foo></foo>"

    node = Foo() + Root(Bar()) 
    assert node.render_inline() == "<foo></foo><bar></bar>"

  def test_adding_a_root_and_another_root(self):
    node = Root() + Root()
    assert node.render_inline() == ""

    node = Root(Foo()) + Root(Bar())
    assert node.render_inline() == "<foo></foo><bar></bar>"

  def test_adding_multiple_nodes(self):
    node = Foo() + Text("Bar") + Quux() + "Baz"
    assert node.render_inline() == "<foo></foo>Bar<quux>Baz"   

  def test_adding_within_a_context_manager(self):
    with (node := Foo()):
      Bar() + Baz() + Quux()

    assert node.render_inline() == "<foo><bar></bar><baz></baz><quux></foo>"   

class TestNodeMultiplication():
  def test_multiplying_return_value(self):
    node = 3 * Foo()    
    assert type(node) == Root

  def test_multiplying_an_integer_and_a_text(self):
    node = 3 * Text("Bar")
    assert node.render_inline() == "BarBarBar"  

    node = Text("Bar") * 3
    assert node.render_inline() == "BarBarBar"  

    node = 2 * Text("Bar") * 2
    assert node.render_inline() == "BarBarBarBar"  

  def test_multiplying_an_integer_and_a_element(self):
    node = 3 * Quux()
    assert node.render_inline() == "<quux><quux><quux>" 

    node = Quux() * 3
    assert node.render_inline() == "<quux><quux><quux>"   

  def test_multiplying_an_integer_and_a_container(self):
    node = 3 * Foo()
    assert node.render_inline() == "<foo></foo><foo></foo><foo></foo>"  

    node = Foo() * 3
    assert node.render_inline() == "<foo></foo><foo></foo><foo></foo>"   

  def test_multiplying_a_root_and_an_integer(self):
    node = Root(Foo(), Quux()) * 2
    assert node.render_inline() == "<foo></foo><quux><foo></foo><quux>" 

    node = 2 * Root(Foo(), Quux())
    assert node.render_inline() == "<foo></foo><quux><foo></foo><quux>" 

  def test_multiplying_an_integer_and_a_root(self):
    node = 2 * Root(Foo(), Quux())
    assert node.render_inline() == "<foo></foo><quux><foo></foo><quux>" 

  def test_multiplying_an_integer_and_a_deep_element(self):
    node = 2 * Foo(Bar(), Quux())
    assert node.render_inline() == "<foo><bar></bar><quux></foo><foo><bar></bar><quux></foo>"    

  def test_multiplying_within_a_context_manager(self):
    with (node := Foo()):
      3 * Quux()

    assert node.render_inline() == "<foo><quux><quux><quux><quux></foo>" 
