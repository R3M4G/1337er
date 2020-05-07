# 1337er v1.0
#
# Author: Astitva Nikose
# Contact : z3k31024@protonmail.com
#
#
# Description:
# Convert text to 1337

from huepy import *

# Banner
print (bold(red('''
          11   3333  3333  77777
           1      3     3     7 
           1     33    33    7  
           1      3     3   7   
	  111  3333  3333  7  er       v1.0 by z3k31024  \n''')))

# Main
kinput = input('Text to Convert into 1337:')
my_string = kinput
name = kinput.replace('a', '4').replace('h', '#').replace('e', '3').replace('i', '!').replace('l', '1').replace('t', '7').replace('s', '5').replace('o', '0')
print (bold(green(name)))