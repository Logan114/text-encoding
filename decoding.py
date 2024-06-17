
print("Do you have an encrypted text in a txt file?")
key = input().strip().lower()
if key == 'n':
    encoded = input("Please paste the encrypted text\n")
elif key == 'y':
    filename = input("what is the filename of it?")
    kiFile = open (filename,"r")
    encoded = kiFile.read()
      
seed = open("seed.txt","r")

shift = seed.readlines()
output = ""
charcode:int = 0

for i in range (0,len(encoded)):
    charcode = (ord(encoded[i])) - int(shift[i])
    output +=(chr(charcode))
print("The decoded text is:\n",output)