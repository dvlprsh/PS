// 0706 Solve
function solution(s)
{
    const stack = []
    s.split('').forEach(v => {if (stack[stack.length -1] !== v) stack.push(v); else stack.pop();})
    if (stack.length) return 0; else return 1;
}