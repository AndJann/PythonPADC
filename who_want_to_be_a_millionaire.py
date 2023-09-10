#!/usr/bin/env python3

from random import randrange, shuffle

questions = [["What sort of animal is Walt Disney's Dumbo?", "Elephant"],
             ["What was the name of the Spanish waiter in the TV sitcom 'Fawlty Towers'?","Manuel"],
             ["Which battles took place between the Royal Houses of York and Lancaster?","Wars of the Roses"],
             ["Which former Beatle narrated the TV adventures of Thomas the Tank Engine?","Ringo Starr"],
             ["Queen Anne was the daughter of which English Monarch?","James II"],
             ["Who composed 'Rhapsody in Blue'?","George Gershwin"],
             ["What is the Celsius equivalent of 77 degrees Fahrenheit?","25"],
             ["What are Suffolk Punch and Hackney?","Horse"],
             ["Which Shakespeare play features the line 'Neither a borrower nor a lender be'?","Hamlet"],
             ["Which is the largest city in the USA's largest state?","Anchorage"],
             ["The word 'aristocracy' literally means power in the hands of ","The best"],
             ["Where would a 'peruke' be worn?","On the head"],
             ["In which palace was Queen Elizabeth I born?","Greenwich"],
             ["From which author's work did scientists take the word 'quark'?","James Joyce"],
             ["Which of these islands was ruled by Britain from 1815 until 1864?","Corfu"],
             ["In the UK, the abbreviation NHS stands for National what Service?","Health"],
             ["Which Disney character famously leaves a glass slipper behind at a royal ball?","Cinderella"],
             ["Which of these brands was chiefly associated with the manufacture of household locks?","Chubb"],
             ["The hammer and sickle is one of the most recognisable symbols of which political ideology?","Communism"],
             ["Which toys have been marketed with the phrase 'robots in disguise'?","Transformers"]]

variants = [["Elephant", "Deer", "Rabbit", "Donkey"],
	        ["Manuel", "Pedro", "Alfonso", "Javier"],
	        ["Thirty Years War", "Hundred Years War", "Wars of the Roses", "English Civil War"],
            ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
	        ["James II", "Henry VIII", "Victoria", "William I"],
	        ["Irving Berlin", "George Gershwin", "Aaron Copland", "Cole Porter"],
	        ["15", "20", "25", "30"],
	        ["Carriage", "Wrestling style", "Cocktail", "Horse"],
	        ["Hamlet", "Macbeth", "Othello", "The Merchant of Venice"],
	        ["Dallas", "Los Angeles", "New York", "Anchorage"],
	        ["The few", "The best", "The barons", "The rich"],
	        ["Around the neck", "On the head", "Around the waist", "On the wrist"],
	        ["Greenwich", "Richmond", "Hampton Court", "Kensington"],
	        ["Lewis Carroll", "Edward Lear", "James Joyce", "Aldous Huxley"],
	        ["Crete", "Cyprus", "Corsica", "Corfu"],
	        ["Humanity", "Health", "Honour", "Household"],
	        ["Pocahontas", "Sleeping Beauty", "Cinderella", "Elsa"],
	        ["Phillips", "Flymo", "Chubb", "Ronseal"],
	        ["Republicanism", "Communism", "Conservatism", "Liberalism"],
	        ["Bratz Dolls", "Sylvanian Families", "Hatchimals", "Transformers"]]
question_cnt = 20
right_answers = 0

print("Welcome to the game 'Who wants to be a millionaire'")

for i in range(1, 11):
    rand_id = randrange(question_cnt)
    print(f"\n{i}. {questions[rand_id][0]}\n")
    shuffle(variants[rand_id])
    print(f"A.{variants[rand_id][0]}\tB.{variants[rand_id][1]}\tC.{variants[rand_id][2]}\tD.{variants[rand_id][3]}\n")
    answer = input("Please answer A, B, C or D: ").lower()
    while answer not in 'abcd' or answer in '':
        print("Wrong answer!!")
        answer = input("Please answer A, B, C or D: ").lower()

    answer = ord(answer) - 97
    if variants[rand_id][answer] == questions[rand_id][1]:
        right_answers += 1
    del questions[rand_id]
    del variants[rand_id]
    question_cnt -= 1


print(f"\nRight answers: {right_answers}\n")

