// 0 -> 공백, 1 -> #

function solution(n, arr1, arr2) {
    const result = []
    let arr1For = arr1.map((i) => i.toString(2).padStart(n, '0'))
    let arr2For = arr2.map((i) => i.toString(2).padStart(n, '0'))
    for(let i=0; i < n; i++) {
        let str = ''
        for(let j=0; j < n; j++) {
        if(arr1For[i][j] === '1' || arr2For[i][j] === '1') str += '#'
        else if(arr1For[i][j] === '0' || arr2For[i][j] ==='0') str += ' '
        }
        result.push(str)
    }
    return result
}