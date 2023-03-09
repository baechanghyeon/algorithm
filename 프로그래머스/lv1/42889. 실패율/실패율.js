// 전체 스테이지의 개수 N 
// 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
// 실패율 = 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
const cntArr = []
const failArr = []
function solution(N, stages) {
    //#1 각 자릿수 마다 중복된 값 카운트
    for(let i =1 ; i <= N; i++) 
    {
        const cnt = stages.filter((j) =>  i === j)
        cntArr.push(cnt.length);
    }
    //#2 1 ~ 5 까지 실패율 구하기
    let leng = stages.length
    for(let k = 0; k < N; k++) {
         if(k === 0) failArr.push([k, cntArr[k] / leng])
         else {
              leng -= cntArr[k-1]
              failArr.push([k, cntArr[k] / leng] )
         }
    }
    //#3 내림차순으로 정렬
    const result = failArr.sort((a, b) => b[1]-a[1])
    const r = result.map((i) => i[0] + 1)
    return r
}