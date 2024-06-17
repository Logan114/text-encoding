seed = open("seed.txt","r")
kiFile = open ("out.txt","r")
shift = seed.readlines()
output = ""
charkod:int = 0
kodolt = kiFile.read()

for i in range (0,len(kodolt)):
    charkod = (ord(kodolt[i])) - int(shift[i])
    output +=(chr(charkod))
print("The decoded text is:\n",output)