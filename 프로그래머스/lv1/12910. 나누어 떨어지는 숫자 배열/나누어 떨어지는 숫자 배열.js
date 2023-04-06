function solution(arr, divisor) {
    let result = []
    arr.forEach((i) => {
        if(i%divisor === 0) result.push(i)
    })
    if(result.length === 0) result.push(-1)
    return result.sort((a,b) => a-b)
}