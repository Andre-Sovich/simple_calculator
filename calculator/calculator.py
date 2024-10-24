"""This module contains the calculator functions for the formulas square, tri, lazy caterer, and magic squares"""
import math

def squareNums(n):
    """Calculates the square"""
    return n**2

def triNums(n):
    """Calculates the tri number"""
    return (n * (n + 1)) / 2


def lazyCaterer(n):
    """Calculates the lazy caterer number"""
    return (n**2 + n + 2) / 2


def magicSquares(n):
    """Calculates the magic squares number"""
    return (n * (n**2 + 1)) / 2

def squareRoot(n):
    """Calculates the square root of number"""
    return math.sqrt(n)

def polyAngle(n):
    """Calculates the interior angle of a polygon of a given size"""
    return (n-2) * 180

def circArea(n):
    """Calculates the area of a circle of a given radius"""
    return round(math.pi * n**2, 2)


    

def run_calculator(input_formula, input_num):
    """Calls and returns results for the specified formulas"""
    calculator = [squareNums, triNums, lazyCaterer, magicSquares, squareRoot,polyAngle,circArea]
    formula = calculator[input_formula - 1]
    return_result = formula(input_num)
    return return_result



if __name__ == "__main__":
    print(
        "Choose which formula to use: 1 for square, 2 for tri, 3 for lazy caterer, 4 for magic squares, 5 for square root, 6 for polygon angle, and 7 for circle area"
    )
    input_formula = int(input())
    print(
        "Enter a number to calculate the square, tri, lazy caterer, magic squares numbers, square root, polygon angle, or circle area"
    )
    input_num = int(input())

    result = run_calculator(input_formula, input_num)
    print(result)
