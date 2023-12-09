# Initialize the total to 0
total = 0

# Ask the user for input
input_str = input("Enter a number (or 'done' to stop): ")

# Use a while loop to continually ask for numbers until the user enters 'done'
while input_str != 'done':
  # Convert the user's input to a number
  number = int(input_str)

  # Add the number to the total
  total += number

  # Ask the user for input again
  input_str = input("Enter a number (or 'done' to stop): ")

# Print the total once the loop has finished
print("The total is:", total)