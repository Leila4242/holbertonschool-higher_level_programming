#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("object-oriented programming"):str.find("l")] + str[str.find("with"):str.find("very")] + str[str.find("Python"):str.find("is")]
print(str)