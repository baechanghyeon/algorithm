function solution(arr) {
    let test = arr.filter((i) => Math.min(...arr) !== i) 
    if(arr.length<=1) return [-1]
    return test
}