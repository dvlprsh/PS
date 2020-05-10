function solution(d, budget) {
    var answer = 0;

    d.sort(function(a, b){
        return a-b;
    })

    d.map ((v, i)=> {
        if(budget >= v){
            budget -= v;
            answer += 1;
        }
    })
    return answer;
}