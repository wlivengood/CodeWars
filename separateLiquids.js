function separateLiquids(glass) {
  var obj = {};
  
  var densities = {
    "H": 1.36,
    "W": 1.00,
    "A": 0.87,
    "O": 0.80
  }
  
  for (let i = 0; i < glass.length; i++) {
    for (let j = 0; j < glass[i].length; j++) {
      if (obj[glass[i][j]])
        obj[glass[i][j]]++;
      else
        obj[glass[i][j]] = 1;
    }
  }
  
  var ordered = Object.keys(densities).sort(function(a,b) {
    if (densities[a] > densities[b])
      return -1;
    else if (densities[a] < densities[b])
      return 1;
    else
      return 0;
    });
    
  var oneDimArray = [];
  
  for (let i = 0; i < ordered.length; i++) {
    for (let j = 0; j < obj[ordered[i]]; j++) {
      oneDimArray.push(ordered[i]);
    }
  }
  for (let i = 0; i < glass.length; i++) {
    for (let j = 0; j < glass[i].length; j++) {
      glass[i][j] = oneDimArray.pop();
    }
  }
  return glass;
}