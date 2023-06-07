# Strings, Lists and Tuples

In this assignment you'll have 5 python programs to complete.  You must use lists or tuples to solve the problems. 

## 1) elements.py

This is a simple task of accessing elements (pune intended) of a Tuple.  The file has a Tuple Table (Tuple of Tuples) named ELEMENTS which contains the first 50 elements of the periodic table.  The program should ask the user for the element number 1-50 then output a string, using the string formatting tools we learned in class, that shows the elements Name, Symbol, and Atomic Mass. The string should look something like this: `Hydrogen (H) with an Atomic Mass of 1.007`

Additionally, the program should have error checking to prevent the user from entering a number greater than 50 or less than 1.  If the user enters a number outside of the 1-50 range print an error message that includes the word "error". 

Example:

![Elements](images/elements.png)

## 2) average_of_five.py
This program should take a list of 5 number separated by commas on one line and prints the average of the numbers.  To accomplish this you'll need use the 'split' method on the list.  Remember that the list will be made up of strings so you'll need to typecast them into integers.
 
Example:

![Average](images/average_of_five.png)


## 3) sorter.py 

This program will take an input of words separated by spaces for example `bannana apple orange grape`. The inputted string will then need to be `split` on the commas to create a list.  That list of words then be `sort`ed and `reverse`d. Before being `join`ed back together and printed.  To perform the join you'll need to call join on a string space passing in the list as an argument like this: `" ".join(word_list)`.  The number wor words should not matter, you program should work with 1 word, 25 words or more. 

Example: 

![sorter](images/sorter.png)

## 4) radii.py
For this problem you'll have the user enter 4 numbers that represent the radius of 4 circles separated by commas.  The program will then print out the circle areas separated by dashes.  You need to use lists for this I want your code to:

1. Split the text input into a list 
2. Replace the values of each radius in the list with the area 
3. Join the list back together as a string using a dash as the separator 
4. Print that string.

Don't worry about rounding or limiting the precision of the float output.

Example:

![Elements](images/radii.png)

## 5) names.py 

This one might be a bit of a challenge.  The program should ask the user for 5 full names (first last).  Have them enter each name on a new line.  You then need to split each name into a list on the spaces, and put it back together in the format "last, first".  Then append all the names to a list so you can sort it.  They print out each name, one per a line, in sorted order.  

![Sorter](images/name.png)

## Style matters (10 points)
Comment your code, use good variable names, use spacing to group logic and all the things that make code readable. 




 

