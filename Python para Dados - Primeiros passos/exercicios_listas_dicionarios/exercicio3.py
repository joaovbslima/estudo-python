# 3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

lista_num = []
for i in range(1, 6):
    item = int(input('Digite um número inteiro: '))
    lista_num.append(item)

print(lista_num)