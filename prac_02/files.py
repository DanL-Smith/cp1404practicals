# # 1. Files Program 1
# name = input("Enter name: ")
# out_file = open("name.txt", 'w')
# out_file.write(name)
# out_file.close()

# # Files Program 2
# in_file = open("name.txt", 'r')
# name = in_file.read().strip()
# in_file.close()
# print(f"Your name is {name}")

# # 3. Files Program 3
# in_file = open("Numbers.txt", "r")
# numbers = []
# for i in range(2):
#     numbers.append(int(in_file.readline()))
# in_file.close()
# print(sum(numbers))

# Files Program 4
# total = 0
# in_file = open("Numbers.txt", "r")
# for line in in_file:
#     number = int(line)
#     total += number
# in_file.close()
# print(total)