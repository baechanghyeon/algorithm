function solution(sizes) {
    const a = []
    const b = []
    sizes.forEach((i) => {
        i.sort((a,b) => a-b)
        a.push(i[0])
        b.push(i[1])
    })    
    return Math.max(...a) * Math.max(...b)
}