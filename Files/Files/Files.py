file_name = "output.txt"

file = open(file_name, "w")

for i in range(100):
    file.write(f"{i} Hello, World!\n")

file.close()