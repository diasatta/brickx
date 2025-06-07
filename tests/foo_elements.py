from brickx.node import Container, Element

class Foo(Container):
  tag_name: str = "foo"

class Bar(Container):
  tag_name: str = "bar"

class Baz(Container):
  tag_name: str = "baz"

class Quux(Element):
  tag_name: str = "quux"

class Fred(Element):
  tag_name: str = "fred"
