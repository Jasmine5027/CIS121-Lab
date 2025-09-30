def every_word(sentence):
  word = []
  collection = ''
  for x in sentence:
    if x != ' ':
      collection += x
    else:
      word.append(collection)
      collection = ''
    
  if collection != '':
    word.append(collection)

  return word

sentence = input('Enter your sectence:')

print(every_word(sentence))