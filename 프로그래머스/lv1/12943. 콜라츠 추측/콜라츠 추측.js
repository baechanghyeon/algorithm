function solution(num) {
    if(num === 1) return 0
    for(let i =0; i< 501; i++){
        if(num%2 === 0) {
            num /= 2
        }
        else if(num%2 === 1) {
            num = (num*3) + 1
        }
        
        if(num === 1) return i+1
        if(i===500) return -1
    }
}