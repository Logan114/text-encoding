seed = open("seed.txt","r")
kiFile = open ("out.txt","r")
shift = seed.readlines()
output = ""
charcode:int = 0
encoded = kiFile.read()

for i in range (0,len(encoded)):
    charcode = (ord(encoded[i])) - int(shift[i])
    output +=(chr(charcode))
print("The decoded text is:\n",output)