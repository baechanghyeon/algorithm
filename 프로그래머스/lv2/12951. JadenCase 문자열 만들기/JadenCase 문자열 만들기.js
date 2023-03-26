function solution(s) {
    let arr = s.split(' ')
    let result = []
    arr.forEach((i) => {
        let answer = []
        for(let j=0; j<i.length; j++) {
            if(j === 0) typeof i[j] === 'string' ? answer.push(i[j].toUpperCase()) : answer.push(i[j])
            else answer.push(i[j].toLowerCase())
        }
        result.push(answer.join(''))
    })
    return result.join(' ')
    
}