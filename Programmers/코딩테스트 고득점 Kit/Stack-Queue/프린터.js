//0803 solve
function solution(priorities, location) {
  const priorities_set = priorities.map((v, i) => [v, i]);
  let order = 1;
  while(priorities_set.length > 0){
      const document = priorities_set.shift();
      const higher = priorities_set.find(v => v[0] > document[0]);
      if (higher) {
          priorities_set.push(document);
          continue;
      }else {
          if (document[1] === location) return order;
          else order ++;
      }
  }
}