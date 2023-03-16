try:
    inFilename = input("enter input file")
    inContent = open(inFilename, 'r')
    outFilename = input("enter output filename")
    outContent = open(outFilename, 'w')
except:
    print("the file doesn't exit")
else:
    findText = input("enter the text to be replaced")
    replaceText = input("enter the replacement text")
    lines = inContent.readlines()
    for line in lines:
       text = (line.replace(findText, replaceText))
       outContent.write(text)