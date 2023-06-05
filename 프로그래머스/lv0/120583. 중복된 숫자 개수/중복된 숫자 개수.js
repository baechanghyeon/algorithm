function solution(array, n) {
    let cnt = 0
    array.forEach((i) => {
        if( i === n) cnt++
    })
    return cnt
}