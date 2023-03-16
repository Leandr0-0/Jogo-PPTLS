# REGRAS DO JOGO:
# Pedra esmaga tesoura e largato;
# Papel cobre pedra e refuta Spock;
# Tesoura corta papel e decapita largato;
# Largato come papel e envenena Spock;
# Spock esmaga tesoua e vaporiza papel.

# RESUMO:
# Pedra > Tesoura e Largato;
# Papel > Pedra e Spock;
# Tesoura > Papel e Largato;
# Largato > Papel e Spock;
# Spock > Pedra e Tesoura.

from random import randint 
itens = ('Pedra', 'Papel', 'Tesoura', 'Largato', 'Spork')
computador = randint(0, 4)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] LARGATO
[ 4 ] SPOCK''')
jogador = int(input('Qual é a sua jogada?'))
print('-=' * 10)
print ('Computador jogou {}'.format(itens[computador]))
print ('Jogadou jogou {}'.format(itens[jogador]))
print('-=' * 10)