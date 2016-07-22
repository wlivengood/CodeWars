function divisors(integer) {
  divs = [];
  for (var i = 2; i < integer; i++) {
    if (integer % i == 0)
      divs.push(i);
  }
  if (divs.length > 0)
    return divs
  else
    return integer.toString() + " is prime"
};