function solution(n) {
    const num = n.toString(3).split('').reverse().join('')
    const result = parseInt(num, 3)
    return result;
}