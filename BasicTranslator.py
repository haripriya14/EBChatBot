#This is a translator#Read The phrase
def translate(phrase):
    translator=""
    for letters in phrase:
        if letters.lower() in "aeiou":
            if letters.isupper():
                translator=translator+"G"
            else:
                translator=translator+"g"
        else:
            translator=translator+letters
    return translator

#Read The phrase
print(translate(raw_input("Enter any phrase: ")))
