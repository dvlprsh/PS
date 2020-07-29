//0730 Solve
function is_balanced(p) {
  const count_right = p.match(new RegExp(/[(]/g)).length
  const count_left = p.match(new RegExp(/[)]/g)).length
  if (count_right === count_left) return true;
  else return false;
}
function is_correct(p) {
  const stack = [];
  p.split('').forEach((v) => {
      if (stack[stack.length-1] === '(' && v === ')') stack.pop();
      else stack.push(v);
  });
  if (stack.length === 0) return true;
  else return false;
}
function solution(p) {
  if (p === '') return '';
  if (is_correct(p)) return p;
  
  let count_right = 0;
  let count_left =0;
  
  for(let i=0; i< p.length; i++){
      if (p[i] === '(') count_left++;
      else count_right++;
      if(count_left !==0 && count_left === count_right){
          break;
      }
  }
  
  const u = p.substring(0, count_left*2);
  const v = p.substring(count_left*2);

  if (is_correct(u)){
      return u + solution(v);
  } else {
      let new_string = '(';
      new_string += solution(v);
      new_string += ')';
      return new_string + u.substring(1, u.length-1).split('').map(v => v==='('? ')': '(').join('');
  }
}