function countOne(num) {
    let cnt = 0, ejin = num.toString(2).split('');
    for(let i = 0; i < ejin.length; i++) {
        if (ejin[i] == 1) { cnt++; }
    }
    return cnt; 
}

function solution(n) {
    let testNum = n;
    while(true) {
        testNum++; 
        if(countOne(testNum) == countOne(n)) return testNum;
    }
}