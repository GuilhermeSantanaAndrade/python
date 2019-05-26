import pytest
from test_op import somar
from test_op import subtrair

def test_somar():
    assert somar(2,3) == 5

def test_subtrair():
    assert subtrair(5,3) == 2