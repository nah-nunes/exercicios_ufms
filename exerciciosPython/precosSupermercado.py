def cadastrar_produtos(n):
    produtos = []
    for _ in range(n):
        produto = input()
        preco = float(input())
        for item in produtos:
            if item[0].lower() == produto.lower():
                print(item[1])
                break
        else:
            produtos.append((produto, preco))
    return produtos
def buscar_preco(produtos):
    while True:
        produto_busca = input()
        
        if produto_busca.lower() == "fim":
            break
        
        for item in produtos:
            if item[0].lower() == produto_busca.lower():
                print(item[1])
                break
        else:
            print("")

def main():
    n = int(input())
   
    produtos = cadastrar_produtos(n)
    
    buscar_preco(produtos)
main()
