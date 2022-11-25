import csv
import random

class Quiz:
    # def __init__(self):
    #     self.questions = []
    # #     #self.readQuiz()
    # #     self.loadQuiz()
    # #     # self.getQuiz()

    def loadQuiz(self,filenum):
        questions = []
        '''クイズの情報を取得する'''
        # ファイルを開く
        try:
            f = open('quizdata/quiz{}.csv'.format(filenum))
        except FileNotFoundError:
            return None

        # CSVデータとしてファイル読み込み
        csv_data = csv.reader(f)
        # CSVの各行をリスト化
        for quiz in csv_data:
            questions.append(quiz)
        f.close()

        #ランダムに10個を選択
        select_quiz = random.sample(questions, 10)
        return select_quiz

if __name__ == "__main__":
    qz = Quiz()
    print(qz.loadQuiz())
    # def getQuiz(self,page_count=0):
    #     # 正答率を計算するために、初期値として正答数に0をセット
    #     correct_count = 0
    #     #ページ数
    #     # page_count = 0
    #     #問題週の読み込み
    #     questions = Quiz.loadQuiz(self)
    #     #問題の選択
    #     question = questions[page_count][1]
    #     #選択肢を作る（１）誤りの３つ
    #     answers = questions[page_count][3:]
    #     #選択肢を作る（２）正解の１つを入れる
    #     correct_ans = questions[page_count][2]
    #     answers.append(correct_ans)
    #     #選択肢を作る（３）シャッフルする
    #     random.shuffle(answers)
    #     return question, answers, correct_ans
        
    #     # # question = self.select_quiz
    #     # # ループを回してランダムに出題しながら都度回答を表示
    #     # for quiz, question in enumerate(self.questions):
    #     #     # 選択肢を作る　（１）誤りの３つをいれる
    #     #     answers = question[3:]
    #     #     # 選択肢を作る　（２）正解を入れる
    #     #     correct_ans = self.questions[quiz][2]
    #     #     answers.append(correct_ans)
    #     #     # 選択肢を作る　（３）シャッフルする
    #     #     random.shuffle(answers)

        