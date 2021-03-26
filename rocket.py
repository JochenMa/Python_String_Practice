"""
File: rocket.py
Name: Jo
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


# The head is a pyramid with the same width and length as the SIZE. It is divided into right and left, j and k loop
def head():
	for i in range(SIZE):
		print(" ", end="")
		for j in range(SIZE):
			if int(i+j) < int(SIZE-1):
				print(" ", end="")
			else:
				print("/", end="")
		for k in range(SIZE):
			if int(i-k) >= 0:
				print("\\", end="")
			else:
				print(" ", end="")
		print("")


# Start and end with "+", and the number of "=" is two times of SIZE
def belt():
	print("+", end="")
	for i in range(SIZE):
		print("=", end="")
		print("=", end="")
	print("+")


# The head is a pyramid with the same width and length as the SIZE. It is divided into right and left, j and k loop
def upper():
	for i in range(SIZE):
		print("|", end="")
		for j in range(SIZE):
			# Number of "."
			if int(i+j) <= int(SIZE-2):
				print(".", end="")
			else:
				if int(SIZE) % 2 == 0:
					# If the SIZE is even and i+j is odd
					if int(i+j) % 2 != 0:
						print("/", end="")
					# If the SIZE is even and i+j is even
					else:
						print("\\", end="")
				else:
					# If the SIZE is odd and i+j is even
					if int(i+j) % 2 == 0:
						print("/", end="")
					# If the SIZE is odd and i+j is odd
					else:
						print("\\", end="")
		for k in range(SIZE):
			# Number of "."
			if int(i - k) < 0:
				print(".", end="")
			else:
				if int(SIZE) % 2 != 0:
					# If SIZE is odd and i+k is even
					if int(i + k) % 2 == 0:
						print("\\", end="")
					# If SIZE is odd and i+k is odd
					else:
						print("/", end="")
				else:
					# If SIZE is even and i+k is even
					if int(i + k) % 2 == 0:
						print("\\", end="")
					# If SIZE is even and i+k is odd
					else:
						print("/", end="")
		print("|")


# Similar logic to upper
def lower():
	for i in range(SIZE):
		print("|", end="")
		for j in range(SIZE):
			if int(i-j) > 0:
				print(".", end="")
			else:
				if int(SIZE) % 2 == 0:
					if int(i+j) % 2 != 0:
						print("/", end="")
					else:
						print("\\", end="")
				else:
					if int(i+j) % 2 == 0:
						print("\\", end="")
					else:
						print("/", end="")
		for k in range(SIZE):
			if int(i+k) > int(SIZE-1):
				print(".", end="")
			else:
				if int(SIZE) % 2 != 0:
					if int(i + k) % 2 == 0:
						print("/", end="")
					else:
						print("\\", end="")
				else:
					if int(i + k) % 2 == 0:
						print("\\", end="")
					else:
						print("/", end="")
		print("|")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()