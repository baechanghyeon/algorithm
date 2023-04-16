function solution(k, dungeons) {
    // const result = []
    // const dfs = (tired, duns, answer) => {
    //     result.push(answer)
    //     for(let i =0; i<duns.length; i++) {
    //         const [a,b] = duns[i]
    //         if(tired < a) continue;
    //         else {
    //             dfs(tired-b, duns ,answer++)
    //         }
    //     }
    // }
    // dfs(k, dungeons, 0)
    let answer = []
    let visited = Array(dungeons.length).fill(false)
    
    const dfs = (cnt, k) => {
        answer.push(cnt)
        
        for(let i =0; i<dungeons.length; i++) {
            let cur = dungeons[i]
            if(k >= cur[0] && !visited[i]){
                visited[i] = true
                dfs(cnt + 1, k - cur[1])
                visited[i] = false
            }
        }
    }
    dfs(0, k)
    console.log(visited)
    console.log(answer)
    return Math.max(...answer)
}