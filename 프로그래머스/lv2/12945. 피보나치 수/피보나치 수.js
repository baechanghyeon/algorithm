function solution(n) {
    let test = []
    test[0] = 0
    test[1] = 1
    let m = 1234567
    for(let i=2; i<=n; i++) {
        test[i] = (test[i-2] % m + test[i-1] % m)
    }
    return test[n] %m
}