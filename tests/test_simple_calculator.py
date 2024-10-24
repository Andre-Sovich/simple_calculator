# tests/test_simple_calculator.py

import pytest
import math
import sys
sys.path.insert(0, 'calculator\calculator.py')
import calculator as cl

# Test for squareNums function
@pytest.mark.parametrize("n, expected", [
    (5, 25),
    (6, 36),
    (-9, 81),
])
def test_squareNums(n, expected):
    """Test squareNums function with various integers"""
    assert cl.squareNums(n) == expected

# Test for cubeNums function
@pytest.mark.parametrize("n, expected", [
    (4, 64),
    (-1, -1),
    (5, 125),
])
def test_cubeNums(n, expected):
    """Test cubeNums function with various integers"""
    assert cl.cubeNums(n) == expected

# Test for triNums function
@pytest.mark.parametrize("n, expected", [
    (5, 15),
    (3, 6),
    (4, 10),
])
def test_triNums(n, expected):
    """Test triNums function with various integers"""
    assert cl.triNums(n) == expected

# Test for lazyCaterer function
@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (-2, 2),
    (3, 7),
])
def test_lazyCaterer(n, expected):
    """Test lazyCaterer function with various integers"""
    assert cl.lazyCaterer(n) == expected

# Test for magicSquares function
@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 15),
])
def test_magicSquares(n, expected):
    """Test magicSquares function with various integers"""
    assert cl.magicSquares(n) == expected

# Test for squareRoot function
@pytest.mark.parametrize("n, expected", [
    (4, 2),
    (9, 3),
    (25, 5),
])
def test_squareRoot(n, expected):
    """Test squareRoot function with various integers"""
    assert cl.squareRoot(n) == expected

# Test for polyAngle function
@pytest.mark.parametrize("n, expected", [
    (3, 180),
    (4, 360),
    (5, 540),
])
def test_polyAngle(n, expected):
    """Test polyAngle function with various integers"""
    assert cl.polyAngle(n) == expected

# Test for circArea function
@pytest.mark.parametrize("n, expected", [
    (2, 12.57),
    (3, 28.27),
    (4, 50.27),
])
def test_circArea(n, expected):
    """Test circArea function with various integers"""
    assert cl.circArea(n) == expected