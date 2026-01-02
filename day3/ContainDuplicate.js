let arr = [1, 2, 3, 4, 1, 5, 2];

function hasDuplicate(nums) {
    let mySet = new Set();
    
    for (let num of nums) {
        if (mySet.has(num)) {
            return true; // Jaise hi pehla duplicate mila, true return kardo
        }
        mySet.add(num);
    }
    return false; // Poora loop khatam hone par bhi kuch nahi mila
}

console.log(hasDuplicate(arr)); // Output: true