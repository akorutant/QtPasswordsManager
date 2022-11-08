import random

from constants import UPPER_SYMBOLS, LOWER_SYMBOLS, SPECIAL_SYMBOLS, NUMBERS


# Класс генератора паролей.
class PasswordGenerator:
    def __init__(self,
                 special_symbols: bool = False,
                 numbers: bool = False,
                 length: int = 0
                 ):
        self.special_symbols = special_symbols
        self.numbers = numbers
        self.length = length
        self.symbols = None
        self.password = ''

    # Фукнция генерации.
    def generate(self) -> str:
        try:
            # Проверка условий для генерации пароля.
            if not self.special_symbols and not self.numbers:
                self.symbols = list(UPPER_SYMBOLS + LOWER_SYMBOLS)
            elif self.special_symbols and not self.numbers:
                self.symbols = list(UPPER_SYMBOLS + LOWER_SYMBOLS + SPECIAL_SYMBOLS)
            elif not self.special_symbols and self.numbers:
                self.symbols = list(UPPER_SYMBOLS + LOWER_SYMBOLS + NUMBERS)
            elif self.special_symbols and self.numbers:
                self.symbols = list(UPPER_SYMBOLS + LOWER_SYMBOLS + NUMBERS + SPECIAL_SYMBOLS)

            # Генерация пароля.
            for i in range(self.length):
                self.password += random.choice(self.symbols)
            return self.password
        except Exception as error:
            return error
