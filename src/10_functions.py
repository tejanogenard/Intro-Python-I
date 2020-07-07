# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x % 2 == 0:
        print(f"{x} is an even number")
        return True
    elif x % 1 == 0:
        print(f"{x} is an Odd number")
        return False
        
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
 # YOUR CODE HERE
if num % 2 == 0: 
    print("Even!")
elif num % 1 == 0:
    print("Odd!")

