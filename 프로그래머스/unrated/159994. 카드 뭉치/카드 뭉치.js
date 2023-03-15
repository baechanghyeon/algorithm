// 두 카드는 서로 다른 문자들로만 구성
// 한번 사용한 카드 다시 사용 X
function solution(cards1, cards2, goal) {
    let result = ''
    goal.forEach((i) => {
        if(cards1.includes(i)){
            if(cards1[0] === i) {
                cards1 = cards1.filter((x) => x!==i)
                goal = goal.filter((y) => y !== i)
            } else {
                result = "No"
            }
        } else {
            if(cards2[0] === i) {
                cards2 = cards2.filter((x) => x !== i);
                goal = goal.filter((y) => y !== i)
            } else {
                result = "No"
            }
        } 
    })
    if(goal.length === 0 )result = "Yes"
    return result;
}