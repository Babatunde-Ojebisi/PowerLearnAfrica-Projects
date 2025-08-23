#File Read & Write Challenge 🖋️: 
#Create a program that reads a file and writes a modified version to a new file.

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

#Error Handling Lab 🧪: 
#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("✅ File read successfully!")
        print("Content:\n", content)
except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")