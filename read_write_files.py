fw = open("sample.txt", "w")
fw.write("Add some text to this file\n")
fw.write("I like Swimming\n")
fw.close()

fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()