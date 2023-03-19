// 장르별 가장 많이 재생된 노래 두개씩 모아 베스트 앨범 출시
// genres = 노래 장르
// plays = 노래가 재생된 횟수
function solution(genres, plays) {
    // 장르별 재생된 횟수
    const list = {}
    genres.forEach((i, idx) => {
        if(!list[i]) list[i] = plays[idx]
        else list[i] += plays[idx]
    })
    const arr = []
    for(let [key, value] of Object.entries(list)) {
        arr.push([key, value])
    }
    
    // 많이 재생된 순서로 정렬
    arr.sort((a,b) => b[1]-a[1])
    let answer = []
    for(let i of arr) {
        const style = []
        for(let j =0; j< genres.length; j++) {
            if(i[0] === genres[j]) style.push([j, plays[j]]) 
            style.sort((a,b) => b[1]-a[1])
            if(style.length>2) style.pop()
        }          
        answer = answer.concat(style)
    }
    const result = []
    for(let i of answer) result.push(i[0])
    return result
    
}