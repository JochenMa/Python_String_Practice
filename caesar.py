"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The user can input a secret number.
    When the user input the cipher, the program will decipher the code.
    """
    secret_number = int(input("Secret number: "))
    if secret_number > 26:
        print("Please enter 1-26")
    else:
        cipher = input("What's the ciphered string? ")
        cipher = cipher.upper()
        new_alphabet = swift(secret_number)
        code = decipher(cipher, new_alphabet)
        print("The deciphered string is: " + str(code))


# Define new alphabet order by putting the alphabet before the secret number to the end
def swift(secret_number):
    """
    :param secret_number: int
    :return: str, the new alphabet order
    """
    new_alphabet = ALPHABET[secret_number:] + ALPHABET[:secret_number]
    return new_alphabet


# Find the index in the ALPHABET to decipher the code by putting new alphabet with same index on the string
def decipher(cipher, new_alphabet):
    """
    :param cipher: str
    :param new_alphabet: str
    :return: str, decipher answer
    """
    ans = ""
    # Check times for checking the letter is the len of the cipher
    for i in range(len(cipher)):
        ch = cipher[i]
        # Check whether is cipher is inside the new alphabet or not
        if ch in new_alphabet:
            index = ALPHABET.find(ch)
            ans += new_alphabet[index]
        # If not, put the origin cipher on the new string
        else:
            ans += cipher[i]
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
