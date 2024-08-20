
#não é porssivel concatenar numeros inteiros com o texto com o sinal + , a menos que ele seja convertido em String
num = int(input('digite um numero inteiro: '))

print('ola' + str(num) + 'seja bem-vindo')

#concatenacção com (,)
print('o numero digitado foi:', num)

#concatenação com fstring (f)
print(f'o numero digitado é: {num} usando a concatenação de "f"')

div = num / 3
print(f'o resultado da divisão é: {div:.5f}')

#usando format para a formatação numerica
#limitando a quanidade de casas decimais

nome = input('digite seu nome aqui: ')
email = input('qual seu email: ')
cidade = input('onde voce mora: ')
precogas = float(input('coloque quanto custa a gasolina do posto: '))
precoal = float(input('coloque quanto custa o alcool do posto:' ))
divgas = (64 * 20) / 14
dival = (64 * 20) / 12
prgas = precogas * divgas 
pral = precoal * dival 

print(f'se voce abastecer com a gasolina sera gasto {divgas:.2f}, esse mes, quase um tanque e meio por mes, na minha opnião esta valendo mais a pena ')
print(f'se voce abastecer com o alcool sera gasto {dival:.2f}, esse mes, praticamente dois tanques')
print(f'voce ira gastar R${prgas:.2f}, por mes se voce abastecer com a gasolina')
print(f'voce ira gastar R${pral:.2f}, por mes se voce abastecer com o alcool')

