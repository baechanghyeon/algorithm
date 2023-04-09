function solution(k, tangerine) {
    let orange = {}
    // 크기별 귤 갯수 파악
    tangerine.forEach((i) => {
        orange[i] = ++orange[i] || 1
    })
    // 귤 큰 순서대로 정렬
    let sortArr = Object.values(orange).sort((a, b) => b - a)
    // k 소거 및 응답값 구하기
    let answer = 0
    for(let j of sortArr) {
        answer++
        if(k > j) k-=j
        else break;
    }
    return answer
}