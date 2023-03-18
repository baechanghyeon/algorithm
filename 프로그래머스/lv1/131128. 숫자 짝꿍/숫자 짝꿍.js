function solution(X, Y) {
    // 숫자 0 ~ 9
    const x = [0,0,0,0,0,0,0,0,0,0]
    const y = [0,0,0,0,0,0,0,0,0,0]
    X.split('').map((i) => x[i]++)
    Y.split('').map((i) => y[i]++)
    const answer =[]
    
    for(let i =0; i< x.length; i++) {
        let min = Math.min(x[i], y[i])
        for(let j =0; j < min; j++) answer.push(i)
    }
    answer.sort((a,b) => b-a)
    if(answer[0] === 0) return '0'
    if(answer.length === 0) answer.push(-1)
    return answer.join('')
}