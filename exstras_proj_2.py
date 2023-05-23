#ex 1.1.2
import string
import tkinter
from functools import reduce
from tkinter import ttk

import winsound


def double_letter(my_str):
    return ''.join(ch * 2 for ch in my_str)

#ex 1.1.3
def four_dividers(n):
    return [x for x in range(1, n+1) if x % 4 == 0]

#ex 1.1.4
def sum_of_digits(n):
    return reduce(lambda x, y: int(x) + int(y), str(n))

#ex 1.3.1
def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))

#ex 1.3.2
def is_prime(n):
    return n > 1 and reduce(lambda acc, val: acc and bool(n % val), range(2, int(n), True))

#ex 1.3.3
def is_funny(s):
    return reduce(lambda acc, char: acc and (char == 'h' or char == 'a'), s, True)

#ex 1.3.4
def figure(password):
    return ''.join(list(map(lambda l: chr((ord(l) - ord('a') + 2) % 26 + ord('a')) if l not in string.punctuation and l != ' ' else l,password)))

#ex 2.2.2
class Dog:
    _count_animals = 0

    def __init__(self, age, name="Octavio"):
        self._name = name
        self._age = age
        Dog._count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    @classmethod
    def get_count_animals(cls):
        return cls._count_animals


#ex 2.3.4
class Pixel:

    def __init__(self):
        self._x = 0
        self._y = 0
        self._red = 0
        self._green = 0
        self._blue = 0

    def __init__(self, x, y, red):
        self._x = x
        self._y = y
        self._red = red
        self._green = 0
        self._blue = 0

    def set_coordinates(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        color = f'({self._red}, {self._green}, {self._blue})'
        if self._red == 0 and self._green == 0 and self._blue > 50:
            color += ' Blue'
        elif self._red == 0 and self._blue == 0 and self._green > 50:
            color += ' Green'
        elif self._green == 0 and self._blue == 0 and self._red > 50:
            color += ' Red'
        print(f'X: {self._x}, Y: {self._y}, Color: {color}')


# ex 2.4.2
class BigThing:
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        if isinstance(self._thing, (int, float)):
            return self._thing
        else:
            return len(self._thing)


class BigCat(BigThing):
    def __init__(self, thing, weight):
        super().__init__(thing)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        else:
            return "OK"


#ex 3.1.3
def raise_stop_iteration():
    i = iter([71, 92, 53])
    next(i)
    next(i)
    next(i)
    next(i)


def raise_zero_division_error():
    a = 1
    b = 0
    c = a / b


def raise_assertion_error():
    x = 10
    y = 5
    assert x < y, "AssertionError: x is not less than y"


#def raise_import_error():
     #import non_existent_module


def raise_key_error():
    my_dict = {"key": "value"}
    print(my_dict["non_existent_key"])


# def raise_syntax_error():
#     len('hello') = 5


# def raise_indentation_error():
#         print("IndentationError function")
#             print("IndentationError function - IndentationError")


def raise_type_error():
    a = "5"
    b = 2
    c = a + b

#ex 3.2.5
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return f"__CONTENT_START__\n{content}__CONTENT_END__\n"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__\n"

# ex 3.3.2
class UnderAge(Exception):
    def __str__(self):
        return "Your age is less than 18. You're only " + str(
            self.args[0]) + " years old. Come back in a few years for Ido's birthday."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should invite " + name)
    except UnderAge as e:
        print(e)


#ex 4.1.2
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return ' '.join(words.get(word, word) for word in sentence.split())


#ex 4.1.3
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_primes(start):
    current = start
    while True:
        if is_prime(current):
            yield current
        current += 1


def first_prime_over(n):
    primes = generate_primes(n + 1)
    return next(primes)


#ex 4.2.2
def parse_ranges(ranges_string):
    # First generator: split ranges string and convert ranges to (start, stop) tuples
    range_tuples = ((start, stop) for start, stop in (range_str.split('-') for range_str in ranges_string.split(',')))

    # Second generator: generate all numbers in each range
    numbers = (num for start, stop in range_tuples for num in range(int(start), int(stop) + 1))

    return numbers


#ex 4.3.4
def get_fibo():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second

#ex 5.1.2
def sing():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    all_the = notes.split('-')
    print(type(all_the))
    print(all_the)
    for item in all_the:
        both = item.split(',')
        frequency = freqs[both[0]]
        duration = int(both[1])
        winsound.Beep(frequency, duration)


#ex 5.2.2
def good():
    numbers = iter(list(range(1, 101, 3)))
    for i in numbers:
        print(i)


#ex 5.3.2
class MusicNotes:
    def __init__(self):
        self._notes = {
            'La': [55, 110, 220, 440, 880],
            'Si': [61.74, 123.48, 246.96, 493.92, 987.84],
            'Do': [65.41, 130.82, 261.64, 523.28, 1046.56],
            'Re': [73.42, 146.84, 293.68, 587.36, 1174.72],
            'Mi': [82.41, 164.82, 329.64, 659.28, 1318.56],
            'Fa': [87.31, 174.62, 349.24, 698.48, 1396.96],
            'Sol': [98, 196, 392, 784, 1568]
        }
        self._notes_list = []
        for octave in range(5):
            for note in self._notes:
                self._notes_list.append((note, octave))
        self._index = 0
        self._max_index = len(self._notes_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._max_index:
            note, octave = self._notes_list[self._index]
            freq = self._notes[note][octave]
            self._index += 1
            return freq
        else:
            raise StopIteration


#ex 6.1.3
def gui():
    # Let's create the Tkinter window
    window = tkinter.Tk()
    window.title("GUI")
    tkinter.Label(window, text="What do I like the most?", font=("Arial", 14), fg="red").pack()

    # creating a function called DataCamp_Tutorial()
    def DataCamp_Tutorial():
        label = tkinter.Label(window, text="This is what I like:")
        label.pack()
        image = tkinter.Image.open(r'C:\Users\user\Desktop\sigitDana\yumi.jpg')
        photo_image = ImageTk.PhotoImage(image)
        image_label = ttk.Label(window, image=photo_image)
        image_label.image = photo_image  # store a reference to the image to prevent garbage collection
        image_label.pack()

    tkinter.Button(window, text="Click Me to find out !", command=DataCamp_Tutorial).pack()
    window.mainloop()


#ex 6.3.3
def text_to_speech():
    import pyttsx3

    # The text that you want to convert to speech
    my_text = "first time i'm using a package in next.py course"

    # Initialize the Text-to-speech engine
    engine = pyttsx3.init()

    # Set the speed of speech
    engine.setProperty('rate', 150)

    # Convert text to speech
    engine.say(my_text)

    # Play the speech
    engine.runAndWait()

