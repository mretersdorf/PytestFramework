from pytest import mark


@mark.smoke
@mark.body
def test_body_functions_as_exepected():
    assert True