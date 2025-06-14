import pytest
from brickx.style import StyleSheet
from brickx.styler import  Styler, InlineStyler, SpecificStyler, AtomicStyler
from brickx.node import Element, Container

class TestRuleNormalizing():
  def test_normalizing_a_rule_with_default_media(self):
    style: StyleSheet = {
      "rule": {
        "color": "black",
        "background-color": "white",
        ":hover": {
          "background-color": "blue"
        }
      }
    }

    styler: Styler = Styler(style["rule"])

    assert styler.normalize(style["rule"]) == {
      "": {
        "": {
          "color": "black",
          "background-color": "white", 
        },
        ":hover": {
          "background-color": "blue", 
        }
      }
    }

  def test_normalizing_a_rule_with_extra_prop(self):
    style: StyleSheet = {
      "rule": {
        "color": "black",
        "padding-x": "0px",        
      }
    }

    styler: Styler = Styler(style["rule"])

    assert styler.normalize(style["rule"]) == {
      "": {
        "": {
          "color": "black",
          "padding-left": "0px",
          "padding-right": "0px",
        },
      }
    }

  def test_normalizing_a_rule_with_media(self):
    style: StyleSheet = {
      "rule": {
        "@media": "min-width: 700px",
        "color": "black",
        "background-color": "white",
        ":hover": {
          "background-color": "blue"
        }
      }
    }

    styler: Styler = Styler(style["rule"])

    assert styler.normalize(style["rule"]) == {
      "min-width: 700px": {
        "": {
          "color": "black",
          "background-color": "white", 
        },
        ":hover": {
          "background-color": "blue", 
        }
      }
    }

  def test_normalize_a_complex_rule(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler: Styler = Styler(style["rule"])

    assert styler.normalize(style["rule"]) == {
      "": {
        "": {
          "color": "red",
          "border": "1px solid white",
        },
        ":hover:disabled": {
          "color": "blue",
        },
        ":hover": {
          "background-color": "black",
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

class TestStyle():
  def test_declaration(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = SpecificStyler(style["rule"])

    assert styler.declaration("", "", "color") == "color: red;"
    assert styler.declaration("", ":hover:disabled", "color") == "color: blue;"
    assert styler.declaration("", ":hover", "background-color") == "background-color: black;"
    assert styler.declaration("", "", "border") == "border: 1px solid white;"

  def test_specific_class_name(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = SpecificStyler(style["rule"])

    assert styler.class_name("", ":hover:disabled", "color") == "s66a208b"
    assert styler.class_name("") == "s66a208b"

  def test_atomic_class_name(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = AtomicStyler(style["rule"])

    assert styler.class_name("", ":hover:disabled", "color") == "a30ef48f"
    assert styler.class_name("", "", "color") == "a2296f0d"

  def test_specific_selector(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = SpecificStyler(style["rule"])

    assert styler.selector("", "") == "s66a208b"
    assert styler.selector("", "", "border") == "s66a208b"
    assert styler.selector("", ":hover:disabled", "color") == "s66a208b:hover:disabled"
    assert styler.selector("", ":focus") == "s66a208b:focus"

  def test_atomic_selector(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = AtomicStyler(style["rule"])

    assert styler.selector("", "", "color") == "a2296f0d"
    assert styler.selector("", "", "border") == "a8b4be93"
    assert styler.selector("", ":hover:disabled", "color") == "a30ef48f:hover:disabled"
    assert styler.selector("", ":focus", "cursor") == "a38624e5:focus"

  def test_atomic_classes(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = AtomicStyler(style["rule"])

    assert styler.classes() == {
      "": {
        "0": {
          "a2296f0d": {"color": "red"},
          "a8b4be93": {"border": "1px solid white"}, 
          "ab0e91e9:hover": {"background-color": "black"}, 
          "a38624e5:focus": {"cursor": "pointer"},
        },
        "1": {
          "a30ef48f:hover:disabled": {"color": "blue"}, 
        }
      }
    }

  def test_specific_classes(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = SpecificStyler(style["rule"])

    assert styler.classes() == {
      "": {
        "s66a208b": {
          "color": "red",
          "border": "1px solid white", 
        },
        "s66a208b:focus": {
          "cursor": "pointer",
        },
        "s66a208b:hover": {
            "background-color": "black",
        },
        "s66a208b:hover:disabled": {
          "color": "blue",
        },
      }
    }

  def test_atomic_classe_names(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = AtomicStyler(style["rule"])

    assert styler.class_names() == ["a2296f0d", "a8b4be93", "ab0e91e9", "a38624e5", "a30ef48f1"]

  def test_specific_classe_names(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = SpecificStyler(style["rule"])

    assert styler.class_names() == ["s66a208b"]

  def test_atomic_render(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = AtomicStyler(style["rule"])

    assert styler.render(styler.classes()) == \
""".a2296f0d { color: red; }
.a8b4be93 { border: 1px solid white; }
.ab0e91e9:hover { background-color: black; }
.a38624e5:focus { cursor: pointer; }
.a30ef48f1:hover:disabled { color: blue; }
"""

  def test_specific_render(self):
    style: StyleSheet = {
      "rule": {
        "color": "red",
        "border": ("1px", "solid", "white"),
        ":hover": {
          ":disabled":   {
            "color": "blue",
          },
          "background-color": "black"
        },
        ":focus": {
          "cursor": "pointer"
        }
      }     
    }

    styler = SpecificStyler(style["rule"])

    assert styler.render(styler.classes()) == \
""".s66a208b {
  color: red;
  border: 1px solid white;
}
.s66a208b:hover {
  background-color: black;
}
.s66a208b:hover:disabled {
  color: blue;
}
.s66a208b:focus {
  cursor: pointer;
}
"""

class TestPropResolution():    
  def test_counting_conflicts_with_empty_conflicts(self):
    styler = AtomicStyler()

    conflicts = {} 
    layer = styler._conflict_count("border-color", conflicts)

    assert layer == -1

  def test_counting_conflicts_with_a_non_conflicting_prop(self):
    styler = AtomicStyler()
    conflicts = {
      'color': 0,
      'color$': 2,
    } 

    assert styler._conflict_count("color", conflicts) == 2

  def test_counting_conflicts_with_a_conflicting_prop(self):
    styler = AtomicStyler()

    conflicts = {
      'border-color': 0, 
      'border-color$': 0,
      'border-bottom-color$': 0, 
      'border-left-color$': 3, 
      'border-right-color$': 1, 
      'border-top-color$': 0, 
      'border-top-style$': 10, 
      'color': 6,
    } 

    count = styler._conflict_count("border-color", conflicts)

    assert count == 3 

  def test_resolving_conflicts(self):
    styler = AtomicStyler()

    conflicts = {
      'border-color': 0, 
      'border-color$': 0,
      'border-bottom-color$': 0, 
      'border-left-color$': 3, 
      'border-right-color$': 1, 
      'border-top-color$': 0, 
      'border-top-style$': 10, 
      'color': 6,
    } 
   
    styler._resolve("border-color", conflicts)

    assert conflicts == {
      'border-color': 4, 
      'border-color$': 4,
      'border-bottom-color$': 4, 
      'border-left-color$': 4, 
      'border-right-color$': 4, 
      'border-top-color$': 4, 
      'border-top-style$': 10, 
      'color': 6,
    }

    styler._resolve("border-top-color", conflicts)

    assert conflicts == {
      'border-color': 4, 
      'border-color$': 4,
      'border-top-color': 5, 
      'border-bottom-color$': 4, 
      'border-left-color$': 4, 
      'border-right-color$': 4, 
      'border-top-color$': 5, 
      'border-top-style$': 10, 
      'color': 6,
    }

class TestRuleLayers():    
  def test_classes_with_non_conflicting_props(self):
    style: StyleSheet = {
      "rule1": {
        "border-width": "1px",
        "border-style": "solid",
        ":hover": {
          "color": "blue"
        }
      },
      "rule2": {        
        "border-width": "2px",
      },
      "rule3": {       
        "@media": "media", 
        "width": "0.125rem",
      }
    }

    styler = AtomicStyler(style["rule1"], style["rule2"], style["rule3"])

    assert styler.classes() == {
      "": { 
        "0": {
          "a900f0eb": {"border-width": "2px"}, 
          "a594b855": {"border-style": "solid"},
          "a30ef48f:hover": {"color": "blue"},
        }
      },
      "media": {
        "0": {
          "a2e4465a": {
            "width": "0.125rem",
          },
        },
      },
    }

  def test_classes_with_conflicting_props(self):
    style: StyleSheet = {
      "rule1": {
        "border-width": "1px",
        "border-style": "solid",
        "border-top-style": "dotted",
        ":hover": {
          "color": "blue"
        }
      },
    }

    styler = AtomicStyler(style["rule1"])

    assert styler.classes() == {
      "": { 
        "0": {
          "a8d6e0e8": {"border-width": "1px"}, 
          "a594b855": {"border-style": "solid"},
          "a30ef48f:hover": {"color": "blue"},
        },
        "1": {
          "a051471b": {"border-top-style": "dotted"}, 
        }
      },
    }

class TestElementStyling():
  def test_element_with_specific_style(self):
    style: StyleSheet = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      }
    }

    foo = Element(style=[style["rule1"], style["rule2"]])  
    foo.styler = SpecificStyler()
    assert foo.render_inline() == '<element class="se6dacc8">'

    bar = Element() 
    bar.style = [style["rule1"], style["rule2"]] 
    bar.styler = SpecificStyler()
    assert foo.render_style() == bar.render_style()

    assert foo.render_style() == \
""".se6dacc8 {
  background-color: blue;
  color: black;
}
.se6dacc8:hover {
  background-color: red;
}
"""    

  def test_element_with_atomic_style(self):
    style: StyleSheet = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      }
    }

    foo = Element(style=[style["rule1"], style["rule2"]])  
    foo.styler = AtomicStyler()
    assert foo.render_inline() == '<element class="a6fa6fa2 a94fac93 a5bc668f1">'

    bar = Element() 
    bar.style = [style["rule1"], style["rule2"]] 
    bar.styler = AtomicStyler()
    assert foo.render_style() == bar.render_style()

    assert foo.render_style() == \
""".a6fa6fa2 { background-color: blue; }
.a94fac93 { color: black; }
.a5bc668f1:hover { background-color: red; }
""" 

  def test_element_with_inline_style(self):
    style: StyleSheet = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      }
    }

    foo = Element(style=[style["rule1"], style["rule2"]])  
    foo.styler = InlineStyler()

    assert foo.render_inline() == '<element style="background-color: blue; color: black;">'

  def test_nested_element_css(self):
    style: StyleSheet = {
      "rule1": {
        "background-color": "white",
        "color": "black",
        ":hover": {
          "background-color": "blue"
        }
      },
      "rule2": {
        "background-color": "blue",
        ":hover": {
          "background-color": "red"
        }
      },
      "rule3": {
        "background-color": "green",
      }
    }

    baz = Element(style=style["rule3"])
    foo = Container(baz, style=style["rule1"])
    bar = Container(foo, style=style["rule2"])
    bar.styler = SpecificStyler()

    assert bar.render_style() == \
""".s229c421 {
  background-color: blue;
}
.s229c421:hover {
  background-color: red;
}
.s429f63f {
  background-color: white;
  color: black;
}
.s429f63f:hover {
  background-color: blue;
}
.sf1da6fa {
  background-color: green;
}
"""      
