import os
import platform
import random
import time


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


class Player:

    def __init__(self, name: str, job: str, connection: str):
        self.name = name
        self.job = job
        self.connection = connection
        self.role = "بريء"
        self.is_culprit = False
        self.is_eliminated = False

    def to_dict(self):
        return {
            "name": self.name,
            "job": self.job,
            "connection": self.connection,
            "role": self.role,
            "is_culprit": self.is_culprit,
            "is_eliminated": self.is_eliminated,
        }


class PlayerManager:

    def __init__(self, cases_data: list):
        self.cases_data = cases_data
        self.players = []
        self.selected_case = None

    def setup_players(self):
        print("=== 🕵️ مرحبًا بكم في لعبة التحقيق والغموض 🕵️ ===\n")

        while True:
            try:
                count = int(
                    input("أدخل عدد اللاعبين (الحد الأدنى 4 لاعبين): ")
                )

                if count >= 4:
                    break

                print("❌ يجب أن يكون عدد اللاعبين 4 على الأقل!")

            except ValueError:
                print("❌ برجاء إدخال رقم صحيح.")

        print("\n--- إدخال أسماء اللاعبين ---")

        player_names = []

        for i in range(1, count + 1):
            name = input(f"أدخل اسم اللاعب رقم {i}: ").strip()

            while not name:
                name = input(
                    f"❌ الاسم لا يمكن أن يكون فارغًا. أدخل اسم اللاعب {i}: "
                ).strip()

            player_names.append(name)

        self.selected_case = random.choice(self.cases_data)

        characters = self.selected_case["characters"].copy()

        while len(characters) < count:
            characters.append(
                {
                    "job": f"شاهد إضافي {len(characters) + 1}",
                    "connection": "كان متواجدًا بالقرب من موقع الحادث.",
                }
            )

        random.shuffle(characters)

        self.players = []

        for i, name in enumerate(player_names):

            char_info = characters[i]

            player = Player(
                name=name,
                job=char_info["job"],
                connection=char_info["connection"],
            )

            self.players.append(player)

        culprit_player = random.choice(self.players)

        culprit_player.is_culprit = True
        culprit_player.role = "جاني"

        print("\n✅ تم تسجيل اللاعبين واختيار القضية وتوزيع الأدوار بنجاح!")

        time.sleep(2)

    def pass_the_phone_screen(self):

        for player in self.players:

            clear_screen()

            print("=" * 50)
            print(f"🔒 شاشة سرية خاص باللاعب: [{player.name}]")
            print("=" * 50)

            input(
                "\n👉 تأكد أنك وحدك من ينظر إلى الشاشة، ثم اضغط Enter..."
            )

            clear_screen()

            print("=" * 50)
            print(f"👤 الاسم: {player.name}")
            print(f"💼 الوظيفة في القضية: {player.job}")
            print(f"📝 الصلة/العذر: {player.connection}")
            print("-" * 30)

            if player.is_culprit:

                print(
                    "🎭 دورك السري: 🔴 أنت الجاني! "
                    "(حاول التمويه والهرب)"
                )

            else:

                print(
                    "🎭 دورك السري: 🟢 أنت محقق بريء! "
                    "(حاول اكتشاف الجاني)"
                )

            print("=" * 50)

            input(
                "\n✅ بعد قراءة بياناتك، اضغط Enter "
                "لمسح الشاشة وتسليم الجهاز للاعب بعدك..."
            )

            clear_screen()

        print(
            "\n🎉 تم كشف الأدوار لجميع اللاعبين بنجاح! "
            "جاهزون لبدء الجولة."
        )

        time.sleep(2)


CASES_DATABASE = [

    {
        "id": 1,
        "title": "تسميم في الكافتيريا",
        "location": "كافتيريا الشركة",
        "story": "موظف أصيب بإعياء شديد بعد استراحة قصيرة جوا الكافتيريا...",
        "characters": [
            {
                "job": "عامل كافتيريا",
                "connection": "كان بيقدم الطلبات ويرتب الطاولات خلال الاستراحة.",
            },
            {
                "job": "موظفة حسابات",
                "connection": "كانت بتاخد استراحتها مع عدد من زمايل الشغل.",
            },
            {
                "job": "زميل مكتب",
                "connection": "كان قاعد قرب الضحية أثناء الاستراحة.",
            },
            {
                "job": "مشرفة الدور",
                "connection": "كانت بتتابع الموظفين وتنظيم فترة الراحة.",
            },
        ],
    },

    {
        "id": 2,
        "title": "اختفاء عقد الألماس",
        "location": "قاعة مزادات خاصة",
        "story": "انقطعت أنوار صالة العرض لمدة دقيقة واحدة ووُجدت الواجهة مفتوحة...",
        "characters": [
            {
                "job": "حارس الأمن",
                "connection": "كان واقف عند الباب الرئيسي وقت انقطاع النور.",
            },
            {
                "job": "خبير التقييم",
                "connection": "المسؤول الوحيد اللي معاه نسخة ثانية من مفتاح الواجهة.",
            },
            {
                "job": "مهندس الكهرباء",
                "connection": "كان بيتفقد لوحة المفاتيح الرئيسية في القبو أثناء العطل.",
            },
            {
                "job": "جامعة تحف (ضيفة)",
                "connection": "كانت واقفة تتأمل العقد قبل انطفاء الأنوار بلحظات.",
            },
        ],
    },

    {
        "id": 3,
        "title": "تخريب لوحة المعرض",
        "location": "صالة الفنون التشكيلية",
        "story": "تم تشويه اللوحة الأغلى في المعرض بسكب حبر زيتي عليها...",
        "characters": [
            {
                "job": "فنان منافس",
                "connection": "كان بيجهز ركن لوحاته في نفس الممر.",
            },
            {
                "job": "مسؤول النظافة",
                "connection": "كان بيمسح الأرضيات بالقرب من المعرض.",
            },
            {
                "job": "مدير المعرض",
                "connection": "كان بيراجع قائمة الحضور في مكتبه بالدور الأول.",
            },
            {
                "job": "مرشد سياحي",
                "connection": "كان بيتدرب على الشرح للزوار أمام اللوحات.",
            },
        ],
    },

    {
        "id": 4,
        "title": "سرقة أسرار الشركة",
        "location": "غرفة الاجتماعات المغلقة",
        "story": "فلاشة تحتوي على كود سري للمشروع الجديد اختفت من لابتوب المدير...",
        "characters": [
            {
                "job": "المبرمج الرئيسي",
                "connection": "كان يعرض الكود على الشاشة الكبيرة أثناء الاجتماع.",
            },
            {
                "job": "المتدرب الجديد",
                "connection": "كان يدوّن الملاحظات ويوزع أوراق العمل.",
            },
            {
                "job": "مدير التسويق",
                "connection": "غادر الاجتماع لإجراء مكالمة هاتفية عاجلة لدقيقتين.",
            },
            {
                "job": "السكرتيرة",
                "connection": "كانت ترتب الملفات وتجمع الأكواب بعد انتهاء الجلسة.",
            },
        ],
    },

    {
        "id": 5,
        "title": "مقتل رجل الأعمال في الفيلا",
        "location": "غرفة المكتب بالفيلا",
        "story": "عُثر على رجل الأعمال مقتولاً داخل غرفة مكتبه المغلقة...",
        "characters": [
            {
                "job": "الخادم الشخصي",
                "connection": "كان يجهز طاولة العشاء في الدور الأرضي وقت الحادث.",
            },
            {
                "job": "المحامي الخاص",
                "connection": "كان يناقش بنود العقد مع الضحية قبل الحادث بنصف ساعة.",
            },
            {
                "job": "حارس الحديقة",
                "connection": "كان يتفقد أسوار الفيلا للتأكد من إغلاق البوابات بسبب العاصفة.",
            },
            {
                "job": "طبيب العائلة",
                "connection": "وصل متأخراً لتسليم أدوية الضغط الخاصة برجل الأعمال.",
            },
        ],
    },
]


All_cases = [

    {
        "id": 1,
        "title": "قضية: تسميم",
        "location": "كافتيريا",
        "story": (
            "موظف أصيب بإعياء شديد بعد استراحة قصيرة جوا الكافتيريا، "
            "رغم إن زمايله شاركوه نفس الأكل والشراب. "
            "ما ظهرش فرق واضح في الأطباق أو الأكواب. "
            "الغريب إن بطاقة تهنئة اتحطت على الطاولة قبل وصوله بدقايق، "
            "بعدين اتنقلت من مكانها أثناء الازدحام."
        ),
        "main_clue": [
            "بطاقة التهنئة كانت مطوية جوا من ناحية واحدة، رغم إن باقي الزينة فضلت مرتبة.",
            "ظهر أثر مسحوق خفيف على طرف منديل مستخدم، لكنه شبيه ببقايا السكر أو فتات الحلوى الموجود على الطاولة.",
        ],
        "extra_clue": [
            "أحد الموظفين لمح شخصاً يسند إيده على بطاقة التهنئة وهو يعدل فنجان الضحية أثناء الزحمة."
        ],
    },

    {
        "id": 2,
        "title": "قضية: اختفاء عقد الألماس",
        "location": "قاعة مزادات خاصة",
        "story": "انقطعت أنوار صالة العرض لدقيقة واحدة، وعند عودة الإضاءة وُجدت واجهة العرض مفتوحة بمفتاحها وعقد الألماس النادر اختفى دون إطلاق صفارات الإنذار.",
        "main_clue": [
            "مفتاح لوحة الكهرباء الرئيسية فُتح بمفك عزل متخصص وليس عطلاً عشوائياً.",
            "صفارات الإنذار تم تعطيلها يدوياً من لوحة التحكم قبل قطع الكهرباء.",
        ],
        "extra_clue": [
            "عُثر على قطعة قماش مقطوعة من سترة عمل بالقرب من لوحة الكهرباء."
        ],
    },

    {
        "id": 3,
        "title": "قضية: تخريب لوحة المعرض",
        "location": "صالة الفنون التشكيلية",
        "story": "تم تشويه اللوحة الأغلى في المعرض بسكب حبر زيتي عليها قبل حفل الافتتاح بساعة، ووُجدت كاميرا المراقبة مغطاة بقطعة قماش.",
        "main_clue": [
            "الحبر المستخدم من نوع زيتي نادر لا يستخدمه إلا المحترفون في الرسم.",
            "قطعة القماش التي غطت الكاميرا هي مريلة رسم ملوثة بألوان زيتية.",
        ],
        "extra_clue": [
            "تم العثور على زجاجة تنر مخبأة في سلة مهملات الممر الخلفي."
        ],
    },

    {
        "id": 4,
        "title": "قضية: سرقة أسرار الشركة",
        "location": "غرفة الاجتماعات المغلقة",
        "story": "فلاشة تحتوي على كود سري للمشروع الجديد اختفت من لابتوب المدير بعد جلسة عصف ذهني مغلقة حضرها 4 أشخاص فقط.",
        "main_clue": [
            "تم نسخ ونقل البيانات في توقيت مكالمة هاتفية خارجية بالضبط.",
            "منفذ الـ USB وُجد عليه خدوش تشير إلى إدخال الفلاشة ونزعها بسرعة وارتباك.",
        ],
        "extra_clue": [
            "سجل بوابة الخروج الإلكترونية سجل فتح الباب الخلفي بنفس دقيقة نقل الملفات."
        ],
    },

    {
        "id": 5,
        "title": "قضية مقتل رجل الأعمال",
        "location": "غرفة المكتب بالفيلا",
        "story": "عُثر على رجل الأعمال مقتولاً داخل غرفة مكتبه المغلقة بعد سماع صوت زجاج يتحطم أثناء العاصفة. نافذة المكتب مكسورة من الداخل للخارج، وخزنة أوراقه مفتوحة ومسروق منها عقد شراكة مهم.",
        "main_clue": [
            "الزجاج المكسور ملقى في الحديقة الخارجية مما يثبت أن الكسر تم من داخل الغرفة للتمويه.",
            "وُجدت قطرات حبر أحمر تخص قلم التوقيع ملوثة على حافة الخزنة المفتوحة.",
        ],
        "extra_clue": [
            "ساعة القتيل اليدوية توقفت عند الساعة 8:15 مساءً إثر مقاومة عنيفة."
        ],
    },
]


class CaseManager:

    def __init__(self, cases_list):
        self.all_cases = cases_list
        self.current_case = None
        self.available_main_clues = []
        self.revealed_main_clues = []
        self.available_extra_clues = []

    def select_case(self):

        self.current_case = random.choice(self.all_cases)

        self.available_main_clues = list(
            self.current_case["main_clue"]
        )

        self.available_extra_clues = list(
            self.current_case["extra_clue"]
        )

        self.revealed_main_clues = []

        return self.current_case

    def get_case_intro(self):

        if not self.current_case:
            self.select_case()

        return {
            "title": self.current_case["title"],
            "location": self.current_case["location"],
            "story": self.current_case["story"],
        }

    def get_main_clue(self):

        if not self.current_case:
            self.select_case()

        if not self.available_main_clues:
            return "لا توجد أدلة أساسية متبقية"

        clue = random.choice(self.available_main_clues)

        self.available_main_clues.remove(clue)

        self.revealed_main_clues.append(clue)

        return clue

    def get_extra_clue(self):

        if not self.current_case:
            self.select_case()

        if not self.available_extra_clues:
            return "لا توجد أدلة إضافية متبقية"

        extra = random.choice(self.available_extra_clues)

        self.available_extra_clues.remove(extra)

        return extra


def voting_round(players):

    votes = {}
    individual_votes = {}

    print("\n========== جولة التصويت ==========")
    print("اللاعبون الموجودون:")

    for player in players:
        print("-", player.name)

    for player in players:

        print("\nدور اللاعب:", player.name)
        print("اختار الشخص الذي تشتبه به:")

        choices = [
            p for p in players
            if p != player
        ]

        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice.name}")

        while True:

            try:

                choice_number = int(
                    input("اختار رقم: ")
                )

                if 1 <= choice_number <= len(choices):

                    vote = choices[choice_number - 1]

                    break

                else:

                    print("❌ اختيار غير صحيح!")
                    print("اختار رقم موجود في القائمة.")

            except ValueError:

                print("❌ من فضلك اكتب رقم فقط.")

        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1

        individual_votes[player] = vote

    return votes, individual_votes


def find_eliminated_player(votes):

    if not votes:
        return None

    max_votes = max(votes.values())

    players_with_max_votes = [
        player
        for player, number_of_votes in votes.items()
        if number_of_votes == max_votes
    ]

    if len(players_with_max_votes) > 1:

        print("\n⚠️ حصل تعادل في التصويت!")
        print("🔄 سيتم إعادة التصويت.")

        return None

    return players_with_max_votes[0]


def show_votes(votes):

    print("\n========== نتيجة التصويت ==========")

    for player, number_of_votes in votes.items():

        print(
            player.name,
            "حصل على",
            number_of_votes,
            "صوت"
        )


def eliminate_player(players, eliminated_player):

    players.remove(eliminated_player)

    print(
        "\n❌ تم استبعاد:",
        eliminated_player.name
    )


def start_game(players, case_control):

    round_number = 1

    while len(players) > 2:

        print("\n================================")
        print("          الجولة", round_number)
        print("================================")

        votes, individual_votes = voting_round(players)

        show_votes(votes)

        eliminated_player = find_eliminated_player(votes)

        if eliminated_player is None:
            continue

        eliminate_player(
            players,
            eliminated_player
        )

        if eliminated_player.is_culprit:

            print("\n🎉 مبروك!")
            print("لقد اكتشفتم الجاني!")
            print(
                "الجاني هو:",
                eliminated_player.name
            )

            return {
                "culprit_found": True,
                "culprit": eliminated_player,
                "votes": votes,
                "individual_votes": individual_votes,
            }

        else:

            print("\n❌ اللاعب المستبعد كان بريئًا!")
            print("🔎 سيتم كشف دليل جديد.")

            clue = case_control.get_main_clue()

            print("\n========== الدليل الجديد ==========")
            print("🕵️", clue)

            print("\n🔄 ستبدأ جولة جديدة.")

        round_number += 1

    if len(players) == 2:

        print("\n================================")
        print("        ⚠️ نهاية التصويت")
        print("================================")

        print("تبقى لاعبان فقط:")

        for player in players:
            print("-", player.name)

        print("\nلا يوجد تصويت آخر.")

        culprit = None

        for player in players:

            if player.is_culprit:
                culprit = player
                break

        if culprit:

            print("😈 الجاني ما زال بين اللاعبين!")
            print("الجاني هو:", culprit.name)

        print("\n========== انتهت اللعبة ==========")

        return {
            "culprit_found": False,
            "culprit": culprit,
            "votes": {},
            "individual_votes": {},
            "remaining_players": players,
        }


class ScoreJudge:

    POINTS_FOR_CORRECT_VOTE = 100
    POINTS_FOR_CULPRIT_WIN = 300
    MEDALS = ["🥇", "🥈", "🥉"]

    def __init__(self, players):
        self.scores = {player.name: 0 for player in players}
        self.cases_played = 0

    def judge_round(self, game_result):

        if not game_result:
            return

        culprit = game_result.get("culprit")

        if culprit is None:
            return

        self.cases_played += 1

        if game_result.get("culprit_found"):
            self._reward_correct_voters(game_result)
        else:
            self._reward_culprit(culprit)

    def _reward_correct_voters(self, game_result):
        individual_votes = game_result.get("individual_votes", {})

        for voter, suspect in individual_votes.items():

            if suspect.is_culprit:
                self.add_points(voter.name, self.POINTS_FOR_CORRECT_VOTE)

    def _reward_culprit(self, culprit):
        self.add_points(culprit.name, self.POINTS_FOR_CULPRIT_WIN)

    def add_points(self, player_name, points):
        self.scores[player_name] = self.scores.get(player_name, 0) + points

    def get_ranked_scores(self):
        return sorted(
            self.scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )

    def get_mvp(self):
        ranked = self.get_ranked_scores()

        if not ranked:
            return None

        return ranked[0]

    def announce_case_result(self, game_result):

        if not game_result:
            return

        culprit = game_result.get("culprit")

        print("\n" + "=" * 50)
        print("           📢 نتيجة القضية 📢")
        print("=" * 50)

        if game_result.get("culprit_found"):

            print(f"✅ تم كشف الجاني بنجاح: {culprit.name}")
            print(
                f"🏅 كل لاعب صوّت له بشكل صحيح حصل على "
                f"{self.POINTS_FOR_CORRECT_VOTE} نقطة."
            )

        else:

            culprit_name = culprit.name if culprit else "غير معروف"

            print(f"😈 الجاني نجا ولم يتم اكتشافه: {culprit_name}")
            print(
                f"🏅 الجاني حصل على {self.POINTS_FOR_CULPRIT_WIN} "
                f"نقطة كمكافأة الخداع."
            )

        print("=" * 50)

    def show_leaderboard(self):

        print("\n" + "=" * 50)
        print("           🏆 لوحة الصدارة 🏆")
        print("=" * 50)

        ranked_players = self.get_ranked_scores()

        for rank, (name, score) in enumerate(ranked_players, start=1):

            medal = self.MEDALS[rank - 1] if rank <= 3 else f"{rank}."

            print(f"{medal} {name} — {score} نقطة")

        print("=" * 50)

    def announce_final_winner(self):

        mvp = self.get_mvp()

        print("\n" + "=" * 50)
        print("        🎬 نهاية اللعبة 🎬")
        print("=" * 50)

        print(f"عدد القضايا التي لُعبت: {self.cases_played}")

        if mvp and mvp[1] > 0:
            print(f"🏆 بطل اللعبة: {mvp[0]} برصيد {mvp[1]} نقطة!")
        else:
            print("لم يحرز أي لاعب نقاطًا خلال هذه الجلسة.")

        print("=" * 50)


def ask_play_new_case():

    answer = input(
        "\n🔁 هل تريدون بدء قضية جديدة بنفس اللاعبين؟ (y/n): "
    ).strip().lower()

    return answer == "y"


def start_new_case_same_players(manager, case_control):

    for player in manager.players:
        player.is_eliminated = False
        player.is_culprit = False
        player.role = "بريء"

    manager.selected_case = random.choice(manager.cases_data)

    characters = manager.selected_case["characters"].copy()

    while len(characters) < len(manager.players):
        characters.append(
            {
                "job": f"شاهد إضافي {len(characters) + 1}",
                "connection": "كان متواجدًا بالقرب من موقع الحادث.",
            }
        )

    random.shuffle(characters)

    for player, char_info in zip(manager.players, characters):
        player.job = char_info["job"]
        player.connection = char_info["connection"]

    culprit_player = random.choice(manager.players)

    culprit_player.is_culprit = True
    culprit_player.role = "جاني"

    case_control.select_case()

    print("\n✅ تم بدء قضية جديدة بنفس اللاعبين بنجاح!")

    time.sleep(1)


if __name__ == "__main__":

    manager = PlayerManager(CASES_DATABASE)

    manager.setup_players()

    manager.pass_the_phone_screen()

    case_control = CaseManager(All_cases)

    judge = ScoreJudge(manager.players)

    playing = True

    while playing:

        intro = case_control.get_case_intro()

        print(f"\nالقضية: {intro['title']}")
        print(f"المكان: {intro['location']}")
        print(f"القصة: {intro['story']}")

        print(
            f"دليل: {case_control.get_main_clue()}"
        )

        input(
            "\nاضغط Enter للحصول على دليل إضافي..."
        )

        print(
            "دليل إضافي:",
            case_control.get_extra_clue()
        )

        input(
            "\nاضغط Enter لبدء التصويت..."
        )

        active_players = list(manager.players)

        result = start_game(active_players, case_control)

        judge.judge_round(result)
        judge.announce_case_result(result)
        judge.show_leaderboard()

        playing = ask_play_new_case()

        if playing:
            start_new_case_same_players(manager, case_control)
            manager.pass_the_phone_screen()

    judge.announce_final_winner()
