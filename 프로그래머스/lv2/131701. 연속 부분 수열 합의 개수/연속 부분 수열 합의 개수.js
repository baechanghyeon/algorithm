function solution(elements) {
    let len = elements.length
    let answer = []
    // 슬라이딩 윈도우 + set 객체 활용
    while(len > 0) {
        // 배열에 아무것도 없을 때 최초 1 실행
        if(elements.length === len) {
            answer.push(elements.reduce((a,c) => a+c))
            len--
            continue
        }
        let cnt = len
        
        for(let i=0; i < elements.length; i++) {
            let temp = 0
            for(let j=0; j< cnt; j++) {
                if(i+j < elements.length) temp+=elements[i+j]
                else temp+= elements[i+j-elements.length]
            } 
            answer.push(temp)
        }
        len--
    }
    return new Set(answer).size;
    
}