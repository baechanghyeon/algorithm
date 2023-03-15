// 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려고 함.
// 공격력의 제한 수치를 정함. 
// 기관에서 정한 공격력을 가진 무기를 구매해야 함.
// 무기의 공격력 1당 1kg 철이 필요 
// number = 기사 단원의 수 
// limit = 제한 수치
// power = 제한수치를 초과할 경우의 무기 
// return = 무기를 만들기 위한 철의 무게를 return  
function solution(number, limit, power) {
    // #1. 각 기산단원의 약수의 개수를 구해야함 = 무기 공격력
    const numPw = []
    const result = []
    for(let i = 1; i <= number; i++) {
        let cnt = 0
        // 제곱근을 이용한 약수 구하기
        for(let j =1 ; j <= Math.sqrt(i); j++) {
            if(i%j === 0) {
                cnt++
                if(i/j !== j) cnt++;
            }
            
        }  
        numPw.push(cnt)
    }
    // #2. 무기 공격력이 제한 수치를 초과한 경우 정해진 power 를 써야함.
    numPw.forEach((i) => {
        if(i > limit) result.push(power)
        else result.push(i)
    })
    
    // #3. 무기 공격력을 반환 ( 무기 공격력 1당 1kg )
    return result.reduce((a,b) => a += b)
}