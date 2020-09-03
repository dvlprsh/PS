function get_right_idx(n, weak, idx){
  if (idx + 1 >= weak.length) return 0;
  else return idx + 1;
}
function get_left_idx(n, weak, idx){
  if (idx - 1 < 0) return weak.length-1;
  else return idx - 1;
}
function get_right_dist(n, start, end){
  if (start < end) return end - start;
  else return (n - start) + end;
}
function get_left_dist(n, start, end){
  if (start > end) return start - end;
  else return (n - end) + start;
}
function get_max_points(n, weak, dist){
  let max_weaks = [];
  weak.forEach((v, i) => {
      let next_idx = i;
      const available_weak = [v];
      do {
          next_idx = get_right_idx(n, weak, next_idx);
          if (get_right_dist(n, i, next_idx) <= dist) {
              available_weak.push(weak[next_idx]);
          }else {
              break;
          }
      } while (next_idx !== i);
      if (available_weak.length > max_weaks.length) max_weaks = available_weak;
      
      next_idx = i;
      const available_weak2 = [v];
      do {
          next_idx = get_left_idx(n, weak, next_idx);
          console.log('next_idx',next_idx, i)
          if (get_left_dist(n, i, next_idx) <= dist) {
              available_weak2.push(weak[next_idx]);
          }else {
              console.log('break')
              break;
          }
      } while (next_idx !== i);
      if (available_weak2.length > max_weaks.length) max_weaks = available_weak2;
  });
  return max_weaks;
}
function solution(n, weak, dist) {
  var answer = 0;
  dist.sort((a, b)=> b - a);
  for (let i = 0; i < dist.length; i++) {
      console.log('weak', weak)
      const max_weak_points = get_max_points(n, weak, dist[i]);
      weak = weak.filter(v => !max_weak_points.includes(v));
      console.log(max_weak_points, weak)
      if (weak.length === 0) return i+1;
  }
 
  return -1;
}