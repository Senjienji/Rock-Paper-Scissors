moves = ("Rock", "Paper", "Scissors")
p1 = moves.index(input("Please select a move: ").capitalize())
p2 = __import__("random").randrange(0, len(moves))

if p1 - p2 in (-2, 1):
    print("Win!")
elif p1 - p2 in (-1, 2):
    print("Lose!")
else:
    print("Tie!")
print(f"{moves[p1]} | {moves[p2]}")

"""
Rock & Paper: Lose -1
Rock & Scissors: Win -2
Paper & Rock: Win 1
Paper & Scissors: Lose -1
Scissors & Rock: Lose 2
Scissors & Paper: Win 1
"""