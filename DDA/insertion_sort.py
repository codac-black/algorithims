def insertion_sort(arr):
    for i in range(1, len(arr)):
        # key is the element to be inserted
        key = arr[i]
        # j is the index of the element to the left of key
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            # Move the element to the right
            arr[j + 1] = arr[j]
            # Decrement j
            j -= 1
        
        # Insert the key element at the correct position
        arr[j + 1] = key

    return arr



arr = [12,4,90,2,1,0,3]

print(insertion_sort(arr))
