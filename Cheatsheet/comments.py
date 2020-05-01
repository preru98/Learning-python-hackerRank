#Single line
#now multiline

def myFunction():
    """
    This is function docstring
    """
print (myFunction.__doc__)

name=input()
print('Nice to meet you, {}'.format(name))    
print('Nice to meet you, {}'.format('prerna'))
print('let me say hello to all the {}, {}, {}, and {}s present in the party.'.format('puppers','mews','moohs',name))

print(len('henlo'))
print(len(name))

if 'henlo':
    print('Not empty')
else:
    print('Not empty')


if name:
    print('no empty input')
else:
    print('empty input')