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
for source in Sources:
 print(f'{source[0]}) {source[1]}')

# ChosenS = int(input('\nWhich would you like to revise from?'))
# if int(ChosenS) > len(RevisionMedia) or int(ChosenS) < 0 :
#   print('Invalid input')  
ChosenS  =1

links=[]
print(f'\n{RevisionMedia[ChosenS-1][0]}')
for topic in range(1,len(RevisionMedia[ChosenS-1])):
  topicN,topicL= RevisionMedia[ChosenS-1][topic].split('-')
  links.append(topicL)
  print(f'{topic}.  {topicN}')



# os.system("open \"\" https://example.com")