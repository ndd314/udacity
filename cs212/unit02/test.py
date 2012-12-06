import string, re

print ''.join(set(list('xy=zz')))

print re.findall('[a-z]', 'xyzz=')

f = lambda Y,M,E,U,O: (1*U+10*O+100*Y)==(1*E+10*M)**2

print f(2,1,7,9,8)

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    exp = '('
    for idx, val in enumerate(reversed(list(word))):
        exp += '10**%d*%s+' % (idx, val)
    exp += '0)'
    return exp

print compile_word('lower')