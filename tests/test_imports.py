import code_style_formatter as csf


def test_imports():
    assert "to_camel" in dir(csf)
    assert "to_snake" in dir(csf)
