function solution(name, yearning, photo) {
    // 이름에 그리움 점수 객체로 할당
    const list = []
    name.forEach((i, idx) => {
        list.push({ 'name': i, 'year': yearning[idx]})
    })
    const answer = []
    for(let i of photo) {
        let sum = 0
        list.forEach((j) => {
          if(i.includes(j.name)) sum += j.year
        })
        answer.push(sum)
    }
    return answer
}