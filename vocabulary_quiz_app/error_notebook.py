ERROR_WORD_FILE = "error_words.txt"

def save_error_word(word, mean):
    with open(ERROR_WORD_FILE, "a", encoding="utf-8") as f:
        f.write(f"{word} | {mean}\n")

def show_all_error():
    try:
        with open(ERROR_WORD_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        print("=====错题本列表=====")
        print(content)
    except FileNotFoundError:
        print("暂无错题记录")