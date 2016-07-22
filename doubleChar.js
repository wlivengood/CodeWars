function doubleChar(str) {
  dbl = "";
  for (i = 0; i < str.length; i ++)
    dbl += str[i].repeat(2);
  return dbl;
}