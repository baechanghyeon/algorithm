function solution(cacheSize, cities) {
    let time = 0
    let cache = []
    // 캐시 저장
    // 캐시 확인, 캐시 데이터 교체
    // 조건에 따른 실행시간
    for(let i =0; i<cities.length; i++) {
        let cur = cities[i].toLowerCase(); // 전부 소문자로 계산
        let find = cache.find((i) => i === cur)
        if(!find) {
            cache.push(cur)
            if(cache.length > cacheSize) cache.shift()
            time+=5
        }
        else {
            cache = cache.filter((i) => i !== cur)
            cache.push(cur)
            time++
        }
    }
    return time
}