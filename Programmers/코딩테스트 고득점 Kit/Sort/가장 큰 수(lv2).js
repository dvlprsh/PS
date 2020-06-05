// 풀이 참고
function solution(numbers) {
    var answer = '';
    
    answer=numbers.map(v => v+'').sort(function (a, b){
        return `${b}${a}` - `${a}${b}`
    }).join('')
 
    return answer[0] === '0' ? '0': answer
}