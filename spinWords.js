function spinWords(s){
  return s.split(' ').map(function(w) { return w.length >= 5 ? w.split('').reverse().join('') : w }).join(' ');
}