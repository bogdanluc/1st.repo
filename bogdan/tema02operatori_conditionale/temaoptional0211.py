import random

player = int(input('And the dice iiis...  '))
dice_roll = random.randint(1,6)
print(dice_roll)
if player == dice_roll:
    print(f'Ai ghicit. Felicitari! Ai ales {player} si zarul a fost {dice_roll}')
elif player < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {player} dar a fost {dice_roll}')
elif player > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {player} dar a fost {dice_roll}')