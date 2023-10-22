import time

unordered_list = [7,10,4,2,8,6]

# Custom bubble sorting algorithm
start_time = time.time()
swapped = True
while swapped:
    swapped = False
    for i in range(len(unordered_list)-1):
        if unordered_list[i] > unordered_list[i + 1]:
            swapped = True
            unordered_list[i], unordered_list[i + 1] = unordered_list[i + 1], unordered_list[i]
end_time = time.time()
custom_sort_time = end_time - start_time

print(f"Time taken by custom sort: {custom_sort_time} seconds")

# Built-in sort method
unordered_list = [7,10,4,2,8,6]
start_time = time.time()
unordered_list.sort()
end_time = time.time()
builtin_sort_time = end_time - start_time

print(f"Time taken by built-in sort: {builtin_sort_time} seconds")


my_lists = [i * 2 ** 12 / i for i in range(1, 13)]

largest_num = my_lists[0]

for num in my_lists[1:]:
	if num > largest_num:
		largest_num = num

print(largest_num)
