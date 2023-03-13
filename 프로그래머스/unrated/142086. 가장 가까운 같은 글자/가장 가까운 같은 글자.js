function solution(s) {
    const a = [];
    const answer = [];
        for(let i =0; i<s.length; i++) {
            // 안에 값이 없으면 -1
            if(!a.includes(s[i])) {
                a.push(s[i])
                answer.push(-1)

            } else {
            // 같은 값이 있으면
            // 같은 값의 위치 - 현재 값 위치 
                let cnt = 0
                for(let j = a.length-1; j >= 0; j--) {
                    // 중복 검사
                    if(a[j] === s[i] && cnt === 0) {
                        a.push(s[i])
                        answer.push(i-j) 
                        cnt++
                    }
                }
            }
        }
    return answer
}