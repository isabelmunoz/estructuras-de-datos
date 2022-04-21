#Leer archivo

with open("lorem_ipsum.txt", "r") as archivo:
    textos = archivo.read()

#Recorrer archivo y contar los caracteres distintos
    unico = []
    for char in textos[::]:
        if char not in unico:
            unico.append(char)


#Contar las palabras unicas dentro del texto
    count = 0
    words = set(textos.split())
    for word in words:
        count += 1


    print(f'El número de caracteres distintos es: {len(unico)}')
    print('El número de palabras distintas es:', count)