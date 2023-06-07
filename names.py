
def main():
 #
# The purpose of this program is to rewrite a list of names
 print("This program will take 5 names reformat them to 'last, first' and alphabetize them.")

# Now we will get some input from the user
 name1 = input("Enter a name: ")
 name2 = input("Enter a name: ")
 name3 = input("Enter a name: ")
 name4 = input("Enter a name: ")
 name5 = input("Enter a name: ")

# Append the input into a list
 list = []
 list.append(name1)
 list.append(name2)
 list.append(name3)
 list.append(name4)
 list.append(name5)

 #Reverse the List
 list.reverse(list)

 # Split list
 split_list = split.list_rev(",")
 print(split_list)



if __name__ == '__main__':
    main()