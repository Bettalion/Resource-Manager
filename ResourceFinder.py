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


Sources = [s[0] for s in RevisionMedia] 


