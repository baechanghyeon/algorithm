function solution(a, b) {
    const week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    const leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let day = b+4
    for(let i=0; i<a-1; i++) {
        day += leap[i]
    }
    return week[day%7]
}