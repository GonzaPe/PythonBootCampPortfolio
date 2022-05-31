rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
rps = [rock, paper, scissors]
select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if select ==0 or select ==1 or select ==2:
  cpu = random.randint(0,2)
  cpuSelect = rps[cpu]
  humanSelect = rps[select]
  print(humanSelect)
  print("Computer choose:")
  print(cpuSelect)
  if (cpu-select==-1) or (cpu-select==2):
    print("You win")
  elif cpu == select:
    print("Its a draw")
  elif (select-cpu==1) or (select-cpu==-2):
    print("You lose")
  else:
    print("Algo habrá pasado")
else:
  print ("You choose an invalid number, you lose!")