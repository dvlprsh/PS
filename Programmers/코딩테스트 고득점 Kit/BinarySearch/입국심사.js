// 0704 Solve
function solution(n, times) {
  let left = 0;
  let right = Math.max.apply(null, times) * n;
  let mid = 0;
  while (left <= right) {
      let total_job = 0;
      mid = parseInt((left + right) / 2)
      const jobs = times.forEach((v)=> {
          total_job =total_job + parseInt(mid / v);
      })
     
      if (total_job < n) {
          left = mid + 1;
      }else {
          right = mid -1;
      }
  }
  return left;
}