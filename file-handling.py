# Open a file in read mode
#file = open("example.text", 'r')

# Read the content of the file 
#content = file.read()

# Print the content
#print(content)

# Close the file to release any system resourse associated with it
#file.close()


# Open a file in write mode
file = open("example.text", 'w')

# Read the content of the file 
content = file.write("Hello World")

# Print the content
print(content)

# Close the file to release any system resourse associated with it
file.close()


# Open a file in write mode
file = open("example.text", 'r')

# Read the content of the file 
lines = file.readlines()

# Print the content
for line in lines:
    print(line.strip())

# Close the file to release any system resourse associated with it
file.close()


# Open a file in write mode
file = open("example.text", 'w')

# Read the content of the file 
content = file.write("Hello World! \n")

# Print the content
print(content)

# Close the file to release any system resourse associated with it
file.close()


with open("example.text", 'r') as file:
    file.write("Another line")