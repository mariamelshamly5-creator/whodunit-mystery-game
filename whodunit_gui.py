import tkinter as tk
from tkinter import messagebox
import random

try:
    import arabic_reshaper
    from bidi.algorithm import get_display

    def ar(text):
        return get_display(arabic_reshaper.reshape(text))

except ImportError:
    def ar(text):
        return text


INK = "#15130f"
CHARCOAL = "#1f1c15"
MANILA = "#e9dfc0"
MANILA_DARK = "#d8caa2"
BLOOD = "#a91f22"
BLOOD_BRIGHT = "#c9282b"
GOLD = "#e7b93c"
TEXT_LIGHT = "#f1ead6"
TEXT_DARK = "#221d15"
TEXT_FAINT = "#a99a7a"

FONT_TITLE = ("Arial", 26, "bold")
FONT_SUB = ("Arial", 12)
FONT_LABEL = ("Arial", 12)
FONT_BODY = ("Arial", 13)
FONT_MONO = ("Arial", 12)
FONT_BTN = ("Arial", 12, "bold")
FONT_CARD_NAME = ("Arial", 20, "bold")

CASES = [
    {
        "title": "تسميم في الكافتيريا",
        "location": "كافتيريا الشركة",
        "story": ("موظف أصيب بإعياء شديد بعد استراحة قصيرة جوا الكافتيريا، "
                   "رغم إن زمايله شاركوه نفس الأكل والشراب. ما ظهرش فرق واضح "
                   "في الأطباق أو الأكواب. الغريب إن بطاقة تهنئة اتحطت على "
                   "الطاولة قبل وصوله بدقايق، بعدين اتنقلت من مكانها أثناء الازدحام."),
        "characters": [
            {"job": "عامل كافتيريا", "connection": "كان بيقدم الطلبات ويرتب الطاولات خلال الاستراحة."},
            {"job": "موظفة حسابات", "connection": "كانت بتاخد استراحتها مع عدد من زمايل الشغل."},
            {"job": "زميل مكتب", "connection": "كان قاعد قرب الضحية أثناء الاستراحة."},
            {"job": "مشرفة الدور", "connection": "كانت بتتابع الموظفين وتنظيم فترة الراحة."},
        ],
        "main_clue": [
            "بطاقة التهنئة كانت مطوية جوا من ناحية واحدة، رغم إن باقي الزينة فضلت مرتبة.",
            "ظهر أثر مسحوق خفيف على طرف منديل مستخدم، لكنه شبيه ببقايا السكر أو فتات الحلوى.",
        ],
        "extra_clue": [
            "أحد الموظفين لمح شخصاً يسند إيده على بطاقة التهنئة وهو يعدل فنجان الضحية أثناء الزحمة.",
        ],
    },
    {
        "title": "اختفاء عقد الألماس",
        "location": "قاعة مزادات خاصة",
        "story": ("انقطعت أنوار صالة العرض لدقيقة واحدة، وعند عودة الإضاءة وُجدت "
                   "واجهة العرض مفتوحة بمفتاحها وعقد الألماس النادر اختفى دون "
                   "إطلاق صفارات الإنذار."),
        "characters": [
            {"job": "حارس الأمن", "connection": "كان واقف عند الباب الرئيسي وقت انقطاع النور."},
            {"job": "خبير التقييم", "connection": "المسؤول الوحيد اللي معاه نسخة ثانية من مفتاح الواجهة."},
            {"job": "مهندس الكهرباء", "connection": "كان بيتفقد لوحة المفاتيح الرئيسية في القبو أثناء العطل."},
            {"job": "جامعة تحف (ضيفة)", "connection": "كانت واقفة تتأمل العقد قبل انطفاء الأنوار بلحظات."},
        ],
        "main_clue": [
            "مفتاح لوحة الكهرباء الرئيسية فُتح بمفك عزل متخصص وليس عطلاً عشوائياً.",
            "صفارات الإنذار تم تعطيلها يدوياً من لوحة التحكم قبل قطع الكهرباء.",
        ],
        "extra_clue": [
            "عُثر على قطعة قماش مقطوعة من سترة عمل بالقرب من لوحة الكهرباء.",
        ],
    },
    {
        "title": "تخريب لوحة المعرض",
        "location": "صالة الفنون التشكيلية",
        "story": ("تم تشويه اللوحة الأغلى في المعرض بسكب حبر زيتي عليها قبل حفل "
                   "الافتتاح بساعة، ووُجدت كاميرا المراقبة مغطاة بقطعة قماش."),
        "characters": [
            {"job": "فنان منافس", "connection": "كان بيجهز ركن لوحاته في نفس الممر."},
            {"job": "مسؤول النظافة", "connection": "كان بيمسح الأرضيات بالقرب من المعرض."},
            {"job": "مدير المعرض", "connection": "كان بيراجع قائمة الحضور في مكتبه بالدور الأول."},
            {"job": "مرشد سياحي", "connection": "كان بيتدرب على الشرح للزوار أمام اللوحات."},
        ],
        "main_clue": [
            "الحبر المستخدم من نوع زيتي نادر لا يستخدمه إلا المحترفون في الرسم.",
            "قطعة القماش التي غطت الكاميرا هي مريلة رسم ملوثة بألوان زيتية.",
        ],
        "extra_clue": [
            "تم العثور على زجاجة تنر مخبأة في سلة مهملات الممر الخلفي.",
        ],
    },
    {
        "title": "سرقة أسرار الشركة",
        "location": "غرفة الاجتماعات المغلقة",
        "story": ("فلاشة تحتوي على كود سري للمشروع الجديد اختفت من لابتوب المدير "
                   "بعد جلسة عصف ذهني مغلقة حضرها 4 أشخاص فقط."),
        "characters": [
            {"job": "المبرمج الرئيسي", "connection": "كان يعرض الكود على الشاشة الكبيرة أثناء الاجتماع."},
            {"job": "المتدرب الجديد", "connection": "كان يدوّن الملاحظات ويوزع أوراق العمل."},
            {"job": "مدير التسويق", "connection": "غادر الاجتماع لإجراء مكالمة هاتفية عاجلة لدقيقتين."},
            {"job": "السكرتيرة", "connection": "كانت ترتب الملفات وتجمع الأكواب بعد انتهاء الجلسة."},
        ],
        "main_clue": [
            "تم نسخ ونقل البيانات في توقيت مكالمة هاتفية خارجية بالضبط.",
            "منفذ الـ USB وُجد عليه خدوش تشير إلى إدخال الفلاشة ونزعها بسرعة وارتباك.",
        ],
        "extra_clue": [
            "سجل بوابة الخروج الإلكترونية سجل فتح الباب الخلفي بنفس دقيقة نقل الملفات.",
        ],
    },
    {
        "title": "مقتل رجل الأعمال في الفيلا",
        "location": "غرفة المكتب بالفيلا",
        "story": ("عُثر على رجل الأعمال مقتولاً داخل غرفة مكتبه المغلقة بعد سماع "
                   "صوت زجاج يتحطم أثناء العاصفة. نافذة المكتب مكسورة من الداخل "
                   "للخارج، وخزنة أوراقه مفتوحة ومسروق منها عقد شراكة مهم."),
        "characters": [
            {"job": "الخادم الشخصي", "connection": "كان يجهز طاولة العشاء في الدور الأرضي وقت الحادث."},
            {"job": "المحامي الخاص", "connection": "كان يناقش بنود العقد مع الضحية قبل الحادث بنصف ساعة."},
            {"job": "حارس الحديقة", "connection": "كان يتفقد أسوار الفيلا للتأكد من إغلاق البوابات بسبب العاصفة."},
            {"job": "طبيب العائلة", "connection": "وصل متأخراً لتسليم أدوية الضغط الخاصة برجل الأعمال."},
        ],
        "main_clue": [
            "الزجاج المكسور ملقى في الحديقة الخارجية مما يثبت أن الكسر تم من داخل الغرفة للتمويه.",
            "وُجدت قطرات حبر أحمر تخص قلم التوقيع ملوثة على حافة الخزنة المفتوحة.",
        ],
        "extra_clue": [
            "ساعة القتيل اليدوية توقفت عند الساعة 8:15 مساءً إثر مقاومة عنيفة.",
        ],
    },
]


class Player:

    def __init__(self, name):
        self.name = name
        self.job = ""
        self.connection = ""
        self.is_culprit = False
        self.is_eliminated = False


class WhodunitApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(ar("مين الجاني؟ — التحقيق"))
        self.geometry("760x680")
        self.configure(bg=INK)
        self.resizable(False, False)

        self.players = []
        self.active_players = []
        self.scores = {}
        self.case = None
        self.available_main_clues = []
        self.available_extra_clues = []
        self.round_number = 1
        self.pass_index = 0
        self.individual_votes = {}
        self.voting_order = []
        self.current_voter_index = 0

        self.container = tk.Frame(self, bg=INK)
        self.container.pack(fill="both", expand=True)

        self.show_start_screen()

    def clear(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def header(self, parent, eyebrow, title):
        tk.Label(parent, text=ar(eyebrow), font=FONT_SUB, fg=GOLD, bg=parent["bg"]).pack(pady=(26, 2))
        tk.Label(parent, text=ar(title), font=FONT_TITLE, fg=TEXT_LIGHT, bg=parent["bg"]).pack()
        tk.Frame(parent, bg=BLOOD, height=2, width=140).pack(pady=(8, 18))

    # ================= START SCREEN =================

    def show_start_screen(self):
        self.clear()
        frame = tk.Frame(self.container, bg=INK)
        frame.pack(fill="both", expand=True)
        self.header(frame, "ملف القضية — تحقيق جديد", "مين الجاني؟")

        tk.Label(frame, text=ar("أدخل عدد اللاعبين (الحد الأدنى 4 لاعبين):"),
                 font=FONT_LABEL, fg=TEXT_LIGHT, bg=INK).pack(pady=(10, 4))

        self.count_entry = tk.Entry(frame, font=FONT_MONO, width=6, justify="center")
        self.count_entry.pack()

        tk.Button(frame, text=ar("متابعة"), font=FONT_BTN, bg=BLOOD, fg=TEXT_LIGHT,
                  activebackground=BLOOD_BRIGHT, relief="flat", padx=16, pady=8,
                  command=self.show_name_entry).pack(pady=20)

    def show_name_entry(self):
        try:
            count = int(self.count_entry.get())
            if count < 4:
                raise ValueError
        except ValueError:
            messagebox.showerror(ar("خطأ"), ar("من فضلك اكتب رقم صحيح، 4 على الأقل."))
            return

        self.clear()
        frame = tk.Frame(self.container, bg=INK)
        frame.pack(fill="both", expand=True)
        self.header(frame, f"{count} محققين على القضية", "سمّوا المشتبه بهم")

        self.name_entries = []
        form = tk.Frame(frame, bg=INK)
        form.pack()

        for i in range(count):
            row = tk.Frame(form, bg=INK)
            row.pack(pady=4)
            tk.Label(row, text=ar(f"اللاعب {i + 1}:"), font=FONT_LABEL, fg=TEXT_LIGHT,
                     bg=INK, width=14, anchor="e", justify="right").pack(side="right")
            entry = tk.Entry(row, font=FONT_MONO, width=22, justify="right")
            entry.pack(side="right", padx=(0, 8))
            self.name_entries.append(entry)

        tk.Button(frame, text=ar("تحديد الأدوار"), font=FONT_BTN, bg=BLOOD, fg=TEXT_LIGHT,
                  activebackground=BLOOD_BRIGHT, relief="flat", padx=16, pady=8,
                  command=self.assign_roles).pack(pady=18)

    def assign_roles(self):
        names = [entry.get().strip() for entry in self.name_entries]

        if any(name == "" for name in names):
            messagebox.showerror(ar("خطأ"), ar("لازم اسم لكل لاعب."))
            return

        self.players = [Player(name) for name in names]
        self.scores = {player.name: 0 for player in self.players}

        self._deal_new_case()

        self.pass_index = 0
        self.show_pass_phone()

    def _deal_new_case(self):
        self.case = random.choice(CASES)
        characters = list(self.case["characters"])

        while len(characters) < len(self.players):
            characters.append({
                "job": "شاهد إضافي",
                "connection": "كان متواجدًا بالقرب من موقع الحادث.",
            })

        random.shuffle(characters)

        for player, char_info in zip(self.players, characters):
            player.job = char_info["job"]
            player.connection = char_info["connection"]

        culprit = random.choice(self.players)
        culprit.is_culprit = True

    # ================= PASS THE PHONE =================

    def show_pass_phone(self):
        self.clear()
        player = self.players[self.pass_index]

        frame = tk.Frame(self.container, bg=CHARCOAL)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=ar("🔒 سلّم الجهاز لـ"), font=FONT_SUB, fg=GOLD, bg=CHARCOAL).pack(pady=(60, 4))
        tk.Label(frame, text=ar(player.name), font=FONT_TITLE, fg=TEXT_LIGHT, bg=CHARCOAL).pack()

        self.reveal_frame = tk.Frame(frame, bg=CHARCOAL)
        self.reveal_frame.pack(pady=30)

        tk.Button(self.reveal_frame, text=ar("اضغط لكشف دورك السري"), font=FONT_BTN,
                  bg=GOLD, fg=TEXT_DARK, activebackground=MANILA_DARK, relief="flat",
                  padx=20, pady=12, command=lambda: self.reveal_role(player)).pack()

    def reveal_role(self, player):
        for widget in self.reveal_frame.winfo_children():
            widget.destroy()

        card = tk.Frame(self.reveal_frame, bg=MANILA, padx=24, pady=20)
        card.pack()

        tk.Label(card, text=ar(player.name), font=FONT_CARD_NAME, fg=TEXT_DARK, bg=MANILA).pack()
        tk.Label(card, text=ar(f"الوظيفة: {player.job}"), font=FONT_BODY,
                 fg=TEXT_DARK, bg=MANILA).pack(pady=(8, 2))
        tk.Label(card, text=ar(f"العذر: {player.connection}"), font=FONT_BODY, fg=TEXT_DARK,
                 bg=MANILA, wraplength=380, justify="right").pack(pady=2)

        if player.is_culprit:
            role_text, role_color = ar("🔴 أنت الجاني"), BLOOD_BRIGHT
        else:
            role_text, role_color = ar("🟢 أنت بريء"), "#2f6b3a"

        tk.Label(card, text=role_text, font=("Arial", 14, "bold"),
                 fg=role_color, bg=MANILA).pack(pady=(10, 0))

        tk.Button(self.reveal_frame, text=ar("اخفاء وتسليم للاعب التالي"), font=FONT_BTN,
                  bg=BLOOD, fg=TEXT_LIGHT, activebackground=BLOOD_BRIGHT, relief="flat",
                  padx=16, pady=8, command=self.next_pass_phone).pack(pady=20)

    def next_pass_phone(self):
        self.pass_index += 1

        if self.pass_index < len(self.players):
            self.show_pass_phone()
        else:
            self.show_case_intro()

    # ================= CASE INTRO =================

    def show_case_intro(self):
        self.clear()
        self.available_main_clues = list(self.case["main_clue"])
        self.available_extra_clues = list(self.case["extra_clue"])

        frame = tk.Frame(self.container, bg=INK)
        frame.pack(fill="both", expand=True)
        self.header(frame, f"المكان: {self.case['location']}", self.case["title"])

        self.story_label = tk.Label(frame, text="", font=FONT_BODY, fg=TEXT_LIGHT, bg=INK,
                                     wraplength=560, justify="right")
        self.story_label.pack(pady=(0, 16), padx=40)
        self._typewriter(self.story_label, self.case["story"], 0)

        self.clue_label = tk.Label(frame, text="", font=("Arial", 12), fg=GOLD,
                                    bg=INK, wraplength=560, justify="right")
        self.clue_label.pack(pady=(0, 10), padx=40)

        btn_row = tk.Frame(frame, bg=INK)
        btn_row.pack(pady=6)

        tk.Button(btn_row, text=ar("🔍 كشف الدليل الأساسي"), font=FONT_BTN, bg=GOLD, fg=TEXT_DARK,
                  relief="flat", padx=14, pady=8, command=self.reveal_main_clue).pack(side="right", padx=6)
        tk.Button(btn_row, text=ar("🧾 دليل إضافي"), font=FONT_BTN, bg=MANILA_DARK, fg=TEXT_DARK,
                  relief="flat", padx=14, pady=8, command=self.reveal_extra_clue).pack(side="right", padx=6)

        tk.Button(frame, text=ar("ابدأ التصويت"), font=FONT_BTN, bg=BLOOD, fg=TEXT_LIGHT,
                  activebackground=BLOOD_BRIGHT, relief="flat", padx=18, pady=10,
                  command=self.start_voting_round).pack(pady=26)

    def _typewriter(self, label, text, i):
        if i <= len(text):
            label.config(text=ar(text[:i]))
            self.after(18, lambda: self._typewriter(label, text, i + 1))

    def reveal_main_clue(self):
        if not self.available_main_clues:
            self.clue_label.config(text=ar("لا توجد أدلة أساسية متبقية."))
            return

        clue = random.choice(self.available_main_clues)
        self.available_main_clues.remove(clue)
        self.clue_label.config(text=ar("🕵️ " + clue))

    def reveal_extra_clue(self):
        if not self.available_extra_clues:
            self.clue_label.config(text=ar("لا توجد أدلة إضافية متبقية."))
            return

        clue = random.choice(self.available_extra_clues)
        self.available_extra_clues.remove(clue)
        self.clue_label.config(text=ar("🧾 " + clue))

    # ================= VOTING =================

    def start_voting_round(self):
        self.active_players = [p for p in self.players if not p.is_eliminated]

        if len(self.active_players) <= 2:
            self.show_game_over(culprit_found=False)
            return

        self.voting_order = list(self.active_players)
        self.individual_votes = {}
        self.current_voter_index = 0
        self.show_voter_pass()

    def show_voter_pass(self):
        self.clear()
        voter = self.voting_order[self.current_voter_index]

        frame = tk.Frame(self.container, bg=CHARCOAL)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=ar(f"الجولة {self.round_number}"), font=FONT_SUB, fg=GOLD, bg=CHARCOAL).pack(pady=(60, 4))
        tk.Label(frame, text=ar("🔒 سلّم الجهاز لـ"), font=FONT_SUB, fg=GOLD, bg=CHARCOAL).pack()
        tk.Label(frame, text=ar(voter.name), font=FONT_TITLE, fg=TEXT_LIGHT, bg=CHARCOAL).pack()

        tk.Button(frame, text=ar("جاهز للتصويت"), font=FONT_BTN, bg=GOLD, fg=TEXT_DARK,
                  relief="flat", padx=20, pady=12, command=self.show_vote_choice).pack(pady=30)

    def show_vote_choice(self):
        self.clear()
        voter = self.voting_order[self.current_voter_index]

        frame = tk.Frame(self.container, bg=INK)
        frame.pack(fill="both", expand=True)
        self.header(frame, f"{voter.name}، صوّت الآن", "مين في رأيك الجاني؟")

        choices = [p for p in self.active_players if p != voter]

        for suspect in choices:
            tk.Button(frame, text=ar(suspect.name), font=FONT_BTN, bg=MANILA, fg=TEXT_DARK,
                      activebackground=GOLD, relief="flat", padx=16, pady=10, width=26,
                      command=lambda s=suspect: self.cast_vote(voter, s)).pack(pady=5)

    def cast_vote(self, voter, suspect):
        self.individual_votes[voter] = suspect
        self.current_voter_index += 1

        if self.current_voter_index < len(self.voting_order):
            self.show_voter_pass()
        else:
            self.finish_voting_round()

    def finish_voting_round(self):
        tally = {}

        for suspect in self.individual_votes.values():
            tally[suspect] = tally.get(suspect, 0) + 1

        max_votes = max(tally.values())
        top = [player for player, votes in tally.items() if votes == max_votes]

        if len(top) > 1:
            self.show_tie_screen(tally)
            return

        eliminated = top[0]
        self.active_players.remove(eliminated)
        eliminated.is_eliminated = True

        if eliminated.is_culprit:
            for voter, suspect in self.individual_votes.items():
                if suspect.is_culprit:
                    self.scores[voter.name] = self.scores.get(voter.name, 0) + 100

            self.show_game_over(culprit_found=True)
        else:
            self.show_round_result(eliminated, tally)

    def show_tie_screen(self, tally):
        self.clear()
        frame = tk.Frame(self.container, bg=INK)
        frame.pack(fill="both", expand=True)
        self.header(frame, "مفيش أغلبية واضحة", "تعادل!")

        for player, votes in tally.items():
            tk.Label(frame, text=ar(f"{player.name} — {votes} صوت"),
                     font=FONT_BODY, fg=TEXT_LIGHT, bg=INK).pack()

        tk.Button(frame, text=ar("إعادة التصويت في نفس الجولة"), font=FONT_BTN, bg=BLOOD, fg=TEXT_LIGHT,
                  relief="flat", padx=18, pady=10, command=self.start_voting_round).pack(pady=24)

    def show_round_result(self, eliminated, tally):
        self.clear()
        frame = tk.Frame(self.container, bg=INK)
        frame.pack(fill="both", expand=True)
        self.header(frame, f"نتيجة الجولة {self.round_number}", f"{eliminated.name} كان بريء")

        for player, votes in tally.items():
            tk.Label(frame, text=ar(f"{player.name} — {votes} صوت"),
                     font=FONT_BODY, fg=TEXT_FAINT, bg=INK).pack()

        clue_text = "لا توجد أدلة متبقية."

        if self.available_main_clues:
            clue = random.choice(self.available_main_clues)
            self.available_main_clues.remove(clue)
            clue_text = clue

        tk.Label(frame, text=ar("🕵️ دليل جديد اتكشف:"), font=("Arial", 12),
                 fg=GOLD, bg=INK).pack(pady=(20, 2))
        tk.Label(frame, text=ar(clue_text), font=FONT_BODY, fg=TEXT_LIGHT, bg=INK,
                 wraplength=540, justify="right").pack(padx=40)

        self.round_number += 1

        tk.Button(frame, text=ar("الجولة التالية"), font=FONT_BTN, bg=BLOOD, fg=TEXT_LIGHT,
                  relief="flat", padx=18, pady=10, command=self.start_voting_round).pack(pady=26)

    # ================= GAME OVER =================

    def show_game_over(self, culprit_found):
        self.clear()
        frame = tk.Frame(self.container, bg=CHARCOAL)
        frame.pack(fill="both", expand=True)

        culprit = next(p for p in self.players if p.is_culprit)

        if culprit_found:
            self.header(frame, "القضية اتقفلت", f"{culprit.name} اتقبض عليه!")
            tk.Label(frame, text=ar("كل لاعب صوّت صح ياخد 100 نقطة."),
                     font=FONT_BODY, fg=TEXT_LIGHT, bg=CHARCOAL).pack(pady=6)
        else:
            self.scores[culprit.name] = self.scores.get(culprit.name, 0) + 300
            self.header(frame, "القضية اتقفلت", f"{culprit.name} هرب!")
            tk.Label(frame, text=ar(f"{culprit.name} خدع الكل وياخد 300 نقطة."),
                     font=FONT_BODY, fg=TEXT_LIGHT, bg=CHARCOAL).pack(pady=6)

        tk.Button(frame, text=ar("شوف لوحة الصدارة"), font=FONT_BTN, bg=GOLD, fg=TEXT_DARK,
                  relief="flat", padx=18, pady=10, command=self.show_leaderboard).pack(pady=26)

    # ================= LEADERBOARD =================

    def show_leaderboard(self):
        self.clear()
        frame = tk.Frame(self.container, bg=INK)
        frame.pack(fill="both", expand=True)
        self.header(frame, "النتيجة النهائية", "🏆 لوحة الصدارة")

        ranked = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        medals = ["🥇", "🥈", "🥉"]

        for i, (name, score) in enumerate(ranked):
            medal = medals[i] if i < 3 else f"{i + 1}."
            tk.Label(frame, text=ar(f"{medal} {name} — {score} نقطة"), font=("Arial", 14, "bold"),
                     fg=TEXT_LIGHT, bg=INK).pack(pady=4)

        btn_row = tk.Frame(frame, bg=INK)
        btn_row.pack(pady=24)

        tk.Button(btn_row, text=ar("قضية جديدة، نفس اللاعبين"), font=FONT_BTN, bg=BLOOD, fg=TEXT_LIGHT,
                  relief="flat", padx=16, pady=10, command=self.replay_same_players).pack(side="right", padx=6)
        tk.Button(btn_row, text=ar("خروج"), font=FONT_BTN, bg=MANILA_DARK, fg=TEXT_DARK,
                  relief="flat", padx=16, pady=10, command=self.destroy).pack(side="right", padx=6)

    def replay_same_players(self):
        for player in self.players:
            player.is_eliminated = False
            player.is_culprit = False

        self._deal_new_case()

        self.round_number = 1
        self.pass_index = 0
        self.show_pass_phone()


if __name__ == "__main__":
    app = WhodunitApp()
    app.mainloop()