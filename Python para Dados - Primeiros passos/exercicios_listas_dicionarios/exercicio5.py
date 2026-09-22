# # 5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
#%%

def primo(numero):
    if numero <= 1:
        return False

    for i in range(2,numero):
        if numero % i == 0:
            return False

    return True

lista_primos = []

num = int(input('Digite um número inteiro: '))

for i in range (2, num + 1):
    if primo(i):
      lista_primos.append(i)
      
print(lista_primos)
