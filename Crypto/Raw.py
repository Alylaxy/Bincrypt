#Self explanatory
def isHex(n):
    try:
        int(n,10)       #Tests if n is a decimal number. If not, means it's hexadecimal
    except:
        return True
    else:
        return False

#Sums the algarisms of a number
def sumAlgarism(n):
    totalSum = 0
    i = 1
    for algarism in n:
        trueValue = int(algarism, 16) * 10 ** (len(n) - i) #Multiplies by 10 according to house in algarism order
        totalSum += trueValue
        i+=1
    return totalSum

code = input("Qual sua senha?\n")
encodedCrypt = {}
i=1
for character in code:
    cleanHex = hex(ord(character))[2:]          #Ignores '0x'
    if not isHex(cleanHex[1]):
        if not isHex(cleanHex[0]):
            mod = 'ª'                           #ª = not Hex when decripting  
    else:
        mod = 'º'                               #º = consider Hex when decripting
    cleanBin = bin(sumAlgarism(cleanHex))[2:]   #Ignores '0x'
    print("{}\t{} = {}{}".format(i,character, cleanBin, mod))
    i+=1
