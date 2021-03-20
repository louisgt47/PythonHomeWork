N = int(input())
S = list(input())
New = ''
ELetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in S:
  New = New + ELetter[ELetter.index(i)+N]
print(New)
