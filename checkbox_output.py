import tkinter as tk


# gui window to select items from list
def create_checkbox_list(words: list, window_name: str) -> list:
    # Create window
    window = tk.Tk()
    window.title(window_name)

    # Set the height of the window
    window_width = 800
    window_height = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int(screen_width / 4)
    y = int(screen_height / 2 - window_height / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    keywords = []

    max_col = 5
    checked_words = []

    def get_checked():

        for x, keyword in enumerate(keywords):
            if keyword.get():
                checked_words.append(words[x])
        window.destroy()
        return checked_words

    for i, word in enumerate(words):
        var = tk.IntVar()
        keywords.append(var)
        row = i // max_col
        col = i % max_col

        cb = tk.Checkbutton(window, text=word, variable=keywords[i])
        cb.grid(row=row, column=col, sticky="w", padx=20, pady=15)

    def invert():
        for kword in keywords:
            kword.set(not kword.get())

    invert_cb = tk.Checkbutton(window, text="Invert", command=invert)
    invert_cb.grid(columnspan=max_col, pady=40)

    submit_btn = tk.Button(window, text="Submit", command=get_checked)
    submit_btn.grid(columnspan=max_col, pady=30)

    window.mainloop()
    return checked_words


if __name__ == "__main__":
    example_words = ["cat", "dog", "bird", "fish", "cow", "horse", "pig", "sheep", "goat",
                     "cat", "dog", "bird", "big-sword-fish", "cow", "horse", "pig-vey-clever-animal", "sheep", "goat"]
    print(create_checkbox_list(example_words, 'Keywords'))
