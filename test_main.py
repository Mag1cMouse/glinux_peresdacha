from main import greet, add, multiply, get_info


def test_greet():
    assert greet("Мир") == "Привет, Мир!"
    assert greet("Python") == "Привет, Python!"


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(100, 200) == 300


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6
    assert multiply(7, 7) == 49


def test_get_info():
    info = get_info()
    assert isinstance(info, dict)
    assert "author" in info
    assert "subject" in info
    assert "topic" in info


def test_greet_returns_string():
    result = greet("Test")
    assert isinstance(result, str)
