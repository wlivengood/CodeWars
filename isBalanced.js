function isBalanced(s, caps) {
  var opens = "";
  var closes = "";
  var stack = [];
  for (var i = 0; i < caps.length; i++) {
    if (i % 2 === 0)
      opens += caps[i];
    else
      closes += caps[i];
  }
  for (var j = 0; j < s.length; j++) {
    if (opens.indexOf(s[j]) > -1 && closes.indexOf(s[j]) > -1) {
      if (s.match(new RegExp(s[j], "g")).length % 2 !== 0) {
        return false;
      }
      else continue;
    }
    else 
      if (opens.indexOf(s[j]) !== -1)
        stack.push(s[j]);
    else
      if (closes.indexOf(s[j]) !== -1) {
        if (stack.length === 0)
          return false;
        else
          var match = stack.pop();
          if (match !== opens[closes.indexOf(s[j])])
            return false;
      }
  }
  return stack.length === 0;
}