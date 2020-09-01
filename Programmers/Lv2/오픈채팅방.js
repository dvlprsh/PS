//0901 Solve
function solution(record) {
  const answer = [];
  const id_nickname_map = new Map();
  record = record.map(v => v.split(' '));
  record.forEach(token => {
      token[0] !== 'Leave' && id_nickname_map.set(token[1], token[2]);
  });
  record.forEach(token => {
      switch(token[0]){
          case 'Enter':
              answer.push(`${id_nickname_map.get(token[1])}님이 들어왔습니다.`);
              break;
          case 'Leave':
              answer.push(`${id_nickname_map.get(token[1])}님이 나갔습니다.`);
              break;
      }
  });
  return answer;
}