// priorities = 중요도
// location = 인쇄를 요청한 문서가 어떤 위치인지 
// 내가 요청한 문서가 몇번째로 인쇄되는지 return
function solution(priorities, location) {
    // 객체로 key-value 설정
   let answer = 0
   const arr = []
   
   priorities.forEach((i, idx) => {
       arr.push({'num' : i, 'item' : idx === location})
   })

   while(arr[0]) {
       let compareItem = arr.shift()
       if(arr.some(res => res['num'] > compareItem['num'])) {
           arr.push(compareItem)
       } else {
           answer += 1
           if(compareItem['item']) break
       }
   }
    return answer
}