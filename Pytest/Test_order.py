#pip install pytest-ordering

import pytest


@pytest.mark.run(order=1)
def test_visiting():
    print("visit the webpage")

@pytest.mark.run(order=2)
def test_max():
    print("maximize the webpage")

@pytest.mark.run(order=4)
def test_close():
    print("close the webpage")

@pytest.mark.run(order=3)
def test_click():
    print("click the webpage")