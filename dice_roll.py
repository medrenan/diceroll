import random
import re
import sys

print('''Os dados devem ser jogados no seguinte formado: xdy
(x e y são inteiros de qualquer valor)

Caso queira sair digite exit.

Boa campanha! ;)

#############################################

''')

while True:
    dice = input('Jogue um dado: ')
    if dice == 'exit':
        sys.exit()

    q = re.findall(r'(\d+)d', dice)
    n = re.findall(r'd(\d+)', dice)

    try:
        result = random.choices(range(1, int(n[0])+1), k=int(q[0]))
    except IndexError:
        print('Dado inválido.\n')
        continue
    print(f'{dice} -> {result}\n.............................................\n')
