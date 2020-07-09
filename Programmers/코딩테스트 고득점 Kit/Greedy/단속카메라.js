//0709 Solve
function solution(routes) {
    let answer = 0;
    let last_point = -30000;
    routes.sort((a, b) => a[1] - b[1]);
    routes.forEach(v => {
        if (v[0] > last_point) {
            last_point = v[1];
            answer++;
        }
    });
    return answer;
}