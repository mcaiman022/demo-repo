# from collections import Counter, defaultdict, OrderedDict
#
# li = [1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 7]
#
# # print(Counter(li))
#
# sentence = 'blah blah blah thinking about python'
#
# print(Counter(sentence))


# from datetime import *
# from time import *
#
# print(date.today())
# t1 = time()
#
# t2 = time()
#
# print(t1)
#
# print(t2)

'''Debugging'''
import translate

# import pdb
#
#
# def add(num1, num2):
#     # pdb.set_trace()
#     return num1 + num2
#
#
# print(add(4, 5))


'''File I/O (Input/Output)'''

# my_file = open("c:/users/support/desktop/1.txt")
#
# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# # print(my_file.read())
# print(my_file.readlines())

#
# my_file.close()
# try:
#     with open("c:/users/support/desktop/3.py", mode='r') as my_file:
#         text = my_file.read()
#         print(text)
#
# except FileNotFoundError as err:
#     print('nonono')
# except IOError as err:
#     with open("c:/users/support/desktop/3.py", mode='w') as my_file:
#         text = my_file.write('Ok')
#         print(text)


# with open("../4.py", mode='w') as my_file:
#     text = my_file.write('ggg')
#     print(text)
#     # print(my_file.readlines())

from translate import Translator


translator = Translator(to_lang="zh")
translator2 = Translator(to_lang="ja")

try:
    with open("c:/users/support/desktop/3.txt", mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate("This is a pen.")
        translation2 = translator2.translate(text)

        print(translation)
        print(translation2)

except FileNotFoundError as e:
    print('Check your file bobo')

