import pytest
from brickx.node import Node

class Test():
  def test(self):
    assert Node().tag_name == "node"
    assert 1 == 1
    assert 2 == 2