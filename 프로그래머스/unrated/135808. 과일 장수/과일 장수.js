// k = 사과 최대 점수
// score = 사과들의 점수 
// return = 과일장수가 얻을 수 있는 최대 이익
function solution(k, m, score) {
    // 사과 점수가 큰 순으로 정렬 시킨다. 
    const arrSort = score.sort((a,b) => b-a)
    let apple = m
    let cut = []
    // 상자에 들어가는 크기별로 자른다. 
    for(let i = 0; i< arrSort.length; i++){
        if(apple <= arrSort.length) {
            cut.push(arrSort.slice(i*m, apple))
            apple += m
        }
    }
    // 사과 박스의 가격
    // m = 상자에 담는 사과의 갯수
    // p = 상자에 담긴 사과 중 가장 낮은 점수 
    // 사과 한 상자의 가격은 p * m 
    let result = 0
    for(let i of cut) {
        let min = Math.min(...i)
        result += min * m
    }
    return result
}