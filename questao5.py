def inverterString(string):
    invertida = ''
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

original = input("Digite uma palavra: ")
invertida = inverterString(original)
print("Original:", original)
print("Invertida:", invertida)
