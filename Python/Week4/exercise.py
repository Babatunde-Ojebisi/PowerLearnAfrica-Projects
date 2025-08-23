# Create a file called input.txt and write at least five lines of text into it.
# Write a Python script to:
# Read the contents of input.txt.
# Count the number of words in the file.
# Convert all text to uppercase.
# Write the processed text and the word count to a new file called output.txt.
# Print a success message once the new file is created.

file = open("input.txt", "w")
file.write("Welcome to my world\n")

file = open("input.txt", "a")
file.write("You can learn programming\n")
file.write("Let's start with Python\n")

file = open("input.txt", "r")
source = file.read()
caps = source.upper()
length = f"{len(source)}"

new_file = open("output.txt", "w")
new_file.write(caps)

new_file = open("output.txt", "a")
new_file.write(length)