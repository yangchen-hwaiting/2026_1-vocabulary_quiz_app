from __future__ import annotations
import random
import tkinter as tk
from tkinter import ttk, font, messagebox

from vocabulary_quiz_app.quiz_logic import Word, check_answer, draw_word


class VocabularyQuizApp:
    def __init__(self, root: tk.Tk, words: list[Word]) -> None:
        self.words = words
        self.rng = random.Random()
        self.current: Word | None = None
        self.checked = False
        self.score = 0
        self.total = 0

        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(family="NanumGothic", size=12)

        root.title("Vocabulary Quiz")
        root.geometry("420x280")
        root.resizable(False, False)

        self.word_var = tk.StringVar(value="단어를 불러오는 중...")
        self.feedback_var = tk.StringVar(value="")
        self.score_var = tk.StringVar(value="Score: 0/0")

        ttk.Label(root, text="영단어").pack(pady=(16, 4))
        ttk.Label(root, textvariable=self.word_var, font=("NanumGothic", 24)).pack()

        self.answer_entry = ttk.Entry(root, font=("NanumGothic", 14))
        self.answer_entry.pack(pady=12, ipadx=6, ipady=4)

        buttons = ttk.Frame(root)
        buttons.pack(pady=6)
        self.check_button = ttk.Button(buttons, text="채점", command=self.check_current)
        self.check_button.pack(side=tk.LEFT, padx=6)
        ttk.Button(buttons, text="다음", command=self.next_word).pack(side=tk.LEFT, padx=6)
        # 新增：单词收藏按钮
        ttk.Button(buttons, text="단어 즐겨찾기", command=self.add_current_word_to_favorite).pack(side=tk.LEFT, padx=6)

        ttk.Label(root, textvariable=self.feedback_var).pack(pady=8)
        ttk.Label(root, textvariable=self.score_var).pack()

        self.next_word()

    def next_word(self) -> None:
        self.current = draw_word(self.words, self.rng)
        self.word_var.set(self.current.term)
        self.answer_entry.delete(0, tk.END)
        self.feedback_var.set("")
        self.checked = False
        self.check_button.state(["!disabled"])
        self.answer_entry.focus()

    def check_current(self) -> None:
        if self.current is None or self.checked:
            return
        self.checked = True
        self.total += 1
        user_input = self.answer_entry.get()
        if check_answer(self.current, user_input):
            self.score += 1
            self.feedback_var.set("정답입니다!")
        else:
            self.feedback_var.set(f"오답입니다. 정답: {self.current.meaning}")
        self.score_var.set(f"Score: {self.score}/{self.total}")
        self.check_button.state(["disabled"])

   
    def add_current_word_to_favorite(self):
        from vocabulary_quiz_app.data import favorite_words, FAV_FILE

        target_word = random.choice(self.words)
        if target_word in favorite_words:
            messagebox.showwarning("안내", f"{target_word.term} 는 이미 즐겨찾기에 있습니다!")
            return

        favorite_words.append(target_word)
        try:
            with open(FAV_FILE, "a", encoding="utf-8") as f:
                f.write(f"단어: {target_word.term} | 뜻: {target_word.meaning}\n")
            messagebox.showinfo("성공", f"{target_word.term} 를 즐겨찾기에 추가했습니다!")
        except Exception:
            messagebox.showerror("오류", "파일 저장에 실패했습니다.")