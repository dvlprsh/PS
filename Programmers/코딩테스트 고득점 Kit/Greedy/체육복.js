// 0709 Solve
function solution(n, lost, reserve) {
    const _lost = lost.filter(x => !reserve.includes(x)).sort((a, b) => a - b)
    const _reserve = reserve.filter(x => !lost.includes(x)).sort((a, b) => a - b)
    let answer = n;
    _lost.forEach((v, i)=> {
        if (_reserve.includes(v-1)){
            _reserve.splice(_reserve.indexOf(v-1), 1);
        }else if (_reserve.includes(v+1)) {
            _reserve.splice(_reserve.indexOf(v+1), 1);
        }else{
            answer--;
        }
    });
    return answer;
}