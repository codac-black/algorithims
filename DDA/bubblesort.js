function bubbleSort(unorder_list) {
    let swapped = true;
    while (swapped) {
        swapped = false;
        for (let i = 0; i < unorder_list.length - 1; i++) {
            if (unorder_list[i] > unorder_list[i + 1]) {
                swapped = true;
                [unorder_list[i], unorder_list[i + 1]] = [unorder_list[i + 1], unorder_list[i]];
            }
        }
    }
    return unorder_list;
}

let unorder_list = [89, 4, 19, 2, 5, 3, 7, 11, 8, 10, 9, 6, 1, 12, 13, 14, 15, 16, 17, 18, 20];
console.log(bubbleSort(unorder_list));

