def lcs(x, y):
  if not x or not y:
      return ""
  if x[0] == y[0]:
      return x[0] + lcs(x[1:], y[1:])
  else:
      return max(lcs(x, y[1:]), lcs(x[1:], y), key=len)
