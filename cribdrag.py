#!/usr/bin/python

""" Notes on One-time pad
    =====================
From wikipedia:
- a plaintext is paired with a random secret key (one-time pad)
- each bit/char of the plaintext is encrypted by combining it 
with the corresponding bit/char from the pad using XOR operation 


ctext0 & ctext1 are the ciphertexts

"""

def xor(a, b):
    #input: two bytearrays
    #output: bytearray of their xor
    if len(a) > len(b):
        temp = a
        a = b
        b = temp
    s = []
    for i in range(0, len(a)):
        s.append(a[i] ^ b[i])
    for i in range(len(a), len(b)):
        s.append(b[i])
    return s

def cribpend(a, crib, loc):
    #crib is too small; append it with 0's depending on location
    s = []
    for i in range(0, loc):
        s.append(0)
    for i in range(0, len(crib)):
        s.append(crib[i])
    for i in range(len(crib) + loc, len(a)):
        s.append(0)
    s = s[:len(a)]
    return s

def bit(a):
    #returns bitstring of integer
    # put in int, gives you the bit
    s = ""
    while (a != 0):
        if (a % 2 == 0):
            s += "0"
            a /= 2
        else:
            s += "1"
            a -= 1
            a /= 2
    while len(s) < 8:
        s += "0"
    s = s[::-1]
    return s

def s_to_ints(s):
    #convert string to integer list ("bytearray")
    b = []
    for i in range(0, len(s)):
        b.append(ord(s[i]))
    return b
    

def showbytes(a):
    s = ""
    chars = []
    for i in range(65, 91):
        chars.append(i)
    for i in range(97, 123):
        chars.append(i)
    for i in range(44, 47):
        chars.append(i)
    #return string of bytestring
    for i in range(0, len(a)):
        if (a[i] in chars):
            s += chr(a[i])
        elif (a[i] == 0):
            s += " "
        elif (a[i] == 32):
            s += "_"
        else:
            s += "*"
    return s


import random
import sys
import os

# c1 = open("ctextsample0")

with open('citext0', 'r') as c1text:
	c1 = c1text.readlines()
with open('citext1', 'r') as c2text:
	c2 = c2text.readlines()


#print c1


# guess a word that might appear in one of the messages
guess = "The history of br"
# encode word to byte
# ord() each character of your guess

str_guess = ""

for letter in guess:
	integer = ord(letter)		# given a string, return an int representing the Unicode code point of that char
					# ex: ord('t') gives 116
	integer = bit(integer)		# use the bit function to convert to bits
					# ex: 116 -> 01110100
	str_guess += str(integer)	# convert in to string and concatenate to get guess bitarray

# XOR the cipher texts
str_1 = ""
str_2 = ""

# Turn c1 and c2 into bytearrays, stored in str_1 and str_2

list1 = []
list2 = []
for word in c1:
	my_list = [ord(c) for c in word]
	list1 = list1 + my_list	

for word in c2:
	my_list = [ord(c) for c in word]
	list2 = list2 + my_list

bit_c1 = ""
bit_c2 = ""
for num in list1:
	bit_c1 += bit(num)

for num in list2:
	bit_c2 += bit(num)

# result is the xor of the c1 & c2 bytearrays

result = xor(s_to_ints(bit_c1), s_to_ints(bit_c2))

temp_string = ""
for i in result:
	temp_string += str(i)
	
x = len(bit_c1) * 8
y = x - len(str_guess)
output_str = ""	
		
for i in range(0, y/8):
	temp2_guess = ""

	if i%8 == 0:
		temp_guess = str_guess
		temp_guess =  cribpend(temp_string, temp_guess, i)
		for j in temp_guess:
			temp2_guess += str(j)
		temp_xor = xor(s_to_ints(temp_string), s_to_ints(temp2_guess))	
		temp_str2 = ""


		for k in temp_xor:
			temp_str2 += str(k)
	
		for l in range(0,399):
			eight_str = ""
			eight_str += temp_str2[l*8:(l+1)*8]
			output_str += chr(int(eight_str, 2))
		print "I VALUE = " + str(i) + "\n"
		print output_str
		output_str = ""
