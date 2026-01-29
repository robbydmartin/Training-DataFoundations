arr_numbers = input()

arr = arr_numbers.split(" ")
lst = []
for number in arr:
    lst.append(int(number))

lst.sort()

longest_sequence = 1
current_sequence = 1
current_pointer = lst[0]

for number in range(1, len(lst)):
    if lst[number] == current_pointer + 1:
        current_sequence += 1
        current_pointer = lst[number]
        if current_sequence > longest_sequence:
                longest_sequence = current_sequence
    else:
        current_sequence = 0
        current_pointer = lst[number]


print(longest_sequence)