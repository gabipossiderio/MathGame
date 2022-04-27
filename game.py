from models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


print("WELCOME TO THE COOLEST MATH GAME YOU'VE EVER SEEN".center(100, '#'))


def play(points: int) -> None:
    difficulty: int = int(input('\nChoose the difficulty level (1 - 4): '))

    calc: Calculate = Calculate(difficulty)

    print('\nEnter the result of the operation below: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_results(result):
        points += 1
        print(f'\nYou have {points} points.')

    keep_going: int = int(input('\nDo you want to continue in the game? (1 - YES, 0 - NO): '))

    if keep_going == 1:
        play(points)
    elif keep_going == 2:
        print(f'\nYou finished with {points} points.')
        print('See you later! :)')
    else:
        raise ValueError('Please, enter a valid number.')


if __name__ == '__main__':
    main()
