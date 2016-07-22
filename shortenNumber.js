function shortenNumber(suffixes, base) {
  return function(num) {
    if (typeof num !== "string")
      return num.toString();
    var index = 0;
    while (num > base && index < suffixes.length - 1) {
      num = Math.floor(num/base);
      index++;
    }
    return num + suffixes[index];
  }
}