nome = input('Digite seu nome: \n')
idade = int(input('Digite sua idade: \n'))

print('Olá, {}!\nVi que você tem {} anos.'.format(nome, idade))
msg = input('Deseja continuar? [S/N] \n')

if msg in ["S", "s", "sim", "Sim"]:
    salario = float(input('Ok, vamos continuar...\nQual seu salário atual? \n'))
    fam = int(input("Você tem filhos?\nSe sim, quantos? "))

    if salario > 1500 and fam <= 3:
        print('Parabéns, você pode financiar o carro!')
        fin = input('Escolha um plano:\n\n1. 12x R$ 15.340,00\n2. 24x R$ 9.040,00\n3. 48x R$ 4.610,00\n')
        if fin == "1":
            print('Parabéns, você acaba de começar o plano de 12 Meses')
        elif fin == "2":
            print('Parabéns, você acaba de começar o plano de 24 Meses')
        elif fin == "3":
            print('Parabéns, você acaba de começar o plano de 48 Meses')
        else:
            print('Você não escolheu nenhum plano válido, tente novamente!')

    else:
        cons = input('Não consigo liberar o financiamento, mas tenho uma condição especial para você, caso queira adquiri-lo pelo consórcio! \nTem interesse? [S/N] ')
        if cons in ["S", "s", "sim", "Sim"]:
            print('Ótimo, responda algumas perguntas e conseguiremos te ajudar!')
            cpf = input('Digite seu CPF: \n')
            rg = input('Digite seu RG: \n')
            planos = int(input('Ok, escolha o melhor plano para você:\n\n1. 12x R$ 12.340,00\n2. 24x R$ 7.040,00\n3. 48x R$ 3.610,00\n'))
            if planos == 1:
                print('Parabéns, você acaba de começar o plano de 12 Meses')
            elif planos == 2:
                print('Parabéns, você acaba de começar o plano de 24 Meses')
            elif planos == 3:
                print('Parabéns, você acaba de começar o plano de 48 Meses')
            else:
                print('Você não escolheu nenhum plano válido, tente novamente!')
        else:
            print('Certo, se mudar de ideia é só entrar em contato, obrigado!')