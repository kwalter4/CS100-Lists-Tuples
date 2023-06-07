
def main():

 # The purpose of this program is to reformat a list for the user
 print("This program will take a string of words and return them in reverse sorted order")

 # Get input from user
 words = input("Please enter some words: ")

 # Split the list, sort it, and reverse
 words_list = words.split(" ")
 words_list.sort()
 words_list.reverse()

 # Join the list back together
 word_string = " | ".join(words_list)

 # Output the program to the user
 print(word_string)


if __name__ == '__main__':
    main()