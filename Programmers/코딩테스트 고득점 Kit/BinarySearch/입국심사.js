//0916 Solve
function solution(n, times) {
    let start = 0;
    let end = Math.max(...times) * n;
    while(start <= end){
        const mid = parseInt((start + end) / 2);
        const people = times.reduce((a, v) => a + parseInt(mid / v), 0);
        people >= n ? end = mid - 1 : start = mid + 1;
    }
    return start;
}
