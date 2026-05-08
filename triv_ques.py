import pygame
import random


class Trivia:
    def __init__(self, filename, font):
        self.filename =filename
        self.i=-1
        self.font=font
        

        file= open(self.filename, "r")
        self.trivia_q=[]
        for lines in file:
            self.trivia_q.append(lines)
        file.close()
        random.shuffle(self.trivia_q)
        self.question=""
        self.answer=""
        self.get_next_QnA()
    def get_next_QnA(self):
        self.i+=1
        num1 = self.trivia_q[self.i].strip()
        quest_a = num1.split("? ", 1)
        question = quest_a[0] + "?"
        answer = quest_a[1] if len(quest_a) > 1 else ""
        self.answer=answer
        self.question = question
        return question, answer
    def comp(self, guess):
        self.guess=guess
        if guess==self.answer:
            return 1
        else:
            return 0
        
    def draw(self, surface,width):
        self.width= width
        text = self.font.render(self.question, True, "Black")

        surface.blit(text,((width-text.get_size()[0])/2,150))

#triv= Trivia("trivia.txt")
#quest, answer =triv.get_next_QnA()
#print(f"Question: {quest}")
#guess=input()
#print(f"Guess: {guess}")
#score=0
#score +=triv.comp(guess)
#print("Answer:", answer)
#print(score)


        