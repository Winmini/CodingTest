a = input()
print(a.find('a'), a.find('b'), a.find('c'), a.find('d'), a.find('e'),
      a.find('f'), a.find('g'), a.find('h'), a.find('i'), a.find('j'),
      a.find('k'), a.find('l'), a.find('m'), a.find('n'), a.find('o'),
      a.find('p'), a.find('q'), a.find('r'), a.find('s'), a.find('t'),
      a.find('u'), a.find('v'), a.find('w'), a.find('x'), a.find('y'),
      a.find('z'))

a = input()
for i in range(97, 123):
    print(a.find(chr(i)))