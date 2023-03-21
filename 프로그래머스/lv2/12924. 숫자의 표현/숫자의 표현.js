function solution(n) {
    let cnt = 0
    let hap = 0
    let start = 1
    while(n >= start) {
        let hap = 0
        for(let i = start; i <= n; i++){
            hap += i
            if(hap === n) {
                cnt++;
                break
            } else if(hap > n) break
        }
        start++
    }
    return cnt
}
