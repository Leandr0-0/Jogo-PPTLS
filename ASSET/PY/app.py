# REGRAS DO JOGO:
# Pedra esmaga tesoura e largato;
# Papel enrola pedra e refuta Spock;
# Tesoura corta papel e decapita largato;
# Largato come papel e envenena Spock;
# Spock esmaga tesoua e vaporiza papel.

# RESUMO:
# Pedra > tesoura e largato;
# Papel > pedra e Spock;
# Tesoura > papel e largato;
# Largato > papel e Spock;
# Spock > pedra e tesoura.


from random import randint 
itens = ('Pedra', 'Papel', 'Tesoura', 'Largato', 'Spock')
computador = randint(0, 4)


print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] LARGATO
[ 4 ] SPOCK''')


jogador = int(input('Qual é a sua jogada?'))
print('-=' * 12)
print ('Eu joguei: {}'.format(itens[computador]))
print ('Você jogou: {}'.format(itens[jogador]))
print('-=' * 12)


if computador == 0: # Computador jogou pedra.
    if jogador == 0: # Jogador jogou pedra.
        print ('Eeeita! Jogamos iguias kkk.')
    
    elif jogador == 1: # Jogador jogou papel.
        print ('Cê venceu! Papel enrola pedra.')
        
    elif jogador == 2: # Jogador jogou tesoura.
        print ('Eu venci! Pedra esmaga tesoura.')

    elif jogador == 3: # Jogador jogou largato.
        print('Eu venci! Pedra esmaga largato.')

    elif jogador == 4: # Jogador jogou Spock.
        print ('Cê venceu! Spock vaporiza pedra.')

    else: 
        print ('JOGADA INVÁLIDA!')


if computador == 1: # Computador jogou papel.
    if jogador == 0: # Jogador Jogou pedra.
        print ('Eu venci! Papel enrola pedra.')

    elif jogador == 1: # Jogador jogou pepel.
        print ('Deu zebra! Empatou.')

    elif jogador == 2: #Jogador jogou tesoura.
        print ('Você venceu! Tesoura corta papel.')

    elif jogador == 3: # Jogador jogou largato.
        print ('Você venceu! Lagarto come papel.')

    elif jogador == 4: # Jogador jogou Spork.
        print ('Eu venci! Papel refuta Spock.')

    else:
        print ('JOGADA INVÁLIDA!')


if computador == 2: # Computador jogou tesoura.
    if jogador == 0: # Jogador jogou pedra.
        print ('Cê venceu! Pedar esmaga tesoura.')

    elif jogador == 1: # Jogador jogou papel.
        print('Eu venci! Tesoura corta papel')

    elif jogador == 2: # Jogador jogou tesoura.
        print ('Poxa! Empatou.')

    elif jogador == 3: # Jogador jogou largato.
        print ('Eu venci! Tesoura decapita largato.')

    elif jogador == 4: # Jogador jogou Spock.
        print ('Cê venceu! Spock esmaga tesoura.')

    else: 
        print ('JOGADA INVÁLIDA!')


    if computador == 3: # Computador jogou lagarto.
        if jogador == 0: # Jogador jogou pedra.
            print ('Você venceu! Pedra esmaga largato.') 

        elif jogador == 1: # Jogador jogou papel.
            print ('Eu venci! Largato come papel.') 

        elif jogador == 2: # Jogador jogou tesoura.
            print ('Cê venceu! Tesoura decapita largato.') 

        elif jogador == 3: # Jogador jogou largato.
            print ('Que concidência! Empate.')

        elif jogador == 4: # Johador jogou Spock.
            print ('Eu venci! Largato envenena Spock.')

        else:
            print ('JOGADA INVÁLIDA')          


    if computador == 4: # Computador jogou Spock.
        if jogador == 0: # Jogador jogou pedra.
            print ('Eu venci! Spock vaporiza a pedra.')

        elif jogador == 1: # Jogador jogou papel.
            print ('Você venceu! Papel refuta Spock.')

        elif jogador == 2: # Jogador jogou tesoura.
            print ('Eu venci! Spock esmaga tesoura.')

        elif jogador == 3: # Jogador jogou largato.
            print ('Você Venceu! Largato envenena Spock')

        elif jogador == 4: # Jogador jogou Spock.
            print ('Cê leu meus pensametos?!? Empate.')

        else:
            print ('JOGADA INVÁLIDA!')