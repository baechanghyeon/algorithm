function solution(left, right) {
    const measure = (num) => {
        let result = []
        for(let i=1; i<=num; i++) {
            if(num%i === 0) result.push(i)
        }
        return result
    }
    let sum = 0
    for(let i=left; i<=right; i++) {
        if(measure(i).length%2 === 0) sum+=i
        else sum-=i
    }
    return sum
}