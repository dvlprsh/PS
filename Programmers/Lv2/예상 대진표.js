// 0705 Solve
// 풀이1 (풀이2 update)
function set_next_number(participant)
{
    if (participant % 2 === 0) return (participant / 2); else return (participant + 1) /2;
}
function solution(n,a,b)
{
    let count = 0;
    while (a !== b){
        count ++;
        a = set_next_number(a); // a = Math.ceil(a / 2)
        b = set_next_number(b); // b = Math.ceil(b / 2)
    }
    return count;
}
// 풀이 2
function set_next_number(participant)
{
    if (participant % 2 === 0) return (participant / 2); else return (participant+1) /2;
}
function is_meet(a, b){
    if (a % 2 === 0) a /= 2; else a = (a+1) /2;
    if (b % 2 === 0) b /= 2; else b = (b+1) /2;
    if (a === b) return true; else false;
}
function solution(n,a,b)
{
    let count = 1;
    while (!is_meet(a, b)){
        a = set_next_number(a);
        b = set_next_number(b);
        count ++;
    }
    return count;
}