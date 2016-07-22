function pigIt(str){
  var arr = str.split(" ");
  var result = "";
  for (var i = 0; i < arr.length; i++) {
    result += arr[i].slice(1) + arr[i][0] + "ay";
    if (i < arr.length - 1)
      result += " ";
  }
  return result;
}