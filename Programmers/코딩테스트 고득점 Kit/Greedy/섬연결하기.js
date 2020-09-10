//0910 solve
function solution(n, costs) {
  let answer = 0;
  const linkedNode = new Set([]);
  const neighborNodes = Array.from({ length: n}, () => []);
  let candidates = [];

  costs.forEach(v => {
      const [n1, n2, cost] = v;
      neighborNodes[n1].push([n2, cost]);
      neighborNodes[n2].push([n1, cost]);
  });

  costs.sort((a, b) => a[2] - b[2]);
  const [n1, n2, cost] = costs.shift();
  linkedNode.add(n1);
  linkedNode.add(n2);
  candidates.push(...neighborNodes[n2]);
  candidates.push(...neighborNodes[n1]);
  answer += cost;

  while(linkedNode.size < n) {
      candidates = candidates
          .filter(v => !linkedNode.has(v[0]))
          .sort((a, b) => a[1] - b[1]);

      const [n, cost] = candidates.shift();
      linkedNode.add(n);
      candidates.push(...neighborNodes[n]);
      answer += cost;
  }
  return answer;
}