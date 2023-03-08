const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')
let flag = true
function solution(s) {
    const arr = s.split('')
    arr.forEach((i) => {
        alphabet.forEach((j) => {
            if(j.includes(i)){
                flag = false
            };
        })  
    })
    if(s.length !== 6 && s.length !== 4) flag = false
    return flag
}