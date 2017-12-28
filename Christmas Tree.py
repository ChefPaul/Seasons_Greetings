levels = 20

for i in range(1,18,2):

    if levels % 2 == 0:
        print(' '*levels+i*'*')
        levels=levels-1

    else:
        print(' '*levels+i*'o')
        levels=levels-1

print('  '+' '*levels+1*'Merry Christmas')
