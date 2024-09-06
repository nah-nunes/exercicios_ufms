# Criando uma lista com os quadrados dos números de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
print(quadrados)  # Saída: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Criando uma lista com as vogais de uma palavra
palavra = "banana"
vogais = [letra for letra in palavra if letra in 'aeiou']
print(vogais)  # Saída: ['a', 'a', 'a']