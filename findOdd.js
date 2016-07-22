function findOdd(A) {
  var hash = {};
  for (var i = 0; i < A.length; i++) {
    if (hash[A[i]] !== undefined)
      hash[A[i]].push(A[i]);
    else
      hash[A[i]] = [A[i]]
  }
  for (var prop in hash) {
    if (hash[prop].length % 2 === 1)
      return Number(prop);
  }
}