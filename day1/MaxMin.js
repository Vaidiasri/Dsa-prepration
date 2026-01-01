let arr = [12,3,4,16,2]

function MaxMin(arr){
  let max = arr[0]
  let min = arr[0]

  for(let i=1;i<arr.length;i++){
    if(arr[i] > max) max = arr[i]
    if(arr[i] < min) min = arr[i]
  }

  console.log("Max:", max)
  console.log("Min:", min)
}

MaxMin(arr)
