// 모두 더해서 target이 나오는 경우 => 경우의 수 1개
// 더한값이 마이너스 인 경우 => false
function solution(numbers, target) {
    let answer = 0
    function func(idx, hap) {
        if(idx===numbers.length) {
            if(hap === target) answer++
            return;
        }
        
        // 더하거나 빼는 쪽으로 빠져야함. 트리형태로 퍼져나감.
        func(idx+1, hap-numbers[idx])
        func(idx+1, hap+numbers[idx])
    }
    
    func(0, 0) // 0번째 숫자부터 시작하고, 시작값 합계 0을 파라미터로 전달
    return answer
}  