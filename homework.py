# N_1 masala

nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]

# creating iterator  
iterator = iter(nums)

# A variable that holds the sum of even numbers
total_even = 0

# Cycle through an iterator with a while loop
while True:
    try:
        # Getting the next element through an iterator
        num = next(iterator)
        
        # If the number is even, its sum
        if num % 2 == 0:
            total_even += num
    except StopIteration:
        # We stop the loop until the iterator is finished
        break

print("Sum of even numbers:", total_even)



# N_2 masala

# open and write the test.txt file
with open("test.txt", "w") as file:
    for i in range(1, 101):
        file.write(str(i) + "\n")
