def main():

    name1 = ["Förnamn?"]
    names1 = input("Förnamn?")

    name1.append(names1)

    name2 = ["Efternamn?"]
    names2 = input("Efternamn?")

    name2.append(names2)

    age = ["Hur gammal är du?"]
    ages = int(input("Hur gammal är du?"))

    age.append(ages)

    print("Hej",names1,names2,",", ages,"!")

    if ages >= 30:
        question1 = ["Sömn"]
        question2 = float(input("Hur många timmar har du sovit inatt, " + names1 + "?"))
        if question2 <= 8:
            print("Då behöver du ta det lugnt idag, du är faktiskt",ages,"år, passa på och ta en tupplur mitt på dagen.")
        else:
            print("Grattis,",names1,", du bör vara utvilad och redo att fånga dagen!")
    else:
        question3 = float(input("Hur många timmar har du sovit inatt, " + names1 + "?"))
        if question3 <= 8:
            print("Du är ung",names1,", sluta gnäll och upp och hoppa!")
        else:
            print("Grattis,",names1,", du har sovit minst 8 timmar, nu har du energi som räcker hela dagen!")


if __name__ == "__main__":
    main()
