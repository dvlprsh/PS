//0710 Solve
function solution(s) {
    return s.split(' ').map(v=> v.charAt(0).toUpperCase() + v.toLowerCase().slice(1)).join(' ');
}