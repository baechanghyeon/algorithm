// k 번째이내이면 명예전당 등극
// 시작 초기 ~ k일까지 점수로 계산 
// 매일 명예전당 최하위 점수 발표
// return 매일 발표된 명예전당의 최하위 점수를 반환

function solution(k, score) {
    // 매일 한명씩 추가해서 순위를 매긴다.
    const member = []
    const answer = []
    score.forEach((i, idx) => {
        // 매일 k순위 안에 최하위를 배열에 넣는다.
        member.push(i)
        member.sort((a,b) => b-a)
        if(member.length > k) answer.push(member[k-1])
        else answer.push(Math.min(...member))
    })
    return answer
}