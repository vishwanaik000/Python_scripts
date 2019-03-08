import os



y= os.listdir('D:\letusc')
print y
for x in y:
    if (x.endswith('.txt')):
        print x
        print "No .txt files"
for x in y:
    if (x.endswith('.pdf')):
        print x
print "No .pdf files"
for x in y:
    if (x.endswith('.log')):
        print x

