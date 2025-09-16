'''
Exercícios sobre os comandos de condição em python
'''

from datetime import date, datetime

HOJE = datetime.now() # Pega data/hora do computador

def exemploSe():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')

def exemploSeSenao():
    idade = int(input('Idade:'))
    if idade >= 18:
        print('Maior de idade')    
    else:
        print('Menor de idade')
    print('fim do programa')

def exemploSe_SenaoSe_Senao():
    idade = int(input('Idade:'))
    if idade < 18:
        print('Menor de idade')    
    elif idade < 65:
        print('Maior de idade')
    elif idade < 50:
        print('Pessoa madura')
    else:
        print('Idoso')
    print('fim do programa')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    n1 = int(input('Digite um valor inteiro: '))
    n2 = int(input('Digite outro valor inteiro: '))
    soma = n1 + n2
    if soma > 10:
        print(soma)

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    n1 = int(input('Digite um valor inteiro: '))
    n2 = int(input('Digite outro valor inteiro: '))
    soma = n1 + n2
    if soma > 20:
        print(soma + 8)
    else:
        print(soma - 5)    

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num = int(input('Digite um inteiro: '))
    if num % 3 == 0:
        print('É múltiplo de 3')
    else:
        print('Não é múltiplo de 3')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
    num = int(input('Digite um inteiro: '))
    if num % 5 == 0:
        print('É divisível por 5')
    else:
        print('Não é divisível por 5')

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num = int(input('Digite um inteiro: '))
    if num % 3 == 0 and num % 7 == 0:
        print('É divisível por 3 e 7')
    else:
        print('Não é divisível por 3 e 7')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6():
    salario = float(input('Salário bruto: R$ '))
    prestacao = float(input('Prestação para autorizar: R$ '))
    prestacao_maxima = salario * 0.3
    if prestacao > prestacao_maxima:
        print('Empréstimo não autorizado')
    else:
        print('Empréstimo autorizado')

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
    num = int(input('Número inteiro: '))
    if 20<=num<=50: # num >= 20 and num <= 50
        print('Está entre 20 e 50')
    else:
        print('Não está entre 20 e 50')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
    num = int(input('Número inteiro: '))
    if num < 20:
        print('É menor do que 20')
    elif num > 20:
        print('É maior do que 20')
    else:
        print('É igual a 20')

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
    ano_nasc = int(input('Ano de nascimento: '))
    ano_atual = int(input('Ano atual: '))
    if ano_nasc > ano_atual:
        print('ERRO: Não pode ter nascido no futuro')
    else:
        print(f'Idade: {ano_atual - ano_nasc} anos')

def q91():
    data_str = input('Data de nascimento (dd/mm/aaaa): ')
    print(f'Ano atual: {datetime.strftime(HOJE,"%Y")}')
    data_nascimento = datetime.strptime(data_str, '%d/%m/%Y')
    if data_nascimento > HOJE:
        print('Data de nascimento inválida!')
    else:
        print(f'Idade: {int((HOJE - data_nascimento).days/365)} anos.')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.

def q10():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    numeros = [n1, n2, n3]
    numeros.sort()

    print("Números em ordem crescente:", numeros)
q10()

        
#11. Faça um programa que leia 3 números e imprima o maior deles.

def q11():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    maior = n1

    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3

    print(f"O maior número é: {maior}")
q11()


#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos

def q12():
    idade = int(input('Digite a idade: '))
    
    if idade < 18:
        print('Menor de idade')
    elif 18 <= idade < 65:
        print('Maior de idade')
    else:
        print('Maior de 65 anos')
q12()


#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

def q13():
    nom = input('Digite seu nome: ')
    p1 = float(input('Nota Prova 1: '))
    p2 = float(input('Nota Prova 2: '))

    p = (p1 + p2) / 2  # média correta

    if p >= 7:
        print(f'Aprovado: {nom}, Média: {p:.2f}')
    elif 3 <= p < 7:
        print(f'Reprovado: {nom}, Média: {p:.2f}')
    else:
        print(f'{nom} precisa fazer a prova final. Média: {p:.2f}')
q13()



#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

def q14():
    salario = float(input('Digite o salário: '))

    if salario < 600:
        print('Isento')
    elif 600 <= salario < 1200:
        sal = salario * 0.8  # desconto de 20%
        print(f'Salário com 20% de desconto do INSS: R$ {sal:.2f}')
    else:
        print('Faixa salarial não contemplada neste programa.')
q14()


#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

def q15():
    produto = float(input('Digite o valor do produto: '))

    if produto <= 20:
        lucro = produto * 1.45
        print(f'Lucro de 45% será: R$ {lucro:.2f}')
    else:
        lucro = produto * 1.30
        print(f'Lucro de 30% será: R$ {lucro:.2f}')
q15()


#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

def q16():
    idade = int(input('Digite sua idade: '))
    
    if 5 < idade < 7:
        print('Infantil A')
    elif 7 <= idade < 9:
        print('Infantil B')
    elif 9 <= idade < 11:
        print('Juvenil A')
    elif 11 <= idade < 14:
        print('Juvenil B')
    elif idade >= 14:
        print('Sênior maiores de 18 anos')
    else:
        print('Idade fora das categorias definidas')
q16()


#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

def q17():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    if idade <= 10:
        print(f'Idade até 10 anos: {nome} - valor de 30')
    elif idade <= 28:
        print(f'Idade entre 11 a 28: {nome} - valor de 60')
    elif idade <= 44:
        print(f'Idade entre 29 a 44: {nome} - valor de 120')
    elif idade <= 58:
        print(f'Idade entre 45 a 58: {nome} - valor de 150')
    elif idade <= 65:
        print(f'Idade entre 59 a 65: {nome} - valor de 250')
    else:
        print(f'Idade maior que 65 anos: {nome} - valor de 400')
q17()



#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

def q18():
    num = int(input('Digite um número inteiro entre 1 e 12: '))

    if num < 1 or num > 12:
        print('Não existe mês com este número.')
    else:
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        print(meses[num - 1])
q18()



#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

def q19():
    a = int(input("Pontos do jogador 1: "))
    b = int(input("Pontos do jogador 2: "))
    c = int(input("Pontos do jogador 3: "))

    if a != b and a != c and b != c:
        print("Pontos em ordem decrescente:", end=' ')
        if a > b and a > c:
            if b > c:
                print(a, b, c)
            else:
                print(a, c, b)
        elif b > a and b > c:
            if a > c:
                print(b, a, c)
            else:
                print(b, c, a)
        else: 
            if a > b:
                print(c, a, b)
            else:
                print(c, b, a)

        soma = a + b + c
        if soma > 100:
            media = soma / 3
            print(f"Média dos pontos: {media:.2f}")
        else:
            print("Equipe desclassificada.")
    else:
        print("Os jogadores devem ter pontuações diferentes.")
q19()



#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

def q20():
    saldo = float(input("Digite o saldo médio do cliente: R$ "))

    if saldo <= 500:
        credito = 0
    elif saldo <= 1000:
        credito = saldo * 0.30
    elif saldo <= 3000:
        credito = saldo * 0.40
    else:
        credito = saldo * 0.50
    print(f"\nSaldo médio: R$ {saldo:.2f}")
    print(f"Valor do crédito especial: R$ {credito:.2f}")
q20()



#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

def q21():
    livro = input("Nome do livro: ")
    tipo = input("Tipo de usuário (professor ou aluno): ").strip().lower()

    if tipo == "professor":
        dias = 10
    elif tipo == "aluno":
        dias = 3
    else:
        print("Tipo de usuário inválido. Use 'professor' ou 'aluno'.")
        return

    print("\n--- Recibo de Empréstimo ---")
    print(f"Nome do livro: {livro}")
    print(f"Tipo de usuário: {tipo.capitalize()}")
    print(f"Total de dias: {dias}")
q21()


#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

def q22():
    percurso = float(input("Informe o percurso em quilômetros: "))
    tipo = input("Informe o tipo do carro (A, B ou C): ").strip().upper()

    if tipo == "A":
        consumo = percurso / 12
    elif tipo == "B":
        consumo = percurso / 9
    elif tipo == "C":
        consumo = percurso / 8
    else:
        print("Tipo de carro inválido. Use A, B ou C.")
        return

    print(f"\nConsumo estimado de combustível: {consumo:.2f} litros")
q22()


#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

def q23():
    prato = input("Digite o prato (Vegetariano, Peixe, Frango, Carne): ").strip().lower()
    sobremesa = input("Digite a sobremesa (Abacaxi, Sorvete diet, Mousse diet, Mousse chocolate): ").strip().lower()
    bebida = input("Digite a bebida (Chá, Suco de laranja, Suco de melão, Refrigerante diet): ").strip().lower()

    pratos = {
        "vegetariano": 180,
        "peixe": 230,
        "frango": 250,
        "carne": 350
    }

    sobremesas = {
        "abacaxi": 75,
        "sorvete diet": 110,
        "mousse diet": 170,
        "mousse chocolate": 200
    }

    bebidas = {
        "chá": 20,
        "suco de laranja": 70,
        "suco de melão": 100,
        "refrigerante diet": 65
    }

    # Verifica se entradas são válidas
    if prato not in pratos:
        print("Prato inválido.")
        return
    if sobremesa not in sobremesas:
        print("Sobremesa inválida.")
        return
    if bebida not in bebidas:
        print("Bebida inválida.")
        return

    total = pratos[prato] + sobremesas[sobremesa] + bebidas[bebida]

    print(f"Total de calorias: {total} cal")
q23()


#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

def q24():
    placa = input("Digite a placa do carro: ").strip().upper()
    ultimo_char = placa[-1]
    
    if not ultimo_char.isdigit():
        print("Placa inválida! O último caractere deve ser um número.")
        return
    numero = int(ultimo_char)

    mes = 12 if numero == 0 else numero
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    print(f"O emplacamento deve ser renovado em {meses[mes]}.")
q24()



#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

def q25():
    indice = float(input("Digite o índice de poluição: "))

    if indice <= 0.25:
        print("Índice aceitável. Nenhuma intimação necessária.")
    elif indice == 0.3:
        print("Intimação para o 1º grupo.")
    elif indice == 0.4:
        print("Intimação para o 1º e 2º grupos.")
    elif indice == 0.5:
        print("Intimação para o 1º, 2º e 3º grupos.")
    else:
        print("Índice fora dos valores previstos para intimação.")
q25()
