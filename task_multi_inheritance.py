# task1
# import datetime
# from time import sleep

# class Clock:    
#     def time(self):
#         print(datetime.datetime.now())


# class Alarm:
#     alarm = None
#     def turn_on_alarm(self):
#         Alarm.alarm = True

#     def turn_off_alarm(self):
#         Alarm.alarm = False


# class AlarmClock(Alarm, Clock):
#     def get_alarm(self, hour=0, minutes=0):
#         while AlarmClock.alarm:
#             time_now = datetime.datetime.now()
#             if str(time_now.hour) == hour and str(time_now.minute) == minutes:
#                 print('ALARM')
#                 break
#             sleep(1)

# alarm = AlarmClock()
# alarm.time()
# alarm.turn_on_alarm()
# alarm.get_alarm(hour="16",minutes="57")

# task2
# class Coder:
#     experience = ''
#     count_code_time = 0

#     def get_info(self):
#         raise NotImplementedError

#     def coding(self):
#         raise NotImplementedError


# class Backend(Coder):
#     def __init__(self, languages_backend):
#         self.experience = languages_backend

#     def get_info(self):
#         print(f'язык {self.experience} время кода {self.count_code_time} часов')

#     def coding(self, time):
#         count_code_time = 0
#         self.count_code_time = time
#         count_code_time += time
    
#     # def birthday(self):
#         # self.age += 1


# class Frontend(Coder):
#     def __init__(self, languages_frontend):
#         self.experience = languages_frontend

#     def get_info(self):
#         print(f'язык {self.experience} время кода {self.count_code_time} часов')

#     def coding(self, time):
#         self.count_code_time += time


# class FullStack(Frontend, Backend, Coder):

#     def __init__(self, languages_frontend):
#         self.experience = languages_frontend


# b = Backend('Python')
# b.coding(33)
# # b.coding()
# b.get_info()

# f = Frontend('JS')
# f.coding(44)
# f.get_info()

# fs = FullStack('Python, JS')
# fs.coding(77)
# fs.get_info()


# task3

# import random

# class Card:
    
#     def __init__(self, suit, rank):
#         self.suit = suit 
#         self.rank = rank

#     def __str__(self):
#         return f'{self.rank} {self.suit}'
 
 
# class Deck:
    
#     def __init__(self, cards):
#         self.cards = cards
 
#     def mix(self):
#         card = random.shuffle(self.cards)
#         for card in self.cards:
#             print(card)
 
#     def deal(self):
#         if not self.cards:
#             return 'no card'
#         card = random.choice(self.cards)
#         # print(card) 
#         print(f"выбор пал на {card}")
#         c = self.cards.index(card)
#         del(self.cards[c])
    
 
# rank = ['Ace', 'King','Queen','Joker','10','9','8','7','6','5','4','3','2']
# suit = ["червы","бубны","трефы","пики" ]
# cards = [Card(s,r) for s in suit for r in rank] 
 
 
# deck = Deck(cards)
# deck.mix()
# deck.deal()


# task 4

# def hackerrankInString(s):
#     point = 'somestring'
#     dl = len(point)
#     x = 0
#     for char in s:
#         if char == point[x]:
#             x += 1
#             if x == dl:
#                 return "YES"
#     return "NO"
