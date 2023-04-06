function solution(n)
{
    let len = n
    let answer = 0
    while(len !== 0) {
        if(len%2 === 0) len /= 2
        if(len%2 === 1){
            len -= 1
            answer++
        }
    }
    return answer
}