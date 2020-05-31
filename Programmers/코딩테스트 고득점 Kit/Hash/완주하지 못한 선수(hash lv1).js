function solution(participant, completion) {

    participant.sort()
    completion.sort()

    for (var i in completion){
        if(participant[i] !== completion[i]){
            return participant[i]
        }
    }
    return participant[participant.length -1]
}