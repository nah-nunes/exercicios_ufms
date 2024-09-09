<aside>
💡

https://docs.google.com/document/d/e/2PACX-1vTLuF7HIpo5efyJAYEZL3ly7joZ74hhwnV-cUKeqEWnRIgSQbrIJmj1VdxPH7GGEfWAmhNbn7DtfZX8/pub - trilha de aprendizagem

https://padlet.com/sepedagead/estrutura-de-dados-wg2boqwg6mqc6oy4

</aside>

### 1. Tabela Hash

> Associar através de uma função de dispersão cada chave a um valor na tabela (memória)
> 

Tabela hash é uma estrutura de dados usada para armazenar e acessar dados de forma muito rápida.

Uma tabela hash usa pares de chave-valor. A chave sendo uma espécie de apelido para acessar o valor.

A tabela usa uma função hash, que é como uma formula matemática, que pega a chave e gera  um número chamado índice que é usado para determinar onde os dados vão ser armazenados na tabela. 

**Acessando dados**

Quando quiser acessar uma chave de novo, se coloca a chave na função hash e ela te diz em que posição está o valor 

**Definições Tabela de Dispersão** 

Variáveis da tabela de dispersão:

- **d (dado):**  podendo ser de qualquer tipo: string, float, objeto, matriz.
- **k(chave/posição na tabela):** Valores inteiros de 0 até M-1;
- **T (vetor\tabela):**
- **M (tamanho da tabela):**  idealmente um numero primo.
- **v(valor\dado):** armazenado na tabela;
- **F(função de dispersão):**

> **F(d) =k; T[k] = d;**
> 

Podemos ter funções perfeitas e imperfeitas, o difícil é encontrar funções perfeitas em prática. 

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/d2c0e1bc-53f8-4343-8a9f-98f6ed817028/image.png)

**O que se espera de uma boa função de dispersão?** 

- Seja rápido calcular a chave para um dado e rápido acessar a chave na tabela, custo 0(1)
- Distribua (disperse) igualmente os dados na tabela;
- Capture no dado alguma informação que seja relevante para obter uma chave única;

**O que seria ruim para uma função de dispersão?**

- Custo alto de cálculo > 0(N);
- Para cada chave ter associado mais de um dado (colisão)

**Como funciona para Strings?**

- Associar um valor para cada character da string (Tabela ASCII)
- Somar os valores de cada caractere para obter o dado numérico.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/dc39b112-e290-47b4-bacb-092da9e25605/image.png)

**Criando funções de dispersão**

 **Divisão**

A mais clássica função de dispersão é usar a fórmula do resto da divisão (mod ou %) também conhecido como método da divisão, dado % m , m é um número inteiro maior que zero. 

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/3c2f8030-6c71-4de8-8771-e377024e423e/image.png)

- Impacto da escolha de m: F(dado) = dado % m
- A ideia é simular a caminhada em uma estrutura linear de maneira circular

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/393ef0a1-e9d6-473e-84db-2a6542c52de4/image.png)

**Multiplicação**

Usar os valores fracionados de uma multiplicação para determinar a posição da chave;

Utiliza outra constante A, tal que 0 < A < 1;

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/32fc405c-6f3b-4e3b-9aba-eb9bd64f8ff9/image.png)

**Dobra**

- Dobrar o dado como se dobra um papel;
- Quebrar o dado em partes (dobrar e somar) até que se tenha a posição válida(chave) para a tabela de tamanho M;

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/cc0f4763-601f-4c79-ba0e-d646026c123b/image.png)

O desempenho é medido pelo número de colisões, pode ser estimado pelo fator de carga (fc): quantidade de chaves/ M; 

Em geral as colisões ocorrem quando a distribuição das chaves é desigual ou quando a tabela tem tamanho pequeno; 

Estratégias para lidar com as colisões se fazem necessárias, vamos conhecer algumas delas; 

**Tratamentos de colisões**

O que são colisões? São quando dois ou mais valores estão associados a uma chave. 

Estratégias:

**Sondagem por endereçamento aberto:** 

- Tenta encontrar na tabela posições vizinhas disponíveis.
- Distribuir os valores diretamente na tabela;
- Encontrar (sondagem) em posições vizinhas daquela que houve colisão alguma posição disponível.

Algumas formas de fazer a sondagem: 

- **Sondagem linear**
    - Caminhar sequencialmente por toda tabela → Caso ocorra a colisão em alguma posição, incrementar sequencialmente a posição até encontrar uma não ocupada.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/1493f40c-5c8d-4829-b098-579e0cbb6964/image.png)
    

Quando não há uma colisão, temos que percorrer (no pior caso) a tabela inteira para encontrar uma posição disponível. A medida que o fator de carga (fc = N/ M) tende a 1, as colisões aumentam.

A sondagem permite formar agrupamentos, colocando valores parecidos em posições próximas. Esses agrupamentos, se muito grandes tendem a ocupar muitos espaços na tabela necessitando que a sondagem caminhe toda a tabela para encontrar uma posição disponível. 

- **Sondagem quadrática**
    - Caminhar em saltos quadráticos por toda a tabela;
    - A ideia da sondagem quadrática é quebrar os agrupamentos grandes de valores parecidos espalhando-os pela tabela.
    - Incrementa com o quadrado do passo : (dado + passo)% M → (dado + passo²)%M
    - O tamanho não pode ser par, por acarreta numa má distribuição dos valores pares.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/c9ecea97-12ec-4a6d-b2d7-88433de564d1/image.png)
    
- **Sondagem dupla**
    - Utiliza uma segunda função de dispersão F2 para resolver as colisões.
    
    F(d) = (F1(d) + passo * F2((d) % M)
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/8877b66b-e2b6-469b-9860-d04952320664/image.png)
    

A sondagem dupla é mais robusta que a linear e a quadrática, pelo fato de F2 ser uma função padrão diferente de distribuição das chaves do que F1. Ex: F1 lida com valores pares e F2 com valores impares.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/8db574ee-3dec-4507-875b-b50407f67a12/image.png)

**Sondagem por endereçamento encadeado:**

- Utilizar outras estruturas de dados para armazenar mais de um valor em uma chave (posição da tabela) com colisão.
- A ideia é armazenar dados\valores parecidos em uma estrutura de dados, por exemplo, uma lista encadeada, na posição de colisão.
- O curso de inserir um elemento, tanto na tabela quanto na lista, continua com custo 0(1). Porém o custo da busca na tabela e na lista são diferentes. na tabela 0(1) e na lista 0(N) N = tamanho da lista no pior caso.
- Mais simples de lidar com colisões ao invés de criar funções de dispersão mais elaboradas;
- Ideal para quando não se sabe como será a distribuição das chaves na tabela(dinâmica)
- Tamanho mais flexível do que no endereçamento aberto que considera o tamanho fixo na tabela.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/cf74a70c-9617-4742-bbf1-30be64035927/02091bca-3dcc-4444-a716-b5e476f50530/image.png)

### 2. Hash

Uma hash table é como um grande armário com vários compartimentos. Cada dado que você guarda tem uma chave que determina em qual compartimento ele vai. Essa chave é gerada por uma função chamada hash. São ótimas para quando você precisa encontrar ou guardar algo rapidamente, como um dicionário onde pode procurar uma palavra instantaneamente usando a sua chave. 

### Heaps

Estrutura de dados que parece uma arvore, onde o elemento principal ou raiz sempre tem o valor mais alto ou mais baixo, dependendo se é um max-heap ou min heap 

Ele é usado quando precisa acessar rapidamente o maior ou menor valor de um conjunto de dados, como em uma fila de prioridade. As inserções e remoções reorganizam os elementos para manter essa propriedade de maior ou menor no topo