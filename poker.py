import random
import time
players=[]#Зжесь будем держать игроков
stol=[] #карты на нашем столе
print ('Введите колличество игроков от 1 до 9')
x=int(input())
deck=[] #Наша колода 
values=['2','3','4','5','6','7','8','9','10','J','Q','K','A'] #Задаем масти и достонство карт 
suits=['Буби','Червы','Пики','Трефы'] 
 
class Card: #Описывает одну карту как объект 
  def __init__ (self,suit,value): 
      self.suit=suit
      self.value=value 
def gen (): #Генерирует колоду карт 
    global deck 
    for val in values: 
        for su in suits: 
            deck.append(Card(su,val)) #Добавляем в колоду по карте

def otobr (Card): #Функция для отображения карт на экран 
     print (Card.suit,Card.value) 
 

class Player: #создаем класс игроков
  def __init__(self,nomer,karta1, karta2): #инициализируем его
          self.nomer=nomer
          self.karta1=karta1
          self.karta2=karta2
  def otobrpla(nomer): #Метод отображающий игроков
          print ('Номер игрока:',nomer)
          print ('Его карты:')
          otobr(players[nomer].karta1),otobr(players[nomer].karta2)
          print ('____________')
          
def datkart (nomer): #описываем генератор игроков
     global players
     global deck
     karta1=deck.pop()#берем из колоды по карте
     karta2=deck.pop()
     players.append(Player(nomer,karta1,karta2))#добавляем игрока в список игроков
def genstol (kol): #описываем генератор карт на столе
     global deck
     global stol
     for i in range(kol):
          stol.append(deck.pop())
def otobrstol():   #Отображаем наш стол
   global stol
   for  i in stol:
     otobr(i)
   
   
  
gen() 
random.shuffle(deck) # Мешаем колоду
for i in range (x): #Проходимся по всем игрокам 
  datkart (i)#даем карту первому игроку
  Player.otobrpla(i)
print ('Сейчас появится флоп')
time.sleep(3) #Небольшая задержка, чтобы крупье успел раздать карты
genstol (3)
otobrstol()
print ('Сейчас появится терн')
time.sleep(3) #Небольшая задержка, чтобы крупье успел раздать карты
genstol (1)
otobrstol()
print ('Сейчас появится ривер')
time.sleep(3) #Небольшая задержка, чтобы крупье успел раздать карты
genstol (1)
otobrstol()













'''
for i in deck: # Выводим каждый ее элемент на экран 
 otobr(i)
 Deck = [ (suit, value) for suit in suits for value in values]
'''
