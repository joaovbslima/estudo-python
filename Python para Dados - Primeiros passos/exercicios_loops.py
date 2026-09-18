# %%
# 1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while n1 != n2:
    if n2 > n1:
        print(n1)
        n1 += 1
    if n1 > n2:
        print(n1)
        n1 -= 1





# %%
# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.


a = 4
b = 10

prazo = 0

while a < b:
    prazo += 1
    a *= 1 + 0.03
    b *= 1 + 0.015



print(f'Sabendo que as colônias de bactérias A e B têm taxas de crescimento de 3% e 1,5% por dia, respectivamente e que a colônia A iniciou com 4 elementos e a colônia B com 10 elementos, podemos concluir que a colônia A vai ultrapassar ou igualar a colônia B em {prazo} dias. \n Alcançado esse prazo, cada amostra terá o seguinte tamanho: \n Amostra A: {a} elementos \n Amostra B: {b} elementos')




# %%
# 3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

usuario = 1

while usuario <= 5:
    nota = int(input('Digite uma nota de 0 a 5: '))
    
    if (nota < 0) or (nota > 5):
        print('Valor invalido para a nota!')
        nota = int(input('Digite uma nota de 0 a 5: '))
    else:
        usuario += 1
        print(nota)






# %%
# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.







# %%
# 5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.








# %%
# 6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.









# %%
# 7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.








# %%
# 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.








# %%
# 9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.