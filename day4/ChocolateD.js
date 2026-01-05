let arr = [2, 4, 15, 1, 3, 8];
let m = 3; 

function Choclate(arr, m) {
    let n = arr.length;
    
    // Step 1: Sort the array (Essential for finding min difference) 
    arr.sort((a, b) => a - b); 

    // Step 2: Initialize min with a very large number
    let minDiff = Infinity; 

    // Step 3: Loop through the array to find the window 
    for (let i = 0; i + m - 1 < n; i++) {
        let diff = arr[i + m - 1] - arr[i]; // Last - First element of window
        
        if (diff < minDiff) {
            minDiff = diff;
        }
    }

    return minDiff; // Loop khatam hone ke baad final answer return karo
}

console.log("Minimum Difference:", Choclate(arr, m));