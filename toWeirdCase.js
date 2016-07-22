function toWeirdCase(string){
  word_arr = string.split(" ")
  weird_arr = []
  for (i = 0; i < word_arr.length; i++) {
    arr = [];
    word = word_arr[i]
    for (j = 0; j < word.length; j++) {
      if (j % 2 == 0)
        arr.push(word[j].toUpperCase());
      else
        arr.push(word[j].toLowerCase());
    }
    weird_arr.push(arr.join(""))
  }
  return weird_arr.join(" ")
}