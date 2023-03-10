// lottos = 구매한 로또 번호를 담은 배열 
// win_nums = 당첨 번호

function solution(lottos, win_nums) {
    // #1 알아볼 수 없는 번호가 몇개 인지 찾기(0으로 표시 -> undefined_num)
    const undefined_num = lottos.filter((i) => i===0).length
    // 최고점수 = 알아볼수 없는 번호 전부가 당첨번호인 경우
    // 최저점수 = 알아볼수 없는 번호가 전부 당첨번호가 아닌 경우
    // #2 최고점수에서 맞는 번호의 갯수 구하기 
    let match = 0
    lottos.forEach((i) => {
        win_nums.map((j) => {
            if(i === j) match++
        })
    })
    const score = [6,5,4,3,2,1,0]
    let best = match + undefined_num
    let wost = match

    const result = []
    //#3 맞은 갯수에 따라 순위 정해주기
    if(best === 0) {
        result.push(6)
    }else {
    result.push(score.indexOf(best) + 1);
    }
    if(score.indexOf(match) === 5) {
        result.push(6)
    }else if( score.indexOf(match) === 6) {
        result.push(6)   
    }else {
        result.push(score.indexOf(match)+1)
    }
    return result    
    
}