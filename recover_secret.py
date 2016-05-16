def recoverSecret(triplets):
  letters = list(set([i for triplet in triplets for i in triplet]))
  for x in range(len(letters)):
      for i in range(len(letters)):
          for j in range(len(triplets)):
              if letters[i] in triplets[j]:
                  for k in range(len(triplets[j])):
                      if triplets[j].index(letters[i]) < k and i > letters.index(triplets[j][k]):
                          letters[i], letters[letters.index(triplets[j][k])] = letters[letters.index(triplets[j][k])], letters[i]
                      if triplets[j].index(letters[i]) > k and i < letters.index(triplets[j][k]):
                          letters[i], letters[letters.index(triplets[j][k])] = letters[letters.index(triplets[j][k])], letters[i]
  return "".join(letters)
