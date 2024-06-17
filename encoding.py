import random
seed = open("seed.txt","w")
outFile = open ("out.txt","w")
text:str = input("Please enter the text you want to encode\n")
output = ""
charkod:int = 0
for i in range (0,len(text)):
    shift = random.randrange(0,255)
    charkod = (ord(text[i]))+ shift
    output +=(chr(charkod))
    shiftstr = (str((shift))+"\n")
    seed.write(str(shiftstr))
outFile.write(output)
seed.close()
outFile.close()