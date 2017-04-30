def printWordsWithHyphen(stringIn):
  split = stringIn.split(" ")
  split = sorted(split)
  joined = "-".join(split)
  print(joined)
  
printWordsWithHyphen("Hello I Am Dan")
printWordsWithHyphen("I Will Be Hyphenated When Printed")
printWordsWithHyphen("Here We Go")