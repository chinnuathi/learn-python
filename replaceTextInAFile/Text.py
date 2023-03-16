filename = input("get the file")
content = open(filename, 'r')
findtext = input("enter the first value")
replacetext = input("enter the second value")
lines = content.readlines()
for line in lines:
    print(line)
    print(line.replace(findtext, replacetext))