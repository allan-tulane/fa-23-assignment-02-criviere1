from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(8), BinaryNumber(7)) == 8*7
    assert subquadratic_multiply(BinaryNumber(1), BinaryNumber(4)) == 1*4
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(3)) == 4*3
