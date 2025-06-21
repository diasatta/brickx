from brickx.elements import Document, H1, P, Title

class TestElements():  
  def test_simple_document(self) -> None:
    assert Document().render() == \
"""<!DOCTYPE html>
<html>
  <head></head>
  <body></body>
</html>"""

  def test_document(self) -> None:
    doc = Document(H1("Foo"), P("Lorem ipsum"))

    with doc.head:
      Title("Baz")

    with doc.body:
      P("Foo bar")
    
    assert doc.render() == \
"""<!DOCTYPE html>
<html>
  <head>
    <title>Baz</title>
  </head>
  <body>
    <h1>Foo</h1>
    <p>Lorem ipsum</p>
    <p>Foo bar</p>
  </body>
</html>"""    