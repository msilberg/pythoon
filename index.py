#!/usr/bin/python

# fooTuples = (1, 2, 3, 4, 5)
# print type(fooTuples)
# print (fooTuples)
#
# fooDictionary = {'one': 1, 'two': 2, 'three': 3}
# print type(fooDictionary)
# print (fooDictionary)

# --== Data Type Conversions ==--
# foo = '1'
# print type(foo)
# print (foo)
# foo2 = float(foo)
# print type(foo2)
# print (foo2)
#
# fooDictionary = {'one': 1, 'two': 2, 'three': 3}
# print type(fooDictionary)
# fooDictionary2 = repr(fooDictionary)
# print (fooDictionary2)
# print type(fooDictionary2)

# foo = 1
# print eval("foo + 2")

# --=== ++++ ===--
# fooStr = "spacebuttonisbrokenonmykeyboardsowhatcanido"

# tupleVar = tuple(fooStr)
# print (tupleVar)

# listVar = list(fooStr)
# print (listVar)

# setVar = set(fooStr)
# print setVar

# ** Foreach **
# d1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# d2 = {}
# for k, v in d1.items():
#     d2[k] = v
# ** Dict Way **
# d2 = dict((k, v) for k, v in d1.items())
# print type(d2)
# print (d2)

# fooFrozen = frozenset(fooStr)
# print type(fooFrozen)
# print (fooFrozen)

# ** integer to char **
# foo = 1259
# foo2 = chr(foo)
# foo2 = unichr(foo)
# foo2 = ord(foo)
# print type(foo2)
# print (foo2)

# foo = 10
# foo2 = hex(foo)
# foo2 = oct(foo)
# print type(foo2)
# print (foo2)

# ** Operators **
# a = 8
# b = 3
# print (a ** b)
# print (a // b)
# print (a % b)

# ** Binary **
# a = 60  # 0011 1100
# b = 13  # 0000 1101
# c = 0
#
# print (a & b)
# print (a | b)
# print (a ^ b)

# ** if statement **
# if 4 > 22 or 5 > 3:
#     print ("true")
# else:
#     print ("not true")

# foo = [1, 2, 3, 4, 5]
# if 5 in foo:
#     print ("true")
# else:
#     print ("not true")

# foo = "1"
# foo2 = 1
# if foo2 == foo:
#     print ("true")
# else:
#     print ("not true")

# ** Math **
# import math
# print math.pow(100, 2)
# print math.pi

# ** Random **
# import random
# print random.random()
# print random.randrange(1, 1000)

# ** Strings **
# print "My name's %s, I'm %d years old" % ('Mike', 31)
foo = "this is string example is cute"
# foo2 = "         this is string example         "
# foo3 = "7777777777777this is string example7777777777777"
# foo2 = "     "
# print foo.center(60, ' ')
# print foo.capitalize()
# print foo.encode('base64', 'strict')
# print "ololo" + foo.expandtabs(16)
# print foo.find('is')
# print foo.rfind('is')
# print foo.index('string')
# print foo.isspace()
# print foo2.isspace()

# **** Implode
# delimiter = ','
# arr = ('one', 'two', 'three')
# print delimiter.join(arr)

# **** Explode
# print foo.split(' ')

# print len(foo)

# print foo.ljust(50, 'a')
# print foo.rjust(50, 'a')
# **** trims the string
# print foo2.lstrip()
# print foo3.lstrip('7')
# print foo3.rstrip('7')
# foo3 = foo3.lstrip('7')
# print foo3.rstrip('7')


# **** make trans
# from string import maketrans
# inTab = "i"
# outTab = "7"
# transition = maketrans(inTab, outTab)
# print foo.translate(transition)

# print min(foo)
# print min(foo)

# **** replace
# print foo.replace("example", "motherfucker")

# print foo.upper()
# print foo.zfill(40)

# unicode is decimal
foo4 = u"12345"
print foo4.isdecimal()

