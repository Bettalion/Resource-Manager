import os
import random

f=open('/Users/amoghsimhadri/BettalionFolder/cx/Resource-Manager/My Resources','r')
data=f.read().split('\n')
if len(data) == 0:
  print('Invalid Data!')
  quit()


RevisionMedia = []
temp = []

i = 0 # index
while i <len(data):
  if data[i] != '':
   temp.append(data[i])
  else:
    RevisionMedia.append(temp)
    temp=[]
  i+=1
RevisionMedia.append(temp)


Sources = [(s+1,RevisionMedia[s][0].split(':')[0].capitalize()) for s in range(len(RevisionMedia))]
sourceDict={}
for source in Sources:
 sourceDict[source[0]]= source[1]
 print(f'{source[0]}) {source[1]}')


