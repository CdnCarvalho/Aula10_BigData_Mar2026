print('CAIXA ELETRÔNICO')

try:
    saldo = 1000
    saque = float(input('Informe o valor do saque: '))

except ValueError:
    print('Valor inválido')
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário')
else:
    if saque > saldo:
        print('Saldo Insuficiente')
    elif saque <= 0:
        print('Saque precisa ser maior ou igual a 0')
    else:
        saldo -= saque
        print('\nSaque realizado com sucesso')
        print(f'Saldo em conta R$ {saldo:.2f}')
finally:
    print('Operação realizada')

print('\nPrograma Encerrado')