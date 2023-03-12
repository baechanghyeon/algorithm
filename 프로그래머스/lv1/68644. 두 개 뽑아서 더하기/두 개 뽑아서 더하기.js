function solution(numbers) {
    const answer = []
    // #1 각 다른 인덱스 더하기
    // [0 + 1], [0 + 2], [0 + 3], [0 + 4], [1 + 2],[1 + 3],[1 + 4] [2 + 3,], [2+4] [3+4], 
    for(let i =0; i< numbers.length - 1; i++) {
        for(let j = 1 + i; j<numbers.length; j++) {
            if(!answer.includes(numbers[i] + numbers[j])) {
                answer.push(numbers[i] + numbers[j])
            }
        }
    }
    return answer.sort((a,b) => a-b)
}

