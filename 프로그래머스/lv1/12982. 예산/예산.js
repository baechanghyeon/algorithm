function solution(d, budget) {
   let answer = 0;
   let p = budget
   let sortArr = d.sort((a,b)=> a-b)
    
   for(let i =0; i<= d.length; i++) {
       p -= d[i]
       if(p < 0) break;
       if(p >= 0) {
            answer +=1    
       }
   }
   return answer
}