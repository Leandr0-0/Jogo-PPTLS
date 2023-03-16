# REGRAS DO JOGO:
# Pedra esmaga tesoura e largato;
# Papel cobre pedra e refuta Spock;
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
print ('Computador jogou {}'.format(itens[computador]))
print ('Jogadou jogou {}'.format(itens[jogador]))
print('-=' * 12)


if computador == 0: # Computador jogou pedra.
    if jogador == 0: # Jogador jogou pedra.
        print ('EMPATOU!')
    
    elif jogador == 1: # Jogador jogou papel.
        print ('JOGADOR VENCEU!')
        
    elif jogador == 2: # Jogador jogou tesoura.
        print ('COMPUTADOR VENCEU!')

    elif jogador == 3: # Jogador jogou largato.
        print('COMPUTADOR VENCEU!')

    elif jogador == 4: # Jogador jogou Spock.
        print ('JOGADOR VENCEU!')

    else: 
        print ('JOGADA INVÁLIDA!')


if computador == 1: # Computador jogou papel.
    if jogador == 0: # Jogador Jogou pedra.
        print ('COMPUTADOR VENCEU!')

    elif jogador == 1: # Jogador jogou pepel.
        print ('EMPATOU!')

    elif jogador == 2: #Jogador jogou tesoura.
        print ('JOGADOR VENCEU!')

    elif jogador == 3: # Jogador jogou largato.
        print ('JOGADOR VENCEU')

    elif jogador == 4: # Jogador jogou Spork.
        print ('COMPUTADOR VENCEU!')

    else:
        print ('JOGADA INVÁLIDA!')


if computador == 2: # Computador jogou tesoura.
    if jogador == 0: # Jogador jogou pedra.
        print ('JOGADOR VENCEU!')

    elif jogador == 1: # Jogador jogou papel.
        print('COMPUTADOR VENCEU!')

    elif jogador == 2: # Jogador jogou tesoura.
        print ('EMPATOU!')

    elif jogador == 3: # Jogador jogou largato.
        print ('COMPUTADOR VENCEU!')

    elif jogador == 4: # Jogador jogou Spock.
        print ('JOGADOR VENCEU!')

    else: 
        print ('JOGADA INVÁLIDA!')


    if computador == 3: # Computador jogou lagarto.
        if jogador == 0: # Jogador jogou pedra.
            print ('JOGADOR VENCEU!') 

        elif jogador == 1: # Jogador jogou papel.
            print ('COMPUTADOR VENCEU!') 

        elif jogador == 2: # Jogador jogou tesoura.
            print ('JOGADOR VENCEU!') 

        elif jogador == 3: # Jogador jogou largato.
            print ('EMPATOU!')

        elif jogador == 4: # Johador jogoiu Spock.
            print ('COMPUTADOR VENCEU!')

        else:
            print ('JOGADA INVÁLIDA')             

    

    