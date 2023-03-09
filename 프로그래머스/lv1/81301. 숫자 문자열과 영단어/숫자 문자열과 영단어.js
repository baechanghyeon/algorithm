const k = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

function solution(s) {
    k.forEach((i, idx) => {
        s = s.replaceAll(i, idx)
    })
    return parseInt(s)
}