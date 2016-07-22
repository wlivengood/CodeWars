var largestDifference = function(data) {
  var result = 0;
  for(var i = 0; i < data.length; ++i) {
    for(var j = 1; j < data.length; ++j) {
      if (data[i] <= data[j]) {
        if(j-i > result)
          result = j-i;
      }
    }
  }
  return result;
};