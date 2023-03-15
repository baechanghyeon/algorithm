// participant = 마라톤에 참여한 선수들의 이름들
// completion = 완주한 참가자의 이름들
// return = 완주하지 못한 참가자의 이름 반환
// 참가자 중에 동명이인이 있을 수 있음
function solution(participant, completion) {
    let answer = {}
    participant.forEach((i) => {
        if(!answer[i]) answer[i] = 1
        answer[i]++
    })
    
    const result = completion.map((i) => answer[i]--)
    
    for(let i in answer) {
        if(answer[i]===2) return i
    }
    
//     completion[completion.length] =''
//     const x = participant.sort()
//     const y = completion.sort()
//     let result = ''
    
//     for(let i =0; i< x.length; i++) {
//         if(x[i] !== y[i]) result = x[i]
//     }
//     return result
    
}
    