"""
Structure:
    1) */** for unpacking into function arguments
    2) */** for wrapping arguments passed to a function
    3) Positional arguments with named arguments only
    4) Only named arguments without positional
    5) Using * to unpack iterable objects into a list / tuple;
    6) */** tricks
    7) Using ** to unpack dictionaries into other dictionaries.

    IMPORTANT: All these manipulations you can do with slices

    link to article: https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them/
"""

from random import randint

# 1) */** for unpacking into function arguments
print('\n1) */** for unpacking into function arguments')

# in this part print - built-in func
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print('arr: ', fruits[0], fruits[1], fruits[2], fruits[3])  # or for-loop realisation
print('arr: ', *fruits)  # best way


def transpose_list(list_of_lists):
    return [list(row) for row in zip(*list_of_lists)]


print('func: ', transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))

date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
    **date_info,
    **track_info,
)
print('using two stars two times in func: ', filename)

# 2) */** for wrapping arguments passed to a function
print('\n2) */** for wrapping arguments passed to a function')


def roll(*dice):
    return sum(randint(1, die) for die in dice)


print('pass arg to func with start: ', roll(4, 4, 4, 20))


def tag(tag_name, **attributes):
    attribute_list = [
        f'{name}="{value}"'
        for name, value in attributes.items()
    ]
    return f'<{tag_name} {" ".join(attribute_list)}>'


print(tag('a', href="http://example.com"))
print(tag('img', height=20, width=40, src="img.jpg"))


# 3) Positional arguments with named arguments only
print('\n3) Positional arguments with named arguments only')

def get_multiple(*keys, dictionary, default=None):
    return [
        dictionary.get(key, default)
        for key in keys
    ]


fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
print(get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown'))

# 4) Only named arguments without positional;
print('\n4) Only named arguments without positional')


def with_previous(iterable, *, fillvalue=None):
    """Yield each iterable item along with the item before it."""
    previous = fillvalue
    for item in iterable:
        yield previous, item
        previous = item


print(list(with_previous([2, 1, 3], fillvalue=0)))

'''
>>> list(with_previous([2, 1, 3], 0))
Traceback (most recent call last):
  File "", line 1, in 
TypeError: with_previous() takes 1 positional argument but 2 were given
'''

# 5) Using * to unpack iterable objects into a list / tuple;
print('\n5) Using * to unpack iterable objects into a list / tuple;')

fruits = ['lemon', 'pear', 'watermelon', 'tomato']
first, second, *remaining = fruits
print(remaining)

first, *remaining = fruits
print(remaining)

first, *middle, last = fruits
print(middle)

# 6) * / ** tricks
print(" 6) * / ** tricks (SEE IN CODE)")

# change it (bad)
def palindromify(sequence):
    return list(sequence) + list(reversed(sequence))

# to this (best)
def palindromify(sequence):
    return [*sequence, *reversed(sequence)]

def rotate_first_item(sequence):
    return [*sequence[1:], sequence[0]]


# 7) Using ** to unpack dictionaries into other dictionaries.
print('\n7) Using ** to unpack dictionaries into other dictionaries.')

event_info = {'year': '2020', 'month': '01', 'day': '7', 'group': 'Python Meetup'}
new_info = {**event_info, 'day': "14"}

print(new_info)