function solution(s) {
    // 문자열을 공백 기준으로 배열로 만들기
    const arr = s.split("")
    let word = []
    let stack = 0
    arr.forEach((i) => {
       for(let j =0; j<i.length; j++) {
           if(stack%2 === 0) {
               word.push(i[j].toUpperCase())
               stack++
           }
           else if(stack%2 === 1) {
               word.push(i[j].toLowerCase())
               stack++
           }
           
           if(i[j] === ' ') stack = 0
       }
    })
    return word.join("")
}