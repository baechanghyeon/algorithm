function solution(arr) {
    let hap = 0
    arr.forEach((i) => {
        hap += i
    })
    return hap / arr.length
}