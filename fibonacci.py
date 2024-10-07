#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

    - Use a function to generate Fibonacci numbers as a list
    - Use `with` statements for file operations
    - Handle potential file I/O errors with `try`/`except`
    - Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def make_fibonacci(limit):
    fibonacci_list = []
    current_num = 0
    next_num = 1
    while current_num < limit:
        fibonacci_list.append(current_num)
        next_num += current_num
        current_num = next_num - current_num		
    return fibonacci_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=int, help="Limit for the Fibonacci sequence")
    parser.add_argument("file", help="file name to save the Fibonacci list in")
    args = parser.parse_args()

    with open(args.file, 'w') as file:
        try:
            file.write(str(make_fibonacci(args.limit)))
        except:
            print("Ran into error.")
    