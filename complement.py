"""
File: complement.py
Name: Jo
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The user can input the DNA strand, and the program will find the complement strand
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    # Case-insensitive
    dna = dna.upper()
    new_dna = build_complement(dna)
    print("The complement of " + str(dna) + " is " + str(new_dna))


def build_complement(dna):
    """
    :param dna: str, ATGC
    :return: str, the complement DNA
    """
    ans = ""
    # The rule of the complement DNA
    for base in dna:
        if base == 'A':
            ans += 'T'
        if base == 'T':
            ans += 'A'
        if base == 'C':
            ans += 'G'
        if base == 'G':
            ans += 'C'
    return ans




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
