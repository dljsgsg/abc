def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)



result = gcd(48, 18)
print(result)
#2
import random

def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = digits[:4]
    return secret_number

def count_bulls_and_cows(secret_number, guess, index=0, bulls=0, cows=0):
    if index == 4:
        return bulls, cows
    if guess[index] == secret_number[index]:
        bulls += 1
    elif guess[index] in secret_number:
        cows += 1
    return count_bulls_and_cows(secret_number, guess, index+1, bulls, cows)

def play_bulls_and_cows(secret_number, attempts=1):
    guess = input("Введите ваше четырёхзначное число: ")
    if len(guess) != 4 or not guess.isdigit():
        print("Пожалуйста, введите четырёхзначное число.")
        play_bulls_and_cows(secret_number, attempts)
    else:
        guess_digits = [int(digit) for digit in guess]
        bulls, cows = count_bulls_and_cows(secret_number, guess_digits)
        if bulls == 4:
            print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
        else:
            print(f"{bulls} бык(ов), {cows} коров(ы)")
            play_bulls_and_cows(secret_number, attempts+1)

def main():
    print("Добро пожаловать в игру 'Быки и коровы'!")
    secret_number = generate_secret_number()
    play_bulls_and_cows(secret_number)

main()
#3
def is_valid_move(board, x, y):
    if x >= 0 and x < 8 and y >= 0 and y < 8 and board[x][y] == -1:
        return True
    return False

def print_board(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()

def knight_tour(n, board, x, y, move_x, move_y, pos):
    if pos == n**2:
        print_board(board)
        return True
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_valid_move(board, next_x, next_y):
            board[next_x][next_y] = pos
            if knight_tour(n, board, next_x, next_y, move_x, move_y, pos+1):
                return True
            board[next_x][next_y] = -1
    return False

def main():
    n = 8
    board = [[-1 for _ in range(n)] for _ in range(n)]
    start_x = int(input("Введите начальную координату X (от 0 до 7): "))
    start_y = int(input("Введите начальную координату Y (от 0 до 7): "))
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[start_x][start_y] = 0
    if not knight_tour(n, board, start_x, start_y, move_x, move_y, 1):
        print("Нет возможного пути для заданных координат.")

main()