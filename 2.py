# -*- coding: utf-8 -*-

def display_even_numbers(start, end):

    if start > end:
        start, end = end, start  # Swap if start is greater than end

    even_numbers = []
    for number in range(start, end + 1):
        if number % 2 == 0: 
            even_numbers.append(number)

    
    if even_numbers:
        print("Even numbers between", start, "and", end, ":", even_numbers)
    else:
        print("No even numbers between", start, "and", end)


display_even_numbers(3, 15)
display_even_numbers(10, 5)
display_even_numbers(1, 1)
