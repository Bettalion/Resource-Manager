import os
import random
from time import sleep as ts
from datetime import date

def main():
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

  ChosenS = int(input('Which would you like to revise from?'))
  if int(ChosenS) > len(RevisionMedia) or int(ChosenS) < 0 :
    print('Invalid input')  
  # ChosenS  =2

  links=[]
  print(f'\n{RevisionMedia[ChosenS-1][0]}')
  for topic in range(1,len(RevisionMedia[ChosenS-1])):
    topicN,topicL= RevisionMedia[ChosenS-1][topic].split('~')
    links.append([topicN,topicL])
    print(f'{topic}.  {topicN}')

  ChosenT  = int(input('Which would you like to use?'))-1
  if int(ChosenT) >= len(links) or int(ChosenT) < 0:
    print('Invalid input') 
    quit()
  # ChosenT= 1


  print(f'\nYou have chosen:{links[ChosenT][0]}\nYou will be redirected to {links[ChosenT][1]}')

  ts(2.5)
  
  s = RevisionMedia[ChosenS-1][0].split(':')[0]
  log=f'{s} >>> {links[ChosenT][0]} >> {links[ChosenT][1]}'

  dates = date.today().strftime("%m/%d/%y")
  os.chdir('/Users/amoghsimhadri/BettalionFolder/Scrap')
  try:
    open('ResourcePicked.txt','a').write(f'The resource searched to study/revise on {dates}: {log}\n')
  except:
    open('ResourcePicked.txt','w').write(f'The resource searched to study/revise on {dates}: {log}\n')
  try:
    os.system(f"open \"\" {links[ChosenT][1]}")
  except:
    os.system(f"open \"\" https://{links[ChosenT][1]}")


if __name__ == "__main__":
    print('\nWelcome to the Resource Finder!\n')
    main()

    
  