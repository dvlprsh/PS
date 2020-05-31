function solution(clothes) {
    let answer = 1;
    const map = new Map();
    for (let cloth of clothes){
        const kind=cloth[1]
        const count=map.get(kind)
        if(count){
            map.set(kind, count + 1);
        }else{
            map.set(kind, 1);
        }
    }

    for (let value of map.values()){
        answer *= (value + 1);
    }
    return answer-1;
}