//Solve
def solution(genres, plays):
    answer = []
    records = {}
    for i in range(len(plays)):
        if genres[i] in records:
            records[genres[i]]["play"] += plays[i]
        else:
            records[genres[i]]={}
            records[genres[i]]["song"] = {}
            records[genres[i]]["play"] = plays[i]
        records[genres[i]]["song"][i]=plays[i]

    data = sorted(list(records.values()), key= lambda x: -x['play'])
    for value in data:
        song = value['song']
        sorted_song = sorted(song.items(), reverse=True, key= lambda x: x[1])

        if(len(sorted_song) >= 2):
            answer.extend([sorted_song[0][0], sorted_song[1][0]])
        else:
            answer.append(sorted_song[0][0])

    return answer