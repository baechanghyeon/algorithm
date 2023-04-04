// 모두 더해서 target이 나오는 경우 => 경우의 수 1개
// 더한값이 마이너스 인 경우 => false
function solution(numbers, target) {
    let answer = 0
    for(let i=0; i<numbers.length; i++) {
        let arr = []
        for(let j=0; j<numbers.length; j++) {
            if(j===i) arr.push(-numbers[j])
            else arr.push(numbers[j])
        }
        console.log(arr)
    } 
}  