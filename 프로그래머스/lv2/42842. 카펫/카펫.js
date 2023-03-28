function solution(brown, yellow) {
    // 12의 약수 = 1,2,3,4,6,12
    // 9의 약수 = 1,3,9
    // 48의 약수 = 1,2,3,4,6,8,12,16,24,48
    let total = brown + yellow
    let measure = []
    let result = []
    let a = 0
    let b = 1
    
    for(let i=1; i<=total; i++) {
        if(total%i === 0) measure.push(i)  
    }
    while(true){
        if(measure.length%2 === 0) {
            //(x-2)(y-2) == yellow
            if(((measure[measure.length/2+a]) - 2 ) *((measure[measure.length/2-b]) - 2 ) === yellow){
                result.push(measure[measure.length/2+a])
                result.push(measure[measure.length/2-b])
                break;
            }
            else {
                a++
                b++
            }
        }else {
            // measure.length%2 !== 0
            result.push(measure[Math.floor(measure.length/2)])  
            result.push(measure[Math.floor(measure.length/2)])
            break;
        }
    }
    
    
    return result
}

// 반례
// 72의 약수 = 1,2,3,4,6,8,9,12,18,24,36,72