function solution(heights) {
    var stack=[];
    var answer = [];
    for(var height of heights){
        stack.push(height);
        answer.push(0);
    }

    for(var i=stack.length-1; i>=0; i--){
        const height=stack.pop();
        for(var j=stack.length-1; j>=0; j--){
            if (stack[j] > height){
                answer[i]=j+1;
                break;
            }
        }
    }
    return answer;
}