def group_check(s):
  stack = []
  opens, closes = "({[", ")}]"
  for c in s :
    if c in opens :
      stack.append(c)
    elif c in closes :
      if len(stack) == 0:
        return False
      else :
        stack_last = stack.pop()
        match = opens[closes.index(c)]
        if stack_last != match:
          return False
    else :
      return False
  if len(stack) == 0:
      return True
  else: return False
