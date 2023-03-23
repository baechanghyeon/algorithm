function solution(s){
  let answer = []

    for(let i of s) {
       answer.push(i)
       if(answer[answer.length-1] === answer[answer.length-2]){
           answer.pop()
           answer.pop()
       }
    }
    if(answer.length === 0) return 1
    else return 0
}