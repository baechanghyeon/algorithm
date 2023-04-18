// 앞선 프로젝트가 완료되야 이후에 프로젝트도 완성이 됨.
function solution(progresses, speeds) {
    const result = []
    for(let i=0; i< progresses.length; i++) {
        let day = 0
        // 각 배포날짜 구하기
        while(progresses[i] < 100) {
            progresses[i] += speeds[i]
            day++
        }
        result.push(day)
    }
    const answer = []
    let work = result[0]
    let cnt = 1
    for(let i=1; i<result.length; i++) {
        if(work >= result[i]) cnt++;
        else if(work < result[i]){
            work = result[i]
            answer.push(cnt)
            cnt = 1
        }      
    }
    answer.push(cnt)
    return answer
}
    
 
