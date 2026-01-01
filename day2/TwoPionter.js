let arr = [2, 1, 4, 5];

function reverseInPlace(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        // Swap values
        let temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        // Move pointers
        left++;
        right--;
    }
    console.log("Reversed Array:", arr);
}

reverseInPlace(arr);