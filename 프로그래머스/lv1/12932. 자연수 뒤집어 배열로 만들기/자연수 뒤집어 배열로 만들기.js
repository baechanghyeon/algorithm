function solution(n) {
    let answer = []
    let arr = String(n).split('')
    for(let i = arr.length-1; i >=0; i--) {
        answer.push(Number(arr[i]))
    }
    return answer
}