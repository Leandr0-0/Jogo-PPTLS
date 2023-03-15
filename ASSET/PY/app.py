from random import randint 
itens = ('Pedra', 'Papel', 'Tesoura', 'Largato', 'Spork')
computador = randint(0, 4)
print ('O computador escolheu {}'.format(itens[computador]))