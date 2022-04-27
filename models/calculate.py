from random import randint


class Calculate:

    def __init__(self: object, difficulty: int) -> None:
        self._difficulty = difficulty
        self._value1: int = self._value_generator
        self._value2: int = self._value_generator
        self._operation: int = randint(1, 3)
        self._result: int = self._result_generator

    @property
    def difficulty(self: object) -> int:
        return self._difficulty

    @property
    def value1(self: object) -> int:
        return self._value1

    @property
    def value2(self: object) -> int:
        return self._value2

    @property
    def operation(self: object) -> int:
        return self._operation

    @property
    def result(self: object) -> int:
        return self._result

    def __str__(self: object) -> str:
        op: str = ''
        if self._operation == 1:
            op = 'Sum'
        elif self._operation == 2:
            op = 'Subtract'
        elif self._operation == 3:
            op = 'Multiply'
        else:
            op = 'Unknown Operation'
        return f'Value 1: {self.value1} \nValue 2: {self.value2} \nDifficulty: {self.difficulty} \nOperation: {op}'

    @property
    def _value_generator(self: object) -> int:
        if self.difficulty == 1:
            return randint(0, 10)
        if self.difficulty == 2:
            return randint(0, 100)
        if self.difficulty == 3:
            return randint(0, 1000)
        if self.difficulty == 4:
            return randint(0, 10000)
        else:
            raise ValueError('Please, enter a difficulty between 0 and 4.')

    @property
    def _result_generator(self: object) -> int:
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            return self.value1 - self._value2
        else:
            return self.value1 * self.value2

    @property
    def _op_simbol(self: object) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        elif self.operation == 3:
            return '*'

    def check_results(self: object, answer: int) -> bool:
        right: bool = False

        if self.result == answer:
            print('\nCongratulations! Right answer!')
            right = True
        else:
            print("\nOh no! Wrong answer. You didn't score.")
        print(f'\nCheck the right answer: {self.value1} {self._op_simbol} {self.value2} = {self.result}')
        return right

    def show_operation(self: object) -> None:
        print(f'{self.value1} {self._op_simbol} {self.value2} = ?')
