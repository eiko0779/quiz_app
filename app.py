import streamlit as st
# import csv
from getquiz import Quiz
import random

# ページのタイトル設定
st.set_page_config(
    page_title="LPIC101 Quiz",
)

# # セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = "main"
    st.session_state.answers = []
    st.session_state.correct_answers = []
    st.session_state.results = []
    # #問題の読み込み
    # qz = Quiz()
    # st.session_state.questions = qz.loadQuiz()
    #正解をカウント
    st.session_state.correct_count = 0



# 各種メニューの非表示設定
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# 最初のページ
def main():
    st.markdown(
        "<h1 style='text-align: center;'>-LPIC101 Quiz-</h1>",
        unsafe_allow_html=True,
    )
    radio_dic = {"1章":1, "2章":2, "3章":3, "4章":4, "5章":5, "6章":6, "7章":7}

    def change_page():
        file_num = radio_dic[st.session_state.answer0]
        #問題の読み込み
        qz = Quiz()
        st.session_state.questions = qz.loadQuiz(file_num)
        # st.session_state.answers.append(st.session_state.answer0)
        st.session_state.page_id = "page1"

    with st.form("f0"):
        st.radio("問題を選択", radio_dic, key="answer0")
        st.form_submit_button("スタート！", on_click=change_page)


# 問題１
def page1():
    n = 1
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        # nonlocal n
        st.session_state.answers.append(st.session_state.answer1)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer1")
        st.form_submit_button("回答", on_click=change_page)

# 問題２
def page2():
    n = 2
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    #正解リストに追加
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer2)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer2")
        st.form_submit_button("回答", on_click=change_page)

# 問題３
def page3():
    n = 3
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    #正解リストに追加
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer3)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer3")
        st.form_submit_button("回答", on_click=change_page)

# 問題４
def page4():
    n = 4
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    #正解リストに追加
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer4)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer4")
        st.form_submit_button("回答", on_click=change_page)

# 問題５
def page5():
    n = 5
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    #正解リストに追加
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        st.session_state.answers.append(st.session_state.answer5)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer5")
        st.form_submit_button("回答", on_click=change_page)

# 問題6
def page6():
    n = 6
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        # nonlocal n
        st.session_state.answers.append(st.session_state.answer6)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer6")
        st.form_submit_button("回答", on_click=change_page)

# 問題７
def page7():
    n = 7
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        # nonlocal n
        st.session_state.answers.append(st.session_state.answer7)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer7")
        st.form_submit_button("回答", on_click=change_page)

# 問題８
def page8():
    n = 8
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        # nonlocal n
        st.session_state.answers.append(st.session_state.answer8)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer8")
        st.form_submit_button("回答", on_click=change_page)

# 問題９
def page9():
    n = 9
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        # nonlocal n
        st.session_state.answers.append(st.session_state.answer9)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer9")
        st.form_submit_button("回答", on_click=change_page)

# 問題１０
def page10():
    n = 10
    #問題の選択
    question = st.session_state.questions[n-1][1]
    #選択肢を作る（１）誤りの３つ
    answers = st.session_state.questions[n-1][3:]
    #選択肢を作る（２）正解の１つを入れる
    correct_ans = st.session_state.questions[n-1][2]
    answers.append(correct_ans)
    st.session_state.correct_answers.append(correct_ans)
    #選択肢を作る（３）シャッフルする
    random.shuffle(answers)
    st.markdown(
        "<h1 style='text-align: center;'>第{}問</h1>".format(n),
        unsafe_allow_html=True,
    )

    def change_page():
        # nonlocal n
        st.session_state.answers.append(st.session_state.answer10)
        st.session_state.page_id = "page_judge"

    with st.form("f1"):
        st.radio(question, answers, key="answer10")
        st.form_submit_button("回答", on_click=change_page)

#正誤判定
def page_judge(judge_count):
    m = judge_count-1
    
    if st.session_state.correct_answers[m] == st.session_state.answers[m]:
        st.session_state.correct_count += 1  
        st.session_state.results.append("○")
        st.markdown(
            "<h1 style='text-align: center;'>正解！</h1>",
            unsafe_allow_html=True,
        )    
    else:
        st.session_state.results.append("✖")
        st.markdown(
            "<h1 style='text-align: center;'>不正解！</h1>",
            unsafe_allow_html=True,
        ) 
    st.markdown("---")
    # st.markdown(
    #     "<h2 style='text-align: center;'>あなたの回答</h2>",
    #     unsafe_allow_html=True,
    # )
    st.markdown(
        f"<div style='text-align: center;'>正解：{st.session_state.correct_answers[m]}</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='text-align: center;'>あなたの解答：{st.session_state.answers[m]}</div>",
        unsafe_allow_html=True,
    )
    def change_page():
        # st.session_state.answers.append(st.session_state.answer3)
        st.session_state.page_id = "page{}".format(m+2)
        
    st.button("次へ", on_click=change_page)

# 最終ページ
def page_end():
    correct_rate = int(st.session_state.correct_count * 10)
    # 回答内容をサーバに送ったりなんなり

    st.markdown(
        "<h1 style='text-align: center;'>得点：{}点</h1>".format(correct_rate),
        unsafe_allow_html=True,
    )
    st.markdown("---")
    # st.markdown(
    #     "<h2 style='text-align: center;'>あなたの解答</h2>",
    #     unsafe_allow_html=True,
    # )
    # st.markdown(
    #     f"<div style='text-align: center;'>テーブル：{st.session_state.answers[0]}</div>",
    #     unsafe_allow_html=True,
    # )
    for num, value in enumerate(st.session_state.results):
        st.markdown(
            "<div style='text-align: center;'>第{:02d}問：{} </div>".format(num+1,value),
            unsafe_allow_html=True,
        )

    if correct_rate > 70:
        st.balloons()

    def change_page():
        # nonlocal n
        # st.session_state.answers.append(st.session_state.answer1)
        del st.session_state.page_id
        # st.session_state.page_id = "main"

    st.button("もう一回", on_click=change_page)
    # for num, value in enumerate(st.session_state.answers, 0):
    #     if num != 0:
    #         st.markdown(
    #             f"<div style='text-align: center;'>第{num}問：{value}</div>",
    #             unsafe_allow_html=True,
    #         )
    # 70点以上でバルーンを飛ばす
    

# ページ遷移のための判定
if st.session_state.page_id == "main":
    main()

if st.session_state.page_id == "page1":
    page1()

if st.session_state.page_id == "page2":
    page2()

if st.session_state.page_id == "page3":
    page3()

if st.session_state.page_id == "page4":
    page4()

if st.session_state.page_id == "page5":
    page5()

if st.session_state.page_id == "page6":
    page6()

if st.session_state.page_id == "page7":
    page7()

if st.session_state.page_id == "page8":
    page8()

if st.session_state.page_id == "page9":
    page9()

if st.session_state.page_id == "page10":
    page10()

if st.session_state.page_id == "page_judge":
    judge_count = len(st.session_state.answers)
    page_judge(judge_count)
    
if st.session_state.page_id == "page11":
    page_end()
