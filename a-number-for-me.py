'''
Generates a Random 74 Digit Number* 

A Number I could have all for myself
https://notes.whoibrar.com/2022/05

*doesn't check for the case when the first digit is zero
'''

import random
print(''.join([str(random.randint(0,9)) for i in range(74)]))
