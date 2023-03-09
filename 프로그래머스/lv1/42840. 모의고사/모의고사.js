// answers 1번부터 마지막까지 정답이 든 answers 
// 1번은 1,2,3,4,5
// 2번은 2,1,2,3,2,4,2,5
// 3번은 3,3,1,1,2,2,4,4,5,5
function solution(answers) {
    const first = [1,2,3,4,5]
    const second = [2,1,2,3,2,4,2,5]
    const third = [3,3,1,1,2,2,4,4,5,5]
    
    let first_score = 0
    let second_score = 0
    let third_score = 0
    
    let first_j = 0;
    let second_j = 0;  
    let third_j = 0;  
    
    const result = [];
                    
    answers.forEach((i, idx) => {
    // #1
    // if(first_j === first.length - 1) first_j = 0
    // else if(first[first_j] === i) 
    // {
    //     first_score++
    //     first_j++
    // }
    // else first_j++
    // #2
    // if(second_j === second.length - 1) second_j = 0
    // else if(second[second_j] === i) 
    // {
    //     second_score++
    //     second_j++
    // }
    // else second_j++
    // #3        
    // if(third_j === third.length - 1) third_j = 0
    // else if(third[third_j] === i) 
    // {
    //     third_score++
    //     third_j++
    // }
    // else third_j++ 
    // }
    if(i === first[idx%first.length]) first_score++
    if(i === second[idx%second.length]) second_score++
    if(i === third[idx%third.length]) third_score++
    }
    )
    result.push(first_score)
    result.push(second_score)
    result.push(third_score)
    
    
    const k = []
    const max = Math.max(...result)

    result.forEach((i, idx) => 
    {
    if(i === max) k.push(idx + 1)
    }
    )
    console.log(k)
    return k
}