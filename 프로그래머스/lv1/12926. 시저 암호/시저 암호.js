function solution(s, n) {
    let answer = ""
    for(let i = 0 ; i < s.length; i ++)
    {
        let p = s.charCodeAt(i)
        if(p === 32) answer += ""
        
        if(64 < p && p < 91) {
            p += n
            if(90 < p) p -=  26    
        }
        
        else if(96 < p && p < 123) {
            p += n
            if(122 < p) p -= 26
        }
        
        answer += String.fromCharCode(p)
    }
    return answer
}

const test = solution("AB", 1);
console.log(test)
// solution("z", 1);
// solution("Z", 10);
// solution("a B z", 4);
// solution(" aBZ", 20);
// solution("y X Z", 4);
// solution(" . h z", 20);


