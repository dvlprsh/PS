// 0705 Solve
function get_width(n, memo) {
    if (n in memo) return memo[n]; else memo[n] = get_width(n-1, memo) + get_width(n-2, memo);
    return memo[n];
}
function solution(N) {
    const memo = {1: 1, 2: 1};
    const width = get_width(N, memo);
    const height = get_width(N, memo) + get_width(N-1, memo);
    return 2 * width + 2 * height;
}