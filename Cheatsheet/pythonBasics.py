#Highest to lowest precedence of operators
#
#   Exponent          | **
#   Modulus           | %
#   Integer Division  | //
#   Division          | /
#   Multiplication    | *
#   Subtraction       | -
#   Addition          | +
#

import sys
a='exit'
while True:
    if a is 'exit':
        print('Aborting :<')
        sys.exit()
    print('Not aborting this time :)')


a=34
b='678'
c=7.7
d='9'
print('{} | {} | {} | {} |{} |'.format(str(a),int(b),float(b),int(c),str(d)))

e=9.0
if int(d)==e:
    print('true')

print(True is True)
print(True is not False)

# for loop
# for i in range(10):
#     print('{}'.format(str(i)))

#range function (start value, stop value, updation)

for i in range(5,10,1):
    print('{}'.format(str(i)))

for i in range(-5,-10,-1):
    print('{}'.format(str(i)))
    if i==-7:
        break
    
else:
    print('Full loop executed, no breaks :)') #Wont execute in this case 
