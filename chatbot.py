import random
import re

# -------- COUNTRY GAME DATA --------
countries = [
    "pakistan", "nepal", "turkmenistan", "norway", "yemen", "nigeria","yemen","morroco","libya",
    "australia", "afghanistan", "turkey", "yugoslavia", "argentina","oman","iraq","syria",
    "algeria", "india", "austria", "america", "canada", "denmark","iran","england","newzealand",
    "bangladesh","georgia","mexico","brazil","spain","china" ,"russia","germany","france","egypt",
    "japan","albania","algeria","cuba","indonesia","kenya","nepal","vietnam","zimbabwe","united arab emirates",
    "norway","philippines","qatar","saudia arabia","south africa","thailand","lebanon","sudan","ukraine","portugal"
    ,"poland","italy","finland","korea","malaysia","singapore","tunisia","colombia","venezuela","uraguay"
    "greenland","greece","sweden","switzerland","ecuador","romania","djibouti","kuwait",
]


game_active = False
used_countries = []
expected_letter = None


# -------- CALCULATOR FUNCTION --------
def calculate(expression):
    try:
        # Remove spaces
        expression = expression.replace(" ", "")

        # Validate expression (only numbers and operators)
        if not re.match(r'^[0-9+\-*/().]+$', expression):
            return "Invalid calculation!"

        result = eval(expression)
        return f"Result: {result}"

    except:
        return "Error in calculation!"


# -------- COUNTRY GAME FUNCTION --------
def country_game(user_input):
    global game_active, used_countries, expected_letter

    user_input = user_input.lower()

    # End game manually
    if user_input == "end":
        game_active = False
        used_countries = []
        expected_letter = None
        return "You ended the game. I win 😄"

    # Check valid country
    if user_input not in countries:
        return "Invalid country name! Try again ❌"

    # Check repetition
    if user_input in used_countries:
        return "Already used! Try another country ❌"

    # Check correct starting letter
    if expected_letter and not user_input.startswith(expected_letter):
        return f"Wrong country! It should start with '{expected_letter.upper()}'. Try again ❌"

    # Accept user input
    used_countries.append(user_input)

    last_letter = user_input[-1]
    expected_letter = last_letter

    # Bot turn
    for country in countries:
        if country.startswith(last_letter) and country not in used_countries:
            used_countries.append(country)
            expected_letter = country[-1]
            return f"{country.capitalize()}"

    # Bot cannot find answer → user wins
    game_active = False
    used_countries = []
    expected_letter = None
    return "I cannot find a country. You win 🎉"


# -------- MAIN CHAT FUNCTION --------
def get_response(message):
    global game_active, used_countries, expected_letter

    msg = message.lower().strip()

    # -------- GAME MODE --------
    if game_active:
        return country_game(msg)

    # -------- START GAME --------
    if "country game"in msg or"play game" in msg:
        game_active = True
        used_countries = []
        expected_letter = None
        return "Let's start the country game! You go first."

    # -------- CALCULATOR --------
    if re.search(r'[0-9]+\s*[\+\-\*/]\s*[0-9]+', msg):
        return calculate(msg)

    # -------- CUSTOM INTENTS --------
    if msg in ["assalamualaikum", "aoa"]:
        return "Walaikumsalam!"

    if "who made you" in msg or "who created you" in msg:
        return "I was created by Waleed."

    if "email" in msg or "contact" in msg:
        return "You can contact me at: waleedahmed1555@gmail.com"

    if "cv" in msg or "resume" in msg:
        return 'Here is my CV: <a href="https://waleedahmad555.github.io/waleed_designed_cv/" target="_blank">Open CV</a>'

    if "what can you do" in msg or "how can you help" in msg:
        return ("I can:\n"
                "- Show my CV\n"
                "- Do basic calculations\n"
                "- Play country name game\n"
                "- Answer simple questions")

    if "hello" in msg or "hi" in msg or "hey" in msg:
        return random.choice(["Hello!", "Hi there!", "Hey!"])

    if "how are you" in msg:
        return random.choice(["I'm doing great!", "All good!", "Awesome!"])

    if "bye" in msg:
        return "Goodbye!"

    return "Sorry, I didn't understand that."