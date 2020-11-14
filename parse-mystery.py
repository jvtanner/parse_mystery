#!/usr/bin/env python3

"""
Stanford CS106A Parse Mystery Project
"""

import sys

# Next line depends on Pillow package
from simpleimage import SimpleImage

def reverse(s):
    """
   Reverses a string.
   >>> reverse('hello')
   'olleh'
   >>> reverse('')
   ''
   >>> reverse('!!hola&&')
   '&&aloh!!'
    """
    result = ''
    for i in range(len(s)):
        result = s[i] + result
    return result


def parse_line(s):
    """
    Given a string s, parse the ints out of it and
    return them as a list of int values.
    # 3 tiny cases provided to start
    >>> parse_line('1')
    [1]
    >>> parse_line('1$')
    [1]
    >>> parse_line('12$')
    [21]
    >>> parse_line('123^')
    []
    >>> parse_line('12$34^')
    [21]
    >>> parse_line('f35^^')
    []
    >>> parse_line('123^$123$^')
    [321]
    >>> parse_line('800!)176^b006$(46$*#63Z*16$*06$z5^')
    [800, 600, 64, 63, 61, 60]
    """
    search = 0
    result = []
    while True:
        # Find first digit using 'begin' counter
        begin = search
        dont_skip = True
        while begin < len(s) and not s[begin].isdigit():
            begin += 1
        if begin >= len(s):
            break
        # Find end of digits using 'end' counter
        end = begin + 1
        while end < len(s) and s[end].isdigit():
            end += 1

        # Slice the reverse string
        if end < len(s) and s[end] == '$':
            back_number = int(reverse(s[begin:end]))
            result.append(back_number)
            dont_skip = False

        # Forget any values preceding '^'
        if end < len(s) and s[end] == '^':
            dont_skip = False

        # Slice the normal string
        if dont_skip:
            number = int(s[begin:end])
            result.append(number)
        search = end + 1
    return result


def parse_file(filename):
    """
    Given filename, parse out and return a list of all that file's
    int values.
    (test provided)
    >>> parse_file('3lines.txt')
    [800, 600, 64, 63, 61, 60, 74, 81, 55, 56]
    """
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result += parse_line(line)
        return result


def solve_mystery(filename):
    """Solve the mystery as described in the handout."""

    # SimpleImage boilerplate provided as a starting point
    nums_in_list = parse_file(filename)
    width = nums_in_list[0]  # correct values needed here
    height = nums_in_list[1]

    image = SimpleImage.blank(width, height)
    num_pixel = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            # manipulate pixel in here
            pixel.red = nums_in_list[num_pixel + 2]
            pixel.blue = nums_in_list[num_pixel + 2]
            pixel.green = nums_in_list[num_pixel + 2]
            num_pixel += 1

    # This displays image on screen
    image.show()


def main():
    # (provided code)
    # Command lines:
    # 1. -nums file.txt -> prints numbers
    # 2. file.txt -> shows image solution
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-nums':
        nums = parse_file(args[1])
        print(nums)
    if len(args) == 1:
        solve_mystery(args[0])


if __name__ == '__main__':
    main()
