import random

'''
This program is a play off of the Magic 8-Ball toy.
The user asks a yes/no question and the Magic 8-Ball answers
'''

name = "Jonathan"
question = "Will I find success?"
answer = ""

random_number = random.randint(1, 9)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)