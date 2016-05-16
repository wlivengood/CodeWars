def f(n, m):
  n = int(n)
  m = int(m)
  mod = n % m
  no_remainder = ((m - 1) * m) / 2 * (n//m)
  remainder = (mod * (mod + 1)) / 2
  total = no_remainder + remainder
  return total
