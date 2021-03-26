"""
File: similarity.py
Name: Jo
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main() -> object:
    """
    The user can input one long sequence and one short sequence to find the best match
    The best match is the sequence in long sequence which has the highest score
    Also, the user can get the similarity rate
    """
    long_sequence = input("Please give me a DNA sequence to search: ")
    short_sequence = input("What DNA sequence would you like to match? ")
    # Case-sensitive
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    # The score start with 0
    score = 0
    best_match = homology(short_sequence, long_sequence, score)
    print("The best match is: " + str(best_match))


def homology(short_sequence, long_sequence, score):
    """
    :param short_sequence: str, upper letters
    :param long_sequence: str, upper letters
    :param score: int, start with o
    :return: str, the best math sequence
    """
    # If the short sequence is completely the same as sequence in long one
    if short_sequence in long_sequence:
        print("The similarity is: 100%")
        return short_sequence
    else:
        # The max score start with 0
        max_score = score
        ans = ""
        # The times of loop is equal to the len of long sequence - len of short sequence +1
        for i in range(len(long_sequence)-len(short_sequence)+1):
            # The times for program to check every DNA
            for j in range(len(short_sequence)):
                # Pairing the same DNA and give it the score
                if short_sequence[j] == long_sequence[i+j]:
                    score = score+1
            # If the score is higher than the max, copy it
            if max_score < score:
                max_score = score
                ans = long_sequence[i:i+len(short_sequence)]
                similarity = round((max_score/len(short_sequence)), 2)*100
            # The score will start with 0 again
            score = 0
        print("The similarity is: " + str(similarity) + "%")
        return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
