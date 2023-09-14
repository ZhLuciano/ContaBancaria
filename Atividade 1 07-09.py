# # cria_conta( ), que recebe como argumento numero, titular, saldo e limite.

def cria_conta(numero=0, titular="desconhecido", saldo=0.0,codigo=1, limite=0.0):
    conta = {
            'numero': numero,
            'titular': titular,
            'saldo': saldo,
            'limite': limite,
            'tipo_conta': codigo
             }
    return conta

conta=cria_conta(100)

print(conta)

# Crie uma função chamada deposita( ) no mesmo arquivo que recebe como argumento uma conta e um valor. Dentro da função, adicione o valor ao saldo nos tipo de conta.

def deposita(conta,valor):
    conta['saldo']=valor
    return conta

print(deposita(conta, 10))

# def edita_conta(conta,key,txt):
#     conta[key]=txt
#     return conta

# print(edita_conta(conta,'limite',10000000))
# print(edita_conta(conta,'numero',50000000))

def saca(conta, tipo_conta, valor):
    if tipo_conta in conta:
        if conta[tipo_conta]['saldo'] >= valor:
            conta[tipo_conta]['saldo'] -= valor
            print(f'Saque de {valor} realizado com sucesso na conta {tipo_conta}.')
        else:
            print(f'Saldo insuficiente na conta {tipo_conta} para sacar {valor}.')
    else:
        print(f'Conta {tipo_conta} não encontrada.')

# Exemplo de uso da função:
contas = {
    'corrente': {'saldo': 1000.00},
    'poupanca': {'saldo': 5000.00}
}

tipo_conta = input('Digite o tipo de conta (corrente ou poupanca): ')
valor_saque = float(input('Digite o valor a ser sacado: '))

saca(contas, tipo_conta, valor_saque)
print(contas)  # Mostra o saldo atualizado das contas



    

