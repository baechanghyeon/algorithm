// N 마리 중 N/2 가져가도 된다. 
// [3번, 1번, 2번, 3번] -> 3번 2마리, 1번 1마리, 2번 1마리 4C2(순열) 종류는 최댓값이 2  
// nums => 폰켓몬의 종류 번호가 담겨 있음

const arr = [];
let result 
function solution(nums) {
    nums.forEach((i) => {
        if(!arr.includes(i)) arr.push(i)
    })
    if(arr.length > nums.length / 2) return nums.length / 2
    else {
        return arr.length   
    }
}