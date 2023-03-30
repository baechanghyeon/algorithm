function solution(seoul) {
    for(let i of seoul) {
        if(i==="Kim") return `김서방은 ${seoul.indexOf(i)}에 있다`
    }
}