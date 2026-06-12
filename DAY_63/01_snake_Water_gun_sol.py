#  here we use 2-D matrix logic
#       comp -> 0   1   2
# player 0      D   W   L
#        1      L   D   W
#        2      W   L   D


from random import randint

choices = ["Snake", "Water", "Gun"]

result = [
    ['Draw', 'Won', 'Lose'],
    ['Lose', 'Draw', 'Won'],
    ['Won', 'Lose', 'Draw']
]

player = int(input("0=Snake, 1=Water, 2=Gun: "))
computer = randint(0, 2)

print(f"Player: {choices[player]}")
print(f"Computer: {choices[computer]}")
print(result[player][computer])