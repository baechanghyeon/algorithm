// strings = 문자열로 구성된 리스트
// n = 정수 
function solution(strings, n) {
    const a = []
    strings.forEach((i, idx) => {
        // 해당 index 알파벳 찾기
        a[idx] = [i[n], i]

    })
    // 정렬하기
    const result = a.sort((a,b) => {
        if (a > b) return 1;
        if (a < b) return -1;
    })
    // 값 도출
    const answer = []
    result.forEach((i, idx) => {
       answer.push(i[1])
    })
    return answer  
}