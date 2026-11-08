
#pip install pytest-dependency

#pip install pytest-html - for report


import pytest

@pytest.mark.dependency
def test_one():
    print("test case one")
    print(4/0);

@pytest.mark.dependency(depends=["test_one"])
def test_two():
    print("test case two")

"""
dependency = depend on the first testcase incase test one failed mean test two skipped
 suite run = py.test -v -s 
 suite report =py.test -v -s --html=suite.html --capture=sys
"""