//Todo: Count the number of  interger in the number
let num = 4555;
let n = Math.abs(Math.floor(num));
let count = 0;

if (n === 0) count = 1;
while (n > 0) {
  n = Math.floor(n / 10);
  count += 1;
}
console.log(count); // 4