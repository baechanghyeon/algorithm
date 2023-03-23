function solution(n, lost, reserve) {
    lost.sort((a,b) => a-b)
    reserve.sort((a,b) => a-b)
    for(let i=0; i<lost.length; i++) {
        for(let j=0; j<reserve.length; j++) {
            if(lost.includes(reserve[j])) {
                lost.splice(lost.indexOf(reserve[j]),1)
                reserve.splice(j,1)
            }
            if(lost[i]-1 === reserve[j] || lost[i]+1 === reserve[j]) {
                lost.splice(i,1)
                reserve.splice(j,1)
                i-=1
            }
         
        }
        console.log(lost, reserve)
    }    
// 수업들을 수 있는 학생 = 전체학생 - lost 학생     
    return n - lost.length
}