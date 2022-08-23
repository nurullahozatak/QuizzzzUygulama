# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# Quizz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f"Soru {questionNumber} / {totalQuestion}".center(88, "*"))

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print('-' + q)
        answer = input("Cevap : ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1


    def showScore(self):
        print("score:", self.score)



q1 = Question("Mona Lisa'nın sanatçısı kimdir ?", ["Leonardo DiCaprio", "Leonardo DaVinci", "Gogol", "Hegel"],
              "Leonardo DaVinci")
q2 = Question("Titanic'te bahsi geçen tahta parçası iki kişiyi alacak kadar büyük müydü ?", ["Evet", "Hayır"], "Evet")
q3 = Question("En uzun satranç turnuvası kaç hamle sürmüştür ?", ["a)365", "b)296", "c)456", "d)123"], "b")

questions = [q1, q2, q3]

quiz = Quiz(questions)

quiz.loadQuestion()
