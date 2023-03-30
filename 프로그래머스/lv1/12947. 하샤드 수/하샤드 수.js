function solution(x) {
    let a = String(x).split('')
    let sum = 0
    for(let i of a){
        sum += Number(i)
    }
    if(x%sum === 0) return true
    else return false
    
}