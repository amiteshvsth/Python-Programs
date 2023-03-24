# Open a file for reading
f = open("test.txt", "r")

# Read the first line of the file
line1 = f.readline()
print("First line of the file:", line1)

# Read all lines of the file into a list
lines = f.readlines()
print("All lines of the file:", lines)

# Close the file
f.close()

# Open a file for writing
f = open("output.txt", "w")

# Write multiple lines to the file using writelines()
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
f.writelines(lines_to_write)

# Write a single line to the file using writeline()
line_to_write = "Line 4\n"
f.writelines(line_to_write)

# Close the file
f.close()
