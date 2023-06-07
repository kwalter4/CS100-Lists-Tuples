
def main():
# The purpose of this program is to print the average of five numbers
# Get info from the user
 print("This program will take five numbers and return the average")
 input_list = input("Please enter five numbers separated by commas: ")


# Split numbers from the list
 input_list = input_list.split(",")
 list1 = []
 list1.append(int(input_list[0]))
 list1.append(int(input_list[1]))
 list1.append(int(input_list[2]))
 list1.append(int(input_list[3]))
 list1.append(int(input_list[4]))

# list.append(int(input_list[]))
 list1[0] = int(input_list[0])
 list1[1] = int(input_list[1])
 list1[2] = int(input_list[2])
 list1[3] = int(input_list[3])
 list1[4] = int(input_list[4])

# Add up the five numbers inputted from user
 total = list1[0] + list1[1] + list1[2] + list1[3] + list1[4]
 total = float(total)

# Divide by the total number of inputs
 sample = len(list1)
 sample = float(sample)
 average = total / sample
 print("The Average is", average)

#
if __name__ == '__main__':
    main()

