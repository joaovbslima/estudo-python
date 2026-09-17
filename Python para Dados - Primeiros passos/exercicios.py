# %%
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura (em metros): '))


print(f'Olá, {nome}! Você tem {idade} anos e mede {altura}')


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = n1 + n2

print(f'O resultado de {n1} - {n2} é igual a: {n1-n2}')


mp = ((5*1) + (12*2) + (20*3) + (15*4)) / (1+2+3+4)

print(mp)



# %%

# Manipulando strings

frase = input('Digite uma frase: ')

print(frase)

print(frase.upper())

print(frase.lower())

print(frase.strip())

print(frase.strip().lower())

print(frase.lower().replace('e','f'))

print(frase.lower().replace('a', '@'))

print(frase.lower().replace('s','$'))



# %%

# if, else, elif

sm1 = float(input('Digite a nota do simulado 1: '))
sm2 = float(input('Digite a nota do simulado 2: '))
av = float(input('Digite a nota da prova AV: '))
avs = float(input('Digite a nota da prova AVS: '))

if av >= avs:
    notafinal = av
else:
    notafinal = avs

notafinal = (notafinal + sm1 + sm2)


if notafinal >= 10:
    notafinal = 10

if notafinal >= 6:
    situation = 'APROVADO!'
    if notafinal == 10:
        situation = 'APROVADO COM NOTA MÁXIMA!'
else:
    situation = 'REPROVADO!'

print(f'Sua nota final é de {notafinal} pontos. Portanto, você foi {situation}')



# %%

# numero par

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'o número {numero} é par!')
else:
    print(f'o número {numero} é ímpar!')



# %%

# NÚMERO PRIMO: 
# Para calcular se um número é primo, utilizaremos a raiz quadrada.
# O cálculo é feito através de um loop (for). o loop testa números em um range de 2 até a (raiz quadrada de n) + 1.
# Se esse n dividido por algum número desse range tiver resto 0, quer dizer que não é primo, pois ele terá mais de um divisor.
# se ele sair do loop sem divisores ele é um número primo (primo=true)

def primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

num = int(input('Digite um número inteiro: '))

if primo(num):
    print(f'o número {num} é primo!')
else:
    print(f'o número {num} não é primo!')



# %%
# 10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.










# 11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.









# 12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.









# 13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para variação abaixo de -10%: corte de gastos.
# Caso precise de ajuda, opções de solução das atividades estarão disponíveis na seção “Opinião da pessoa instrutora”.











