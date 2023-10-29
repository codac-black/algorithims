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
print(unordered_list)



