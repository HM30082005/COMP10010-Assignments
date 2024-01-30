# # assignment 5 (38%)
# •To be submitted through Brightspace by Sun Nov 26th at 23:59 in any time zone of your choice (I suggest Baker Island time).
# •Worth 38% of the final mark!
# •You lose 1/3 grade for each 2 days you are late (e.g. if you deserve A you get A- if you are 1 day late, B+ 2 days, etc.).
# •
# •In this assignment you will have to deal with files and functions.
# •You are asked to read 1000 floats from a file, which is provided to you (floats.txt). The floats have to be read into a list.
# •Within your program you need to create a function insertion_sort(float_list) that takes as argument a list of floating point 
# numbers and sorts it in ascending order (smallest first) using the Insertion Sort algorithm (see next slide).
# •After reading the floats from the file into a list, your main program should call the insertion_sort function, then it should:
# 1) print the now sorted list onto the screen; 
# 2) write the sorted list onto a file (sorted_floats.txt).


# Define the insertion_sort function to sort a list using Insertion Sort algorithm
def insertion_sort(arr):
    # if array contains only one element then it is already sorted, so we just return it
    if len(arr) == 1:
        return arr
    # Iterate through each element in the list starting from the second element
    for i in range(1, len(arr)):
        j = i
        # Compare the current element with the previous ones and swap if necessary to ensure ascending order
        while arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            # Break the loop if the element has reached the beginning of the list
            if j == 0:
                break
    return arr

# Open the file "floats.txt" in read mode
f = open("floats.txt", "r")

# Read all lines from the file into a list
float_list = f.readlines()

# Close the file
f.close()
n = len(float_list)
# Convert each string element in the list to a float
for i in range(n):
    float_list[i] = float(float_list[i])

# Call the insertion_sort function to sort the list of floats
float_list1 = insertion_sort(float_list)

# Print the sorted list to the screen
for i in float_list1:
    print(i)

# Open a new file "sorted_floats.txt" in write mode
f1 = open("sorted_floats.txt", "w")

# Write each sorted float to the file with a newline character
for i in float_list1:
    f1.write(str(i) + "\n")

# Close the file
f1.close()
