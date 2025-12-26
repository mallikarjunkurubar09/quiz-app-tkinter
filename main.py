import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- QUESTIONS ---------------- #
quiz = [
    {"q": "Capital of India?", "o": ["Delhi", "Mumbai", "Chennai", "Kolkata"], "a": "Delhi"},
    {"q": "Python is a ___ language?", "o": ["Low level", "High level", "Assembly", "Machine"], "a": "High level"},
    {"q": "Which is not a datatype?", "o": ["int", "float", "str", "real"], "a": "real"},
    {"q": "HTML stands for?", "o": ["Hyper Text Markup Language", "High Text Machine Language", "Home Tool Markup", "None"], "a": "Hyper Text Markup Language"},
    {"q": "Which loop runs at least once?", "o": ["for", "while", "do-while", "foreach"], "a": "do-while"},
    {"q": "Which is a Python framework?", "o": ["Django", "Laravel", "Spring", "React"], "a": "Django"},
    {"q": "What is SQL used for?", "o": ["Design", "Testing", "Database", "Styling"], "a": "Database"},
    {"q": "Which keyword defines a function?", "o": ["def", "func", "define", "fun"], "a": "def"},
    {"q": "Which symbol is used for comments in Python?", "o": ["//", "#", "/*", "--"], "a": "#"},
    {"q": "Which data structure uses FIFO?", "o": ["Stack", "Queue", "Tree", "Graph"], "a": "Queue"},
    {"q": "Which is mutable?", "o": ["tuple", "string", "list", "int"], "a": "list"},
    {"q": "Which operator is used for power?", "o": ["^", "**", "//", "%"], "a": "**"},
    {"q": "What does CPU stand for?", "o": ["Central Processing Unit", "Core Process Unit", "Control Program Unit", "None"], "a": "Central Processing Unit"},
    {"q": "Which is not OOP concept?", "o": ["Encapsulation", "Inheritance", "Compilation", "Polymorphism"], "a": "Compilation"},
    {"q": "Python file extension?", "o": [".pt", ".py", ".pyt", ".python"], "a": ".py"},
    {"q": "Which keyword is used to import?", "o": ["include", "import", "using", "require"], "a": "import"},
    {"q": "Which loop is best for fixed iteration?", "o": ["while", "do while", "for", "loop"], "a": "for"},
    {"q": "What is RAM?", "o": ["Storage", "Memory", "CPU", "Input"], "a": "Memory"},
    {"q": "Which is not a DB?", "o": ["MySQL", "MongoDB", "Oracle", "HTML"], "a": "HTML"},
    {"q": "Which is fastest?", "o": ["RAM", "HDD", "SSD", "Cache"], "a": "Cache"},
    {"q": "Which tag for paragraph?", "o": ["<p>", "<h>", "<div>", "<span>"], "a": "<p>"},
    {"q": "What is Git?", "o": ["IDE", "Compiler", "Version Control", "Browser"], "a": "Version Control"},
    {"q": "Which is backend language?", "o": ["HTML", "CSS", "Python", "Bootstrap"], "a": "Python"},
    {"q": "Which is frontend?", "o": ["SQL", "Python", "CSS", "Node"], "a": "CSS"},
    {"q": "Which is not OS?", "o": ["Windows", "Linux", "Oracle", "Mac"], "a": "Oracle"},
]

# ---------------- UI CLASS ---------------- #
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Quiz App")
        self.root.geometry("600x450")
        self.root.config(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.q_index = 0
        self.score = 0
        self.time_left = 15

        # Title
        tk.Label(root, text="QUIZ APPLICATION", font=("Arial", 20, "bold"),
                 bg="#1e1e2f", fg="white").pack(pady=10)

        # Progress
        self.progress = ttk.Progressbar(root, length=400, maximum=len(quiz))
        self.progress.pack(pady=5)

        # Question
        self.question_label = tk.Label(root, text="", wraplength=520,
                                       font=("Arial", 14), bg="#1e1e2f", fg="white")
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.options = []
        for _ in range(4):
            rb = tk.Radiobutton(
                root, text="", variable=self.var,
                font=("Arial", 12),
                bg="#1e1e2f", fg="white",
                selectcolor="#3b3b5c"
            )
            rb.pack(anchor="w", padx=120)
            self.options.append(rb)

        self.timer_label = tk.Label(root, text="Time: 15",
                                    font=("Arial", 12, "bold"),
                                    fg="yellow", bg="#1e1e2f")
        self.timer_label.pack(pady=10)

        self.next_btn = tk.Button(root, text="Next ➜",
                                  font=("Arial", 12),
                                  bg="#4caf50", fg="white",
                                  command=self.next_question)
        self.next_btn.pack(pady=10)

        self.load_question()
        self.update_timer()

    def load_question(self):
        self.var.set(None)
        self.time_left = 15

        q = quiz[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}. {q['q']}")

        for i, opt in enumerate(q["o"]):
            self.options[i].config(text=opt, value=opt)

        self.progress["value"] = self.q_index

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"⏳ Time: {self.time_left}s")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def next_question(self):
        if self.var.get() == quiz[self.q_index]["a"]:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(quiz):
            self.load_question()
        else:
            messagebox.showinfo(
                "Quiz Finished",
                f"🎉 Score: {self.score}/{len(quiz)}"
            )
            self.root.destroy()

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
