// 같은 종류를 선택 시 조합이 안됨 
// 같은 이름을 가진 의상은 존재하지 않습니다.
function solution(clothes) {
    let hash = {}
    let result = 1
    for(let i of clothes) {
        if(!hash[i[1]]) hash[i[1]] = 1
        else hash[i[1]]++
    }
    for(let [key, value] of Object.entries(hash)) {
        result *= (1 + value)
    }
    return result - 1
}