#-------------------------------------------------------Unit1---------------------------------------------------------
import string


def max_word_in_file():
    with open(r'C:\Users\benaz\Documents\names.txt') as file_input: print(
        max((line.strip() for line in file_input), key=len))

def sum_lengths():
    with open(r'C:\Users\benaz\Documents\names.txt') as file_input: print(
        sum(len(line.strip()) for line in file_input))

def min_word_in_file():
    with open(r'C:\Users\benaz\Documents\names.txt') as f:
        lines = [line.strip() for line in f]
        shortest_length = len(min(lines, key=len))
        list(map(lambda line: print(line), filter(lambda line: len(line) == shortest_length, lines)))

def lengths_file():
    with open(r'C:\Users\benaz\Documents\names.txt') as f, open(
            r'C:\Users\benaz\Documents\names.txt', 'w') as out_f:
        out_f.writelines(str(len(line.strip())) + "\n" for line in f)

def names_in_len():
    name_length = int(input("Enter name length: "))
    with open(r'C:\Users\benaz\Documents\names.txt') as f:
        list(
            map(lambda line: print(line.strip()), filter(lambda line: len(line.strip()) == name_length, f.readlines())))


#---------------------------------------------------------Unit2-------------------------------------------------------------
class Animal:
    zoo_name = "Hayaton"  # Shared attribute for all animal instances

    def __init__(self, name, hunger=0):
        self.name = name
        self.hunger = hunger

    def get_name(self):
        return self.name

    def is_hungry(self):
        return self.hunger > 0

    def feed(self):
        if self.is_hungry():
            self.hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeow")


class Skunk(Animal):
    def talk(self):
        print("tssssss")

    def stink(self):
        print("Dear Lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good morning, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    for animal in zoo_lst:
        print(animal.get_name())
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
        print()

    print(Animal.zoo_name)


#if __name__ == '__main__':
    #main()

#---------------------------------------------------------------Unit3--------------------------------------------------------

class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_char, index):
        self._message = f"The username contains an illegal character '{illegal_char}' at index {index}"
        super().__init__(self._message)
        self._illegal_char = illegal_char
        self._index = index


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username consists of less than 3 characters"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username consists of more than 16 characters"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The username consists of less than 8 characters"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The username consists of more than 40 characters"


def check_input(username, password):
    try:
        if not is_valid_username(username):
            for index, c in enumerate(username):
                if c not in string.ascii_letters + string.digits + '_':
                    raise UsernameContainsIllegalCharacter(c, index)
            raise UsernameTooShort() if len(username) < 3 else UsernameTooLong()

        if not is_valid_password(password):
            if not any(char.isupper() for char in password):
                raise PasswordMissingUppercase()
            elif not any(char.islower() for char in password):
                raise PasswordMissingLowercase()
            elif not any(char.isdigit() for char in password):
                raise PasswordMissingDigit()
            elif not any(char in string.punctuation for char in password):
                raise PasswordMissingSpecial()
            raise PasswordTooShort() if len(password) < 8 else PasswordTooLong()

        print("OK")
    except Exception as e:
        print(e)


# check if the username valid
def is_valid_username(username):
    legal_chars = string.ascii_letters + string.digits + '_'

    # Check username length
    if len(username) < 3 or len(username) > 16:
        return False

    # Check if all chars are legal
    for c in username:
        if c not in legal_chars:
            return False

    # If all checks pass, return True
    return True


# check if the username valid
def is_valid_password(password):
    # Check password length
    if len(password) < 8 or len(password) > 40:
        return False

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if password contains at least one special character
    if not any(char in string.punctuation for char in password):
        return False

    # If all checks pass, return True
    return True


def main():
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")


#if __name__ == '__main__':
    #main()

#-----------------------------------------------------------Unit4------------------------------------------------------------
from datetime import datetime

def gen_secs():
    """Generator that yields all possible seconds ranges (0-59) - seconds"""
    for s in range(60):
        yield s

def gen_minutes():
    """Generator that yields all possible seconds ranges (0-59) - minutes"""
    for s in range(60):
        yield s

def gen_hours():
    """Generator that yields all possible seconds ranges (0-59) - hours"""
    for s in range(24):
        yield s

def gen_time():
    """Generator that yields all possible times (hour:minutes:second)"""
    for h in gen_hours():
        for m in gen_minutes():
            for s in gen_secs():
                yield "%02d:%02d:%02d" % (h, m, s)

def gen_years(start=datetime.now().year):
    """Generator that yields all possible years from given year"""
    year = start
    while True:
        yield year
        year += 1

def gen_months():
    """Generator that yields all the months"""
    for m in range(1, 13):
        yield m

def gen_days(month, leap_year=True):
    """Generator that yields the number of days in a given month"""
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31,
        4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    days = days_in_month[month]
    return (x for x in range(1, days + 1))

def gen_date():
    for year in gen_years():
        # Check if the current year is a leap year
        for month in gen_months():
            # the number of days depend on the given mouth
            for day in gen_days(month, leap_year=(year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield " {}/{}/{} {:02d}:{:02d}:{:02d}".format(day, month, year, hour, minute, second)


# def main():
#     fun = gen_date()
#     for i in range(1000000):
#         print(next(fun))
#
#
# if __name__ == '__main__':
#     main()

#---------------------------------------------------Unit5-----------------------------------------------------------------------
from functools import reduce

def check_id_valid(id_number):
    number_list = [int(d) for d in str(id_number)]
    step_one_list = [x * 1 if i % 2 == 0 else x * 2 for i, x in enumerate(number_list)]
    step_two_list = [x % 10 + x // 10 if x > 9 else x for x in step_one_list]
    sum_list = reduce(lambda n, x: n + x, step_two_list)

    return sum_list % 10 == 0


def id_generator(start_id):
    for i in range(start_id, 1000000000):
        if check_id_valid(i):
            yield i


class IDIterator:
    def __init__(self, start_id):
        self._id = int(start_id)
        self._current_id = self._id - 1

    def __iter__(self):
        return self

    def __next__(self):
        self._current_id += 1
        while not check_id_valid(self._current_id):
            self._current_id += 1
        if self._current_id > 999999999:
            raise StopIteration
        return self._current_id


def print_using_gen(input_id):
    print("\nID from generator---->")
    gen = id_generator(int(input_id))
    for i in range(10):
        print(str(next(gen)))


def print_using_it(input_id):
    id_iter = IDIterator(int(input_id))
    print("\nID from iterator---->")
    for i in range(10):
        print(str(next(id_iter)))


def wanted_print(input_id, print_way):
    if print_way == 'it':
        print_using_it(input_id)
    else:
        print_using_gen(input_id)


# def main():
#     input_id = input("Enter ID: ")
#     print_way = input("Generator or Iterator? (gen/it)? ")
#     wanted_print(input_id, print_way)
#
#
# if __name__ == '__main__':
#     main()

#--------------------------------------------Unit6------------------------------------------------------------------------
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt


def main():
    first = (
        146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
        355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
        178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
        307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
        199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
        389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
        216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
        365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
        215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
        290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
        279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
        291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
        306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
        393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
        336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
        259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
        349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
        234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
        339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
        122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
        214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
        134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
        171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
        115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
        89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108,
        132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149,
        77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111,
        156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259,
        136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153,
        366, 149, 379, 147, 394, 146, 399
    )
    second = (
        156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186,
        150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175,
        159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146,
        218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172,
        114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81,
        162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126,
        113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157,
        128, 156, 134, 157, 136, 156, 136
    )
    image = Image.open("pic.jpg")
    draw = ImageDraw.Draw(image)
    draw.line(first, fill="orange")
    draw.line(second, fill="orange")
    # fill the object
    draw.polygon(first, fill=(255, 0, 0, 128))

    plt.imshow(image)
    plt.show()

#
# if __name__ == '__main__':
#     main()