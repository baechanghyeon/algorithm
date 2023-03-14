function solution(s, n) {
    let answer = ""
    for(let i = 0 ; i < s.length; i ++)
    {
        let p = s.charCodeAt(i)
        
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



