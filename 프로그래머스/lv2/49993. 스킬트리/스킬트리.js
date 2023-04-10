function solution(skill, skill_trees) {
    const tree = skill_trees
    let cnt = 0
    
    for(let i of tree) {
        const stack =[]
        // 스택
        for(let j=skill.length-1; j>=0; j--){
            stack.push(skill[j])
        }
        
        for(let k of i) {
            if(stack[stack.length-1] === k) stack.pop()   
        console.log('k',k)
        console.log('stack', stack)
        }
        if(stack.length === 0) cnt++
        console.log('cnt', cnt)
        console.log('----------------------')
    }
    return cnt
}