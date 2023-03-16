from random import randint 
itens = ('Pedra', 'Papel', 'Tesoura', 'Largato', 'Spork')
computador = randint(0, 4)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] LARGATO
[ 4 ] SPORK''')
jogador = int(input('Qual é a sua jogada?'))
print('-=' * 10)
print ('Computador jogou {}'.format(itens[computador]))
print ('Jogadou jogou {}'.format(itens[jogador]))
print('-=' * 10)