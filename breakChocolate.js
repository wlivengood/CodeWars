var breakChocolate = function(n, m) {
  if (m == 0 || n == 0)
    return 0
  else
    return (m - 1) + m * (n-1);
};