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

EQUILATERAL_SIDES = 1
ISOSCELES_SIDES = 2
SCALENE_SIDES = 3
MINIMUM_SIDE_SIZE = 0

RULES = {
  EQUILATERAL_SIDES: 'equilateral',
  ISOSCELES_SIDES: 'isosceles',
  SCALENE_SIDES: 'scalene'
}

def triangle(a, b, c):
    sides = check_sides_length(a, b, c)
    check_sides_sum(a, b, c)
    return unique(sides)

def unique(sides):
    unique_sides = len(set(sides))

    return RULES[unique_sides]

def check_sides_length(a, b, c):
  sides = [a, b, c]

  for side in sides:
    if side <= MINIMUM_SIDE_SIZE:
      raise TriangleError('A side must be a positive integer')

  return sides
# Error class used in part 2.  No need to change this code.

def check_sides_sum(a, b, c):
  if ((a + b) < c or (a + c) < b or (b + c) < a):
    raise TriangleError('Illegal sides sum')

class TriangleError(Exception):
    pass
