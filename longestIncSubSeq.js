function longestSequenceIn(string) {
  return string.split(' ').reduce((a, num) => {
    if (!a.max) a = {max: 1, len: 1, step: NaN, prev: +a}
    let step = +num - a.prev,
        len = step === a.step || isNaN(a.step) ? a.len + 1 : 2
    return {
      len: len,
      max: Math.max(len, a.max),
      step: step,
      prev: +num
    }
  }).max || +!!string
}