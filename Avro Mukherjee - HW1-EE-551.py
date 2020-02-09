"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y
    y = "Stevens"
    # Repeat variable y 5 times
    z=(y*5)
    print(z)
    Output: stevensstevensstevensstevensstevens
    # What is the length of z?
    length = len(z)
    print(length)
    Output: 35
    # Concatenate variable y with string " is good"
    m = y + ' is good'
    print(m)
    output: Stevens is good
    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m.replace('good','awesome')
    print(n)
    output: Stevens is awesome
    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = [n.split(' ')]
    print(p)
    Output: ['stevens', 'is', 'awesome']

    # Get all the items past the first of the third substring
    r = print(p[0:2])
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]

    from numpy import *
    r = array([[1, 4, 5],
               [6, 10, 11],
               [12, 17, 38]
               ])
    m = matrix(r)
    print(m)


output:
    [[1  4  5]
     [6 10 11]
    [12 17 38]]

    # Collect the items in the last column of matrix A using list comprehension

c = [i for i in (m[:,2]) ]
print(str(c))
output: [5, 11, 38]


    # Collect only the even items of the diagonal of matrix A using list comprehension
d = [i for i in diagonal(m) if i%2 == 0]
print(str(d))

Output:[10, 38]

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.

o = [ord(i) for i in y]
print(o)
Output: [115, 116, 101, 118, 101, 110, 115]

    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"

    f = {'fruit': 'apple', 'quantity': '4', 'color': 'green'}
    print(f)
    output: {'fruit': 'apple', 'quantity': '4', 'color': 'green'}


    # Get the item in dictionary f that the key "fruit" maps to
    print(a.get('fruit'))
    output: apple

    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f['quantity'] = '5'
    print(f)
    output: {'fruit': 'apple', 'quantity': '5', 'color': 'green'}


    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    Name = 'Grace Hopper'
    k = {Name: {'first_name': 'Grace', 'Last_name': 'Hopper'}}
    l = ['scientist', 'engineer']
    age = 85



    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    l.append('programmer')
    print(l)
    output: ['scientist', 'engineer', 'programmer']

    # Get the third job Grace has that you recently added
    print(l[-1])
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    t = 'amazing_grace'
    (sorted(t))
    ['_', 'a', 'a', 'a', 'c', 'e', 'g', 'g', 'i', 'm', 'n', 'r', 'z']
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()
