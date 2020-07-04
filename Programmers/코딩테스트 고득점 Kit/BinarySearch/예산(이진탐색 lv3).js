//2020.05--------------------------------------
function get_total(budgets, high){
    var total=0;
    for (var budget of budgets){
        budget=parseInt(budget);
        if(budget > high) {
            total += high;
        }else{
            total += budget;
        }
    }
    return total;
}

function solution(budgets, M) {
    var answer = 0;
    budgets.sort(function(a, b){
        return a-b;
    })
    var low= parseInt( M / budgets.length )
    var high = budgets[budgets.length -1]

    while (low <= high){
        var mid = parseInt((low+high)/2);
        var total=get_total(budgets, mid);
        if (total > M) {
            high = mid-1;
        }else if (total < M){
            low = mid +1;
        }else{
            answer = mid;
        }
    }

    answer = high;
    return answer;
}