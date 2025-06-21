from typing import Unpack, TypedDict
from foo_elements import Foo, Bar, Baz, Quux, Fred

class TestTextAttribute():
  def test_setting_to_a_string(self):
    assert Foo(id="quux").render_inline() == '<foo id="quux"></foo>'

  def test_setting_to_a_list(self):
    assert Foo(class_=["baz"]).render_inline() == '<foo class="baz"></foo>'

  def test_setting_multiple_attributes(self):
    assert Foo(class_=["baz"], id="quux", autofocus=True).render_inline() == '<foo class="baz" id="quux" autofocus></foo>'

  def test_setting_to_an_empty_string(self):
    assert Foo(id="").render_inline() == '<foo id=""></foo>'  

  def test_setting_to_an_empty_list(self):
    assert Foo(class_=[]).render_inline() == '<foo class=""></foo>'  

  def test_updating_wita_string(self):
    foo = Foo()
    foo._attrs["id"] = "quux"
    assert foo.render_inline() == '<foo id="quux"></foo>'

    foo._attrs["autofocus"] = True
    assert foo.render_inline() == '<foo id="quux" autofocus></foo>'

  def test_updating_wita_list(self):
    foo = Foo()
    foo._attrs["class_"] = ["bar"]
    foo._attrs["class_"] += ["baz", "foo"]
    assert foo.render_inline() == '<foo class="bar baz foo"></foo>'

class TestBooleanAttribute():
  def test_setting_to_true(self):
    assert Foo(autofocus=True).render_inline() == "<foo autofocus></foo>"

  def test_setting_to_false(self):
    assert Foo(autofocus=False).render_inline() == "<foo></foo>"

class TestDataAttribute():
  def test_creating_a_data_attribute_in_constructor(self): 
    foo = Foo(data={"baz": "foo"})
    assert foo.render_inline() == '<foo data-baz="foo"></foo>' 

  def test_creating_a_data_attribute_using_assignment(self): 
    foo = Foo()
    # foo.attrs["data"]["bar"] = "foo" # type check error
    foo.data["bar"] = "foo" # no type check error
    assert foo.render_inline() == '<foo data-bar="foo"></foo>' 

    foo.attrs["data"] = {"bar": "quux"}
    assert foo.render_inline() == '<foo data-bar="quux"></foo>' 

    foo.data = {"bar": "fred"}
    # foo.attrs["class"] += ["r"]
    assert foo.render_inline() == '<foo data-bar="fred"></foo>' 

  def test_creating_a_data_attribute_witdash(self): 
    assert Foo(data={"baz-bar": "foo"}).render_inline() == '<foo data-baz-bar="foo"></foo>'   

  def test_creating_a_data_attribute_witmultiple_values(self): 
    assert Foo(data={"baz": "foo", "quux": "fred"}).render_inline() == '<foo data-baz="foo" data-quux="fred"></foo>' 

  def test_creating_a_data_attribute_with_autocompletion(self): 
    class FooAttrs(TypedDict, total=False):
      bar: str
      quux: str

    def foo(**attrs: Unpack[FooAttrs]) -> dict[str, str]:
      d: dict[str, str] = {}
      for attr in attrs:
        d[attr] = attrs[attr]

      return d
    
    assert Foo(data=foo(bar="baz")).render_inline() == '<foo data-bar="baz"></foo>' 

    class BarAttrs(TypedDict, total=False):
      foo: str
      fred: str

    def bar(**attrs: Unpack[BarAttrs]) -> dict[str, str]:
      d: dict[str, str] = {}
      for attr in attrs:
        d[attr] = attrs[attr]

      return d

    assert Foo(data=foo(bar="baz") | bar(foo="quux", fred="baz")).render_inline() == '<foo data-bar="baz" data-foo="quux" data-fred="baz"></foo>' 

class TestAriaAttribute():
  def test_creating_an_aria_attribute(self): 
    assert Foo(aria={"baz": "foo"}).render_inline() == '<foo aria-baz="foo"></foo>'   

  def test_creating_an_aria_attribute_witunderscore(self): 
    assert Foo(aria={"baz-bar": "foo"}).render_inline() == '<foo aria-baz-bar="foo"></foo>'   

  def test_creating_an_aria_attribute_witmultiple_values(self): 
    assert Foo(aria={"baz": "foo", "quux": "fred"}).render_inline() == '<foo aria-baz="foo" aria-quux="fred"></foo>' 

class TestUserAttribute():
  def test_creating_a_user_attribute(self): 
    assert Foo(user={"baz": "foo"}).render_inline() == '<foo baz="foo"></foo>' 

  def test_creating_a_user_attribute_witunderscore(self): 
    assert Foo(user={"baz-bar": "foo"}).render_inline() == '<foo baz-bar="foo"></foo>' 
    assert Foo(user={"class": "foo"}).render_inline() == '<foo class="foo"></foo>' 
    assert Foo(user={"": "foo"}).render_inline() == '<foo ="foo"></foo>'   
    assert Foo(user={"foo_bar": "baz"}).render_inline() == '<foo foo-bar="baz"></foo>'   
    assert Foo(user={"": "baz"}).render_inline() == '<foo ="baz"></foo>'   

  def test_creating_a_standard_attribute_wituser_syntax(self): 
    assert Foo(user={"class": "foo"}).render_inline() == '<foo class="foo"></foo>' 

  def test_creating_a_user_attribute_witmultiple_values(self): 
    assert Foo(user={"baz": "foo", "quux": "fred"}).render_inline() == '<foo baz="foo" quux="fred"></foo>' 
