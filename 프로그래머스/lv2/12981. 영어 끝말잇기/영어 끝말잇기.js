function solution(n, words) {
    // 단어 끝자리 찾기
    let word = words[0].slice(-1)
    let answer = [words[0]]
    
    for(let i=1; i<words.length; i++) {
        // 이미 말한 단어를 말한 경우 && 일치하지 않는 경우
        if(answer.includes(words[i]) || word !== words[i].slice(0, 1)) {
            return [i%n+1, Math.ceil((i+1)/n)]
        }       
        
        // 현재 단어끝자리와 다음 단어 첫번째 자리가 일치하는 경우
        else if(word === words[i].slice(0, 1)){
            word = words[i].slice(-1)
            answer.push(words[i])
        }
        
    }
    return [0, 0]
}