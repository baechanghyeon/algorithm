function solution(t, p) {
    // p의 길이만큼 t 자르기
    const result = []
    let end = p.length
    for(let i=0; i<= t.length-p.length; i++)
    {  
        result.push(t.slice(i, end))
        end++
    }
    const answer = result.filter((i) => Number(i) <= Number(p))
    return answer.length
}