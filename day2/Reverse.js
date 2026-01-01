let  arr=[2,1,4,5]
let dup=[]
function Reverse(arr,dup){
    for(let i=arr.length-1;i>=0;i--){
        dup.push(arr[i])
    }
    console.log(dup)
}
Reverse(arr,dup)