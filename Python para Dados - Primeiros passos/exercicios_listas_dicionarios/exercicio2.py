# 2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

lista_gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

gastos_acima_3000 = 0
total_gasto_acima_3000 = 0

for gasto in lista_gastos:
    if gasto > 3000:
        total_gasto_acima_3000 += gasto
        gastos_acima_3000 += 1

porcentagem = (gastos_acima_3000 / len(lista_gastos)) * 100
print(f'{porcentagem}% das compras foram acima de 3000,00 totalizando o valor de R${total_gasto_acima_3000}')