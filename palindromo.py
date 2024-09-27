def eh_palindromo(numero):
   
    numero_str = str(numero)
   
    return numero_str == numero_str[::-1]

numero = int(input())


if eh_palindromo(numero):
    print("sim")
else:
    print("não")
