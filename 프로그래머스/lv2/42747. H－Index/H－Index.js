function solution(citations) {
    let answer = 0
    // 내림차순
    citations.sort((a,b) => b-a)
    // 자신의 인용횟수가 자신보다 인용횟수가 많은 논문 수 보다 많으면 정답 + 1 
    for(let i=0; i<citations.length; i++) {
        if(i < citations[i]) answer++
    }
    return answer
}