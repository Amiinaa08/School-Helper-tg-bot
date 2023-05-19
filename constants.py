from enum import Enum
import categories.math as math_functions
import categories.geography as geography_functions
import categories.philology as philology_functions
import categories.astronomy as astronomy_functions
import categories.general as general_functions
import categories.physics as physics_functions

APP_HIERARCHY = [
    {
        "name": "Фізика", 
        "subcategories": [
            {
                "name": "Рівняння Гейзенберга неозначеності",
                "function": physics_functions.get_heisenberg_equation_message,
            },
            {
                "name": "Формула Ампера",
                "function": physics_functions.get_magnetic_field_message,
            },
            {
                "name": "Закон Бойля Маріотта",
                "function": physics_functions.get_boyle_mariotte_message,
            },
            {
                "name": "Закон Ома.",
                "function": physics_functions.get_amperage_message,
            },
            {
                "name": "Підрахувати силу тяжіння.",
                "function": physics_functions.get_gravitational_force_message,
            },
        ]
    },
    {
        "name": "Математика", 
        "subcategories": [
            {
                "name": "Довжина дуги кола",
                "function": math_functions.get_arc_length_message,
            },
            {
                "name": "Відстань від точки до прямої в просторі",
                "function": math_functions.get_distance_message,
            },
            {
                "name": "Площа прямокутника",
                "function": math_functions.get_rectangle_square_message,
            },
            {
                "name": "Площа кола",
                "function": math_functions.get_circle_square_message,
            },
        ]
    },
    {
        "name": "Географія", 
        "subcategories": [
            {
                "name": "Який океан найбільший за площею?",
                "function": geography_functions.get_biggest_ocean_message,
            },
            {
                "name": "Які дві держави мають найбільшу кількість кордонів з іншими державами?",
                "function": geography_functions.get_two_countries_names_message,
            },
            {
                "name": "Яка держава має найбільшу кількість озер в світі?",
                "function": geography_functions.get_lakes_message,
            },
            {
                "name": "Визначити форму Землі.",
                "function": geography_functions.get_earth_form_message,
            },
        ]
    },
    {
        "name": "Філологія", 
        "subcategories": [
            {
                "name": "Як утворюються питальні речення в англійській мові?",
                "function": philology_functions.get_question_rule_message,
            },
            {
                "name": "Як утворити Passive Voice в Present Simple?",
                "function": philology_functions.get_passive_voice_rule_message,
            },
            {
                "name": "Які відмінки є в українській мові?",
                "function": philology_functions.get_ukrainian_cases_message,
            },
            {
                "name": "Як утворюються дієслова в давальному відмінку?",
                "function": philology_functions.get_verb_rule_message,
            },
        ]
    },
    {
        "name": "Астрономія", 
        "subcategories": [
            {
                "name": "Як впливає зоряне світло на здоров'я людини?",
                "function": astronomy_functions.get_starlight_information_message,
            },
            {
                "name": "Що таке чорні діри та як вони виникають?",
                "function": astronomy_functions.get_black_holes_information_message,
            },
        ]
    },
    {
        "name": "Загальні", 
        "subcategories": [
            {
                "name": "Який зараз рік?",
                "function": general_functions.get_current_year_message,
            },
            {
                "name": "Заспівати улюблену пісню",
                "function": general_functions.get_random_song_message,
            },
            {
                "name": "Сказати надихаючу цитату",
                "function": general_functions.get_random_quote_message,
            },
            {
                "name": "Гра «історія». Співрозмовник задає 5 питань: хто, де, коли, навіщо, що. І підставляє їх у заготований текст і виводить",
                "function": general_functions.get_game_message,
            },
            {
                "name": "Вивести рандомне число від 1 до 100.",
                "function": general_functions.get_rand_num_message,
            },
            {
                "name": "Вивести поточний час.",
                "function": general_functions.get_current_time_message,
            },
        ]
    },
]

RATE_JUDGEMENTS = [
    """Ви обрали блок {}. Співчуваю :(
Але я з радістю тобі допоможу! Можеш поставити мені декілька перелічених запитань:""",
    "Вау, {} - мій улюблений блок! Я легко допоможу тобі з такими запитаннями:",
    "У світі немає чогось більш захопливого, ніж {}. Що саме з цього блоку тебе цікавить?",
    "Ого, ваш вибір - {}. Я ще сам не надто обізнаний в цьому блоці, але ви можете поставити мені кілька запитань:",
    "Супер, {} складний, але дуже цікавий блок! Давай разом поглиблювати свої знання! Ти можеш запитати в мене наступне: ",
    "{} - чудовий вибір! Вам пощастило: я справжній експерт в цьому блоці. Сміливо запитуйте в мене таке:",
    "Новий день - новий шанс дізнатися трохи більше з блоку {}. Не втрачай його!",
]

GENERAL_CATEGORY_QUOTE = "Вирішили трохи відволіктись від шкільних завдань? Чудово! Якраз для цього в мене є перелік запитань для блоку «{}»: "

class Categories(str, Enum):
    MAIN_MENU = "Головне меню"
    PHYSICS = "Фізика"
    MATH = "Математика"
    GEOGRAPHY = "Географія"
    PHILOLOGY = "Філологія"
    ASTRONOMY = "Астрономія"
    GENERAL = "Загальні"

class Commands(str, Enum):
    HELP = "Допомога"
    BACK ="Назад"
    QUIT = "Вихід"
