function solution(array, commands) {
    const result = []
    commands.forEach((i) => {
      const a = array.slice(i[0]-1, i[1]).sort((a,b) => a-b)
      result.push(a[i[2]-1]) 
    })       
    return result
}