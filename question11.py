numbers = []

n = int(input("Enter how many numbers you want in the list: "))
for i in range(n):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

unique_set = set(numbers)
sorted_list = sorted(unique_set)

print("Sorted list without duplicates:", sorted_list)
