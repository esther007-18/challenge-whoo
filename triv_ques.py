import pygame
import random


class Trivia:
    def __init__(self, filename):
        self.filename =filename
        self.i=-1
        file= open(self.filename, "r")
        self.trivia_q=[]
        for lines in file:
            self.trivia_q.append(lines)
        file.close()
        random.shuffle(self.trivia_q)
    def get_next_QnA(self):
        self.i+=1
        num1 = self.trivia_q[self.i].strip()
        quest_a = num1.split("? ", 1)
        question = quest_a[0] + "?"
        answer = quest_a[1] if len(quest_a) > 1 else ""

        return question, answer
    def comp(self, guess):
        self.guess=guess
        if guess==answer:
            return 1
        else:
            return 0
#triv= Trivia("trivia.txt")
#quest, answer =triv.get_next_QnA()
#print(f"Question: {quest}")
#guess=input()
#print(f"Guess: {guess}")
#score=0
#score +=triv.comp(guess)
#print("Answer:", answer)
#print(score)


        