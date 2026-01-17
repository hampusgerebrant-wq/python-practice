questions = ("Vad vill du ha för frukt?")


options = (("A. Äpple?"),
           ("B. Banan?"),
           ("C. Päron?"))

answers = (("A"),("B"),("C"))
nxt_question = (f"Åh, {options} som är så gott, vill du att jag delar åt dig?")

print(questions)

for option in options:
    print(option)
    print("-------------")
    
    
choice = input(f"Svara med {answers}:").upper()

if choice == "A":
   nxt_question = "Åh, äpple som är så gott! Vill du att jag delar det åt dig?"
elif choice == "B":
   nxt_question = "Åh, banan som är så gott! Vill du att jag delar den åt dig?" 
elif choice == "C":
    nxt_question = "Åh, päron som är så gott! Vill du att jag delar det åt dig?"
else: 
    print("Ogiltigt val.")
    exit()

answer2 = input(nxt_question).lower()

if answer2 == "ja":
    print("Det fixar jag!")
elif answer2 == "nej":
    print("Okej, då struntar vi i det.")
else:
    print("Jag förstod inte ditt svar.")

