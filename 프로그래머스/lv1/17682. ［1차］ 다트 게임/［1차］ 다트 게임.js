function solution(dartResult) {    
    const nums = ['1', '2', '3', '4', '5', '6', '7', '8','9','0']
    const points = dartResult.split('')
    const result= []
    const bonus = []
    const option= [1, 1, 1]
    const resultFor = []
    let answer = []
    points.forEach((i, idx) => {
        // 숫자 분리
        for(let j=0; j < nums.length; j++) {
           if(i === nums[j])
            {           
                if(i === '1') {
                    if(points[idx+1] === '0') result.push('10') 
                    else result.push('1')
                } else if(i === '0') {
                    if(points[idx-1] !== '1') result.push('0')
                }
                else {
                    result.push(i)
                }
            }  
        }
        // bonus (S, D, T)
        switch(i){
            case 'S': 
                bonus.push(1);
                break;
            case 'D':
                bonus.push(2);
                break;
            case 'T':
                bonus.push(3);
                break;
        }
        
        // option (*, #)
        switch(i) {
            case '*':
                if(idx <= 2) option[0] = 2
                else if(idx <= 5) option[1] = 2
                else if(idx > 5) option[2] = 2
                break;
            case '#':
                if(idx <=2) option[0] = -1
                else if(idx <= 5) option[1] = -1
                else if(idx > 5) option[2] = -1
                break;
        }
        
    })
    
    for(let i =0; i<result.length; i++) {
        resultFor.push(Number(result[i]))
    }
    
    option.forEach((i,idx) => {
        if(i === 2) {
            if(idx === 0) {
                answer[idx] = (resultFor[idx]**bonus[idx]) * 2
            } else {
                answer[idx] = (resultFor[idx]**bonus[idx] )* 2
                answer[idx-1] = (answer[idx-1] * 2)
            }
        } 
        else if(i === -1) {
            answer[idx] = (resultFor[idx]**bonus[idx])*(-1)
        }
        else {
            answer[idx] = resultFor[idx]**bonus[idx]
        }
    })
    
    return answer.reduce((a,b) => a+b)


}


    