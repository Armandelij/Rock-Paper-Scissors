import random


class Player(object):

              

               def __init__(self,name):

                              self.name = name

                              self.value = ''

                             

               def getName(self):

                              return self.name
                     

class Bart(Player):

              

               def __init__(self):

                              super(Bart,self).__init__("Bart")

            

               def generateRoshambo(self):

                              self.value = 'rock'

                             

               def getRoshambo(self):

                              return self.value
        

class Lisa(Player):

              

               def __init__(self):

                              super(Lisa,self).__init__("Lisa")


               def generateRoshambo(self):

                              n = random.randint(1,3)

                              if n == 1:

                                             self.value = "rock"

                              elif n == 2:

                                             self.value = "paper"

                              else:

                                             self.value = "scissors"

              

               def getRoshambo(self):

                              return self.value
                 

def main():

               print('Roshambo Game\n')


               name = raw_input('Enter your name : ')

               user = Player(name)


               against_name = raw_input('Would you like to play Bart or Lisa? (b/l): ')

               if against_name.lower() == 'b':

                              against = Bart()

               else:

                              against = Lisa()
        

               wins = 0

               loss = 0

               tie = 0

              

               again = 'y'


               while again == 'y':


                              user_choice = raw_input('\nRock, paper , or scissors? (r/p/s) : ')

                              if user_choice.lower() == 'r':

                                             user_roshambo = 'rock'

                              elif user_choice.lower() == 'p':

                                             user_roshambo = 'paper'

                              else:

                                             user_roshambo = 'scissors'

                                            

                              against.generateRoshambo() 


                              print('\n%s: %s' %(user.getName(),user_roshambo))

                              print('%s: %s' %(against.getName(),against.getRoshambo()))         


                              if(user_roshambo == against.getRoshambo()): 

                                             tie += 1

                                             print('Draw!')

                              elif((user_roshambo == 'rock' and against.getRoshambo() == 'scissors')       or (user_roshambo == 'paper' and against.getRoshambo() == 'rock') or (user_roshambo == 'scissors' and against.getRoshambo() == 'paper')): # user wins

                                             wins += 1

                                             print('%s wins!' %(user.getName()))

                              else: 

                                             loss += 1

                                             print('%s wins!' %(against.getName()))

                                            

                              again = raw_input('\nPlay again? (y/n) : ')

               print('\n Total games : %d '%(wins+loss+tie))

               print('Wins : %d' %(wins))

               print('Loss : %d' %(loss))

               print('\nThanks for playing!')
 

main()                  