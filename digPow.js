function digPow(n, p){
  s = n.toString();
  sum = 0;
  for (i = 0; i < s.length; i++) {
    sum += Math.pow(s[i], p + i);
  }
  return sum % n == 0 ? sum/n : -1;
}