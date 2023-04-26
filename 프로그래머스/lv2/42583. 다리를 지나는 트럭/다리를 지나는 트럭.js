function solution(bridge_length, weight, truck_weights) {
  let que = [] // 큐를 활용하여 풀기
  let totalT = 0
  let weightS = 0
  // 대기 트럭이 있을시, 지나가고 있는 트럭이 없을 시
  while(truck_weights.length || que.length) {
      if (weightS + truck_weights[0] <= weight) {
      const tWeight = truck_weights.shift();
      que.push([tWeight, 0]);
      weightS += tWeight;
    } 
    // 트럭에 시간 추가
    que = que.map(([w, t]) => [w, t + 1]);
    totalT++;
    // 다리 끝에 도달할 시 제외
    if (que[0][1] === bridge_length) {
      weightS -= que.shift()[0];
    } 
  }
  return totalT + 1; 
}