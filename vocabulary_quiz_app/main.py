from __future__ import annotations
from datetime import datetime, timedelta
from collections import Counter

import tkinter as tk

from vocabulary_quiz_app.app import VocabularyQuizApp
from vocabulary_quiz_app.data import WORDS


def main() -> int:
    root = tk.Tk()
    VocabularyQuizApp(root, WORDS)
    root.mainloop()
    return 0


def make_weekly_error_report():
    today = datetime.now()
    week_start = today - timedelta(days=7)
    error_list = []
    try:
        with open("error_words.txt","r",encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            word,err_date_str = line.strip().split("|")
            err_date = datetime.strptime(err_date_str,"%Y-%m-%d")
            if err_date >= week_start:
                error_list.append(word)
        count_dict = Counter(error_list)
        sort_data = sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
        with open("weekly_report.txt","w",encoding="utf-8") as fw:
            fw.write(f"주간통계:{week_start.date()}~{today.date()}\n")
            fw.write("단어|틀린횟수\n")
            for w,c in sort_data:
                fw.write(f"{w}|{c}\n")
        print("주간리포트 생성완료, weekly_report.txt 확인")
    except:
        print("오답파일 없음")

if __name__ == "__main__":
    main()
