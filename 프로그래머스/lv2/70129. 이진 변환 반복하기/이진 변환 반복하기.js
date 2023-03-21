function solution(s) {
    let answer = []
    let flag = true
    let cnt = 0
    let zero = 0
    let arr = s
    while(flag){
        cnt++;
        let arrFor = arr.split('').filter((i)=> i!=='0')
        zero += arr.length - arrFor.length
        arr = arrFor.length.toString(2);
        if(arrFor.length === 1) flag=false
    }
    answer.push(cnt)
    answer.push(zero)
    return answer
}