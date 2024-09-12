def main():
    yourMood = input("How's your mood: 'sad' OR 'happy' ?")
    yourMood = convert(yourMood)
    print(yourMood)

def convert(yourMood):
    yourMood = yourMood.replace(":)", "🙂")
    yourMood = yourMood.replace(":(", "🙁")
    return yourMood

main()