function solution(num_list) {
    let k = 0
    let j = 0
    num_list.forEach((i) => {
        if(i%2 === 0) k++
        else j++
    })
    return [k, j]
}