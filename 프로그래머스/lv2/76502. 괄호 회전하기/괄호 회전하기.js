// 문자열을 한칸씩 왼쪽으로 돌리기
// 주어진 괄호 문자열이 올바른 괄호인지 확인

const pair = { '}': '{', ']': '[', ')': '(' }

const isValid = (arr) => {
    const stack = []
    for (let i = 0; i < arr.length; i++) {
      const c = arr[i]
      if (pair[c] === undefined) stack.push(c)
      else {
        if (stack[stack.length - 1] !== pair[c]) return false
        stack.pop()
      }
    }
    if (stack.length) return false
    return true
  }

function solution(s) {
  const arr = s.split('')
  let result = 0

  for (let i = 0; i < s.length; i++) {
    if (isValid(arr)) result++
    arr.push(arr.shift())
  }

  return result
}