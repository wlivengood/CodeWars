function isPalindrome(n) {
  return n.toString() === n.toString().split('').reverse().join('');
}

var palindromeChainLength = function(n) {
  var count = 0;
  while (!isPalindrome(n)) {
    n += Number(n.toString().split('').reverse().join(''));
    count++;
  }
  return count;
};