import re

def modifier(element):

    a = re.sub('^___[a-z]','',element)
    return a

l = ['___abc','___bnh','___hki','___kli','___ulo']

# print(modifier('___abc'))

k = list(map(modifier,l))
print(k)
# for i in k:
#     print(i)