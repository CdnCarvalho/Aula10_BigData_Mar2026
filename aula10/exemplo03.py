print('=== Cálculo de Produtividade ===')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de Funcionários: '))    
    media_por_funcionario = total_produzido / funcionarios

except (ValueError, TypeError):
    print('O valor precisa ser numérico')
except ZeroDivisionError:
    print('Funcionário não pode ser Zero.')

# Se não der erro, executa o else
else:
    print(f'Média por funcinário: {media_por_funcionario:.2f}')
