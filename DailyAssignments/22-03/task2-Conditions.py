# Write programs:

# Check if a number is even or odd
# Check if a person is eligible to vote (age > 18)
# Find the largest of 3 numbers


x = int(input("Enter a number: "))

print("Even" if x%2==0 else "Odd")

age = int(input("Enter your age: "))
print("Eligible to vote" if age >= 18 else "Not Eligible to vote")

a,b,c = [int(input(f"Enter number {i+1}: ")) for i in range(3)]
print(f"Max value is {max(a,b,c)}")



