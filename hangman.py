import answers
import random

body = ["O", "/", "|", "\\", "/", "\\"]
body_display = [" ", " ", " ", " ", " ", " "]

board = u'\u256D\u2500\u2500\u2500\u2500\u2500\u256E\n' \
        u'\u2502\u0020\u0020\u0020\u0020\u0020%s\n' \
        u'\u2502\u0020\u0020\u0020\u0020%s%s%s\n' \
        u'\u2502\u0020\u0020\u0020\u0020%s\u0020%s\n' \
        u'\u250C\u2500\u2500\u2500\u2500\u2500\u2510\n' \
        u'\u2514\u2500\u2500\u2500\u2500\u2500\u2518' % \
        (body_display[0], body_display[1], body_display[2],
         body_display[3], body_display[4], body_display[5])


def set_board():
    global board
    board = u'\u256D\u2500\u2500\u2500\u2500\u2500\u256E\n' \
            u'\u2502\u0020\u0020\u0020\u0020\u0020%s\n' \
            u'\u2502\u0020\u0020\u0020\u0020%s%s%s\n' \
            u'\u2502\u0020\u0020\u0020\u0020%s\u0020%s\n' \
            u'\u250C\u2500\u2500\u2500\u2500\u2500\u2510\n' \
            u'\u2514\u2500\u2500\u2500\u2500\u2500\u2518' % \
            (body_display[0], body_display[1], body_display[2],
             body_display[3], body_display[4], body_display[5])


words = answers.answers
index = random.randint(0, len(words) - 1)
answer = words[index]
answer_spaces = len(answer)
answer_display = []
wrong_guess = 0

for _ in range(answer_spaces):
    answer_display.append("  ")

while wrong_guess < 6:
    print(board)
    display = ""
    for letter in answer_display:
        display += letter
    print(display)
    print('- ' * answer_spaces)
    guess = input("Guess a letter: ")
    for index in range(answer_spaces):
        if guess.upper() == answer[index]:
            answer_display[index] = answer[index] + " "
    if "  " not in answer_display:
        set_board()
        break
    if guess.upper() not in answer:
        wrong_guess += 1
        body_part = wrong_guess - 1
        body_display[body_part] = body[body_part]
        set_board()

print(board)
display = ""
for letter in answer_display:
    display += letter
print(display)
print('- ' * answer_spaces)
if wrong_guess == 6:
    print("You lose!")
else:
    print("You win!")
