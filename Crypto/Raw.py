senha = input("Qual sua senha?\n")
senhaCrypt = {}
for character in senha:
    cleanHex = hex(ord(character))[2:]
    senhaCrypt.update({str(ord(character)):cleanHex})

print(senhaCrypt)