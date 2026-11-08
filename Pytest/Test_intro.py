import pytest

def test_one():
    print("test case 1")

@pytest.mark.M1
def test_method1():
    print("test case 2")

@pytest.mark.M2
def test_method2():
    print("test case 3")

@pytest.mark.LOGIN
def test_login():
    print("test case 4")

    # pytest filename.py
    # pytest filename.py -v
    # pytest filename -v -s
    # filtering according to the keyword pytest filename.py -v -s -k "keyword"
    # pytest filename.py -v -s -k "marking word"
    # pip install pytest-html
    # pytest filename -v -s --html=name.html --capture=sys

    """Execute test suites"""
    # py.test
    # py.test  -v
    # py.test  -v -s
    # filtering according to the keyword py.test  -v -s -k "keyword"
    # py.test f-v -s -k "marking word"
    # pip install pytest-html
    # py.test  -v -s --html=name.html --capture=sys