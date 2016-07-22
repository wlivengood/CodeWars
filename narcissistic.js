function narcissistic( value ) {
  var arr = value.toString().split("");
  return arr.map(function(x) {
    return Math.pow(Number(x), arr.length)
  }).reduce(function(a,b) {return a + b}) === value;
}