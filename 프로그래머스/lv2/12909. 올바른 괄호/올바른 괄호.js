function solution(s){
    let stack = 0
    for(let i of s) {
        if(i === '('){ 
            stack++ 
        } else stack --;
        if(stack < 0) return false
    }
    return stack === 0
}