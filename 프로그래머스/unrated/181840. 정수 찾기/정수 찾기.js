function solution(num_list, n) {
    let answer = 0
    num_list.forEach((i) => {
       if(i === n) answer = 1
    })
    return answer
}