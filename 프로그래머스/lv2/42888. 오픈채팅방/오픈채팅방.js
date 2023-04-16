function solution(record) {
  let obj = {}
  for(let i of record) {
      let [state, id, nick] = i.split(' ')
      if(nick) obj[id] = nick
  }
    
  let answer = []
  for(let j of record) {
      let [state, id, nick] = j.split(' ')
      switch(state) {
          case 'Enter' :
              answer.push(`${obj[id]}님이 들어왔습니다.`)
              break;
          case 'Leave' :
              answer.push(`${obj[id]}님이 나갔습니다.`)
              break;
      }
  }
  return answer
}