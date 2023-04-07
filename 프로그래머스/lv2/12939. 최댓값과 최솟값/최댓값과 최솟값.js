function solution(s) {
   const arr = s.split(' ')
   let numArr = arr.map(e=> Number(e)).sort((a,b)=> a-b);
    return `${String(numArr[0])} ${String(numArr[arr.length-1])}`
}