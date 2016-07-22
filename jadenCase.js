String.prototype.toJadenCase = function () {
  return this.split(' ').map(function(word){return word[0].toUpperCase() + word.slice(1,word.length)}).join(' ');
};