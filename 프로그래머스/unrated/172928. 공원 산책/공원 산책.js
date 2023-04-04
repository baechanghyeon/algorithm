function solution(park, routes) {
    let prevPos = [0, 0]

    const map = []
    park.forEach((row, idx) => {
        const sPos = row.indexOf('S')
        if(sPos >= 0) {
            prevPos = [idx, sPos]
        }
        map.push([...row])
    })
    const dict = {
        E: [0, 1],
        W: [0, -1],
        S: [1, 0],
        N: [-1, 0]
    }
    
    routes.forEach((route) => {
        const [pos, range] = route.split(" ")
        let curPos = [...prevPos]
        let flag = true
        // 거리만큼 반복
        for(let i = 0 ; i < range; i ++) {
            curPos[0]+= dict[pos][0]
            curPos[1]+= dict[pos][1]
            if(
                    (curPos[0] > map.length - 1) || 
                    (curPos[0] < 0) ||
                    (curPos[1] > map[0].length - 1) ||
                    (curPos[1] < 0)
    )
            {
                flag = false
                break
            }
            
            if(map[curPos[0]][curPos[1]] === 'X') {
                flag = false
                break
            }
            
        }
        // 거리 반영
        if(flag) prevPos = curPos
    })    
    return prevPos
}