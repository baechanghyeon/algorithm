function solution(arr) {
    arr.sort((a,b)=> b-a)
    let num = arr[0]
    for(let i=1; i<arr.length; i++) {
        num = lcm(arr[i], num)
    }
    return num
}

// 최대 공약수
function gcd(a,b) {
    if(a%b === 0) return b
    return gcd(b, a%b)
}

// 최소 공배수
function lcm(a,b) {
    return a*b/gcd(a,b)
}


 
 