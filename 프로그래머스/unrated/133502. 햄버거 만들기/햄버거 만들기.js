function solution(ingredient) {
    let cnt = 0
    for(let i = 0; i < ingredient.length-3; i++) {
        if(ingredient[i] === 1 && ingredient[i+1] === 2 && ingredient[i+2] === 3 && ingredient[i+3]===1){
            ingredient.splice(i,4)
            i -=4
            cnt++
        }
    }    
    console.log(ingredient)
    return cnt
    
    // # 2
    // let cnt = 0
    // let i = 0
    // while(i < ingredient.length-3) {
    //     if(ingredient[i] === 1 && ingredient[i+1] === 2 && ingredient[i+2] === 3 && ingredient[i+3]) {
    //         cnt++
    //         ingredient.splice(i,4)
    //         i=0
    //     } else {
    //         i++;
    //     }
    // }
    // return cnt
}