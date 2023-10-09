import pytest
""" this pytest will used in appium"""

# print("This is a Run Order class")
print("This is a Run Order class")

@pytest.mark.run(order=4)
def test_methodA():
    print("This is method A")

@pytest.mark.run(order=3)
def test_methodB():
    print("This is method B")

@pytest.mark.run(order=1)
def test_methodC():
    print("This is method C")

@pytest.mark.run(order=2)
def test_methodD():
    print("This is method D")
