#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
from fibonacci import make_fibonacci
import argparse

def main():
	fibonacci_list = make_fibonacci(args.limit)
	largest = 0
	for num in fibonacci_list:
		if is_prime(num):
			largest = num
	print(f'The largest prime number in fibonacci sequence under {args.limit} is {largest}.')

def is_prime(number):
	if number <= 1:
		return False
	for i in range(2, number):
		if number%i == 0:
			return False
	return True
	
if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("limit", type=int, help="Limit for the Fibonacci sequence")
	args = parser.parse_args()
	main()