from typing import TypedDict
from foo_elements import Foo


class TestTextAttribute():
  def test_setting_to_a_string(self):
    assert Foo(h_class="baz").render_inline() == '<foo class="baz"></foo>'

  def test_setting_multiple_attributes(self):
    assert Foo(h_class="baz", h_id="quux", h_autofocus=True).render_inline() == '<foo class="baz" id="quux" autofocus></foo>'

  def test_setting_to_an_empty_string(self):
    assert Foo(h_class="").render_inline() == '<foo class=""></foo>'  

class TestBooleanAttribute():
  def test_setting_to_true(self):
    assert Foo(h_autofocus=True).render_inline() == "<foo autofocus></foo>"

  def test_setting_to_false(self):
    assert Foo(h_autofocus=False).render_inline() == "<foo></foo>"

class TestDataAttribute():
  def test_creating_a_data_attribute(self): 
    assert Foo(data={"baz": "foo"}).render_inline() == '<foo data-baz="foo"></foo>'   

  def test_creating_a_data_attribute_with_underscore(self): 
    assert Foo(data={"baz-bar": "foo"}).render_inline() == '<foo data-baz-bar="foo"></foo>'   

  def test_creating_a_data_attribute_with_multiple_values(self): 
    assert Foo(data={"baz": "foo", "quux": "fred"}).render_inline() == '<foo data-baz="foo" data-quux="fred"></foo>' 

class TestAriaAttribute():
  def test_creating_an_aria_attribute(self): 
    assert Foo(aria={"baz": "foo"}).render_inline() == '<foo aria-baz="foo"></foo>'   

  def test_creating_an_aria_attribute_with_underscore(self): 
    assert Foo(aria={"baz-bar": "foo"}).render_inline() == '<foo aria-baz-bar="foo"></foo>'   

  def test_creating_an_aria_attribute_with_multiple_values(self): 
    assert Foo(aria={"baz": "foo", "quux": "fred"}).render_inline() == '<foo aria-baz="foo" aria-quux="fred"></foo>' 

class TestUserAttribute():
  def test_creating_a_user_attribute(self): 
    assert Foo(user={"baz": "foo"}).render_inline() == '<foo baz="foo"></foo>' 

  def test_creating_a_user_attribute_with_underscore(self): 
    assert Foo(user={"baz-bar": "foo"}).render_inline() == '<foo baz-bar="foo"></foo>' 
    assert Foo(user={"h_class": "foo"}).render_inline() == '<foo h-class="foo"></foo>' 
    assert Foo(user={"h_": "foo"}).render_inline() == '<foo h-="foo"></foo>'   
    assert Foo(user={"foo_bar": "baz"}).render_inline() == '<foo foo-bar="baz"></foo>'   
    assert Foo(user={"": "baz"}).render_inline() == '<foo ="baz"></foo>'   

  def test_creating_a_standard_attribute_with_user_syntax(self): 
    assert Foo(user={"class": "foo"}).render_inline() == '<foo class="foo"></foo>' 

  def test_creating_a_user_attribute_with_multiple_values(self): 
    assert Foo(user={"baz": "foo", "quux": "fred"}).render_inline() == '<foo baz="foo" quux="fred"></foo>' 

  def test_creating_a_user_attribute_with_a_typed_dict(self): 
    class UserAttr1(TypedDict, total=False):
      bar: str
      baz: str

    class UserAttr2(TypedDict, total=False):
      bar: str
      baz: str

    assert Foo(user=UserAttr1(bar="quux")).render_inline() == '<foo bar="quux"></foo>' 
    assert Foo(user=UserAttr1(bar="quux") | UserAttr2(baz="fred")).render_inline() == '<foo bar="quux" baz="fred"></foo>' 
  