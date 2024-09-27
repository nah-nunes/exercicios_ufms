''' A função cadastra uma lista de produtos com preços, solicitando ao usuário o nome e preço de cada um em um 
loop até atingir a quantidade especificada por n, evitando duplicatas ao verificar se o produto já foi cadastrado e,
 ao final, retorna uma lista de tuplas com o nome e preço de cada produto.'''



def cadastrar_produtos(n):
    # Lista vazia que armazenará os produtos e seus preços
    produtos = []
    
    # Loop para coletar 'n' produtos
    for _ in range(n):
        # Solicita o nome do produto ao usuário
        produto = input("Digite o nome do produto: ")
        
        # Solicita o preço do produto ao usuário e converte para float
        preco = float(input("Digite o preço do produto: "))
        
        # Verifica se o produto já está cadastrado (ignorando maiúsculas/minúsculas)
        for item in produtos:
            if item[0].lower() == produto.lower():
                # Se o produto já estiver na lista, exibe o preço dele
                print(f"O produto já existe. Preço: {item[1]}")
                break
        else:
            # Se o produto não estiver na lista, adiciona-o à lista de produtos
            produtos.append((produto, preco))
    
    # Retorna a lista de produtos cadastrados
    return produtos

''' A função busca o preço de um produto na lista cadastrada em um loop contínuo até o usuário digitar "fim", 
exibindo o preço se o produto for encontrado e não imprimindo nada se não for.'''

def buscar_preco(produtos):
    # Loop para buscar preços continuamente até que o usuário digite "fim"
    while True:
        # Solicita o nome do produto a ser buscado
        produto_busca = input("Digite o nome do produto para buscar o preço (ou 'fim' para sair): ")
        
        # Se o usuário digitar "fim", o loop é interrompido
        if produto_busca.lower() == "fim":
            break
        
        # Verifica se o produto buscado está na lista de produtos
        for item in produtos:
            if item[0].lower() == produto_busca.lower():
                # Se o produto for encontrado, exibe o preço dele
                print(f"Preço: {item[1]}")
                break
        else:
            # Se o produto não for encontrado, imprime uma linha vazia
            print("Produto não encontrado.")

'''A função principal do programa coordena sua execução solicitando ao usuário a quantidade de produtos a cadastrar e,
 em seguida, chamando as funções de cadastro e busca de preços.'''

def main():
    # Solicita o número de produtos que serão cadastrados
    n = int(input("Quantos produtos você deseja cadastrar? "))
    
    # Chama a função de cadastro de produtos e armazena a lista retornada
    produtos = cadastrar_produtos(n)
    
    # Chama a função de busca de preços, passando a lista de produtos cadastrados
    buscar_preco(produtos)

# Chama a função principal para iniciar a execução do programa
main()
