try:
    filename = input("get the file")
    inContent = open(filename, 'r')
    outfilename = input("enter output filename")
    outContent = open(outfilename, 'w')
except:
    print("the file doesn't exit")
else:
    #content = open(filename, 'r')
    findtext = input("enter the first value")
    replacetext = input("enter the second value")
    lines = inContent.readlines()
    for line in lines:
       #print(line)
       text = (line.replace(findtext, replacetext))
       outContent.write(text)

