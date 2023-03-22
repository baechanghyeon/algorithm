function solution(n){
    let hap = 0
    let num = String(n)
    let format = num.split('')
    
    for(let i =0; i<format.length; i++) {
        hap+= Number(format[i])
    }
    return hap
} 