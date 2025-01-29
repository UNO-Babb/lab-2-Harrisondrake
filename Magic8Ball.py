#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  answers = ["As i see it, yes", "Ask again later", "Better not tell you now",
             "Don't count on it", "It is certain", "Most likely",
             "My reply is no", "My sources say no"]
  #Answer question randomly with one of the options from your earlier list.
  question = input("Ask me a yes or no question: ")
  num = random.random()
  num = num *10
  num = int(num)
  num = num % 9
  print(answers[num])

  

  
if __name__ == '__main__':
  main()
