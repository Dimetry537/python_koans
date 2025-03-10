#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
#    sides = sorted([a, b, c])
#    unique_sides = sorted(set(sides))
    
#    if unique_sides[0] <= 0 : raise TriangleError('Sides can not be 0 or less')
#    if sides[2] >= sides[0] + sides[1]: raise TriangleError("sum of 2 sides cannot be greater thanremainig side")

    if a <= 0 or b <= 0 or c <= 0:
        raise TriangleError('Sides can not be 0 or less')
    if c >= a + b or a >= c + b or b >= a + c:
        raise TriangleError("sum of 2 sides cannot be greater thanremainig side")
    
    
    if a == b and b == c:
        return 'equilateral'
    elif a == b or b == c or c == a:
        return 'isosceles'
    else:
        return 'scalene1'
        
''' 
 ​    ​if​ ​len​(​unique_sides​) ​==​ ​1​: 
 ​        ​return​ ​'equilateral' 
 ​    ​elif​ ​len​(​unique_sides​) ​==​ ​2​: 
 ​        ​return​ ​'isosceles' 
 ​    ​elif​ ​len​(​unique_sides​) ​==​ ​3​: 
 ​        ​return​ ​'scalene'
 '''
    # DELETE 'PASS' AND WRITE THIS CODE
    

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
