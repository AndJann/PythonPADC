#!/usr/bin/env python3

from random import randrange, shuffle

questions = ["What sort of animal is Walt Disney's Dumbo?Elephant Deer Rabbit Donkey",
             "What was the name of the Spanish waiter in the TV sitcom 'Fawlty Towers'?Manuel Pedro Alfonso Javier",
             "Which battles took place between the Royal Houses of York and Lancaster?Wars_of_the_Roses Thirty_Years_War Hundred_Years_War English_Civil_War",
             "Which former Beatle narrated the TV adventures of Thomas the Tank Engine?Ringo_Starr John_Lennon Paul_McCartney George_Harrison",
             "Queen Anne was the daughter of which English Monarch?James_II Henry_VIII Victoria William_I",
             "Who composed 'Rhapsody in Blue'?George_Gershwin Irving_Berlin Aaron_Copland Cole_Porter",
             "What is the Celsius equivalent of 77 degrees Fahrenheit?25 15 20 30",
             "What are Suffolk Punch and Hackney?Horse Carriage Wrestling_style Cocktail",
             "Which Shakespeare play features the line 'Neither a borrower nor a lender be'?Hamlet Macbeth Othello The_Merchant_of_Venice",
             "Which is the largest city in the USA's largest state?Anchorage Dallas Los_Angeles New_York",
             "Where would a 'peruke' be worn?On_the_head Around_the_neck On_the_head Around_the+waist On_the_wrist",
             "In which palace was Queen Elizabeth I born?Greenwich Richmond Hampton_Court Kensington",
             "From which author's work did scientists take the word 'quark'?James_Joyce Lewis_Carroll Edward_Lear Aldous_Huxley",
             "Which of these islands was ruled by Britain from 1815 until 1864?Corfu Crete Cyprus Corsica",
             "In the UK, the abbreviation NHS stands for National what Service?Health Humanity Honour Household",
             "Which Disney character famously leaves a glass slipper behind at a royal ball?Cinderella Pocahontas Sleeping_Beauty Elsa",
             "Which of these brands was chiefly associated with the manufacture of household locks?Chubb Phillips Flymo Ronseal",
             "The hammer and sickle is one of the most recognisable symbols of which political ideology?Communism Republicanism Conservatism Liberalism",
             "Which toys have been marketed with the phrase 'robots in disguise'?Transformers Bratz_Dolls Sylvanian_Families Hatchimals",
             "In Ancient Egyptian Mythology, Who Was The God Of The Sun?Ra Osiris Horus Geb"]

question_len = len(questions)
mx_questions = 10
right_answers = 0

print("Welcome to the game 'Who wants to be a millionaire'")

for i in range(1, mx_questions + 1):
    rand_id = randrange(question_len)
    print(f"\n{i}. {questions[rand_id][:questions[rand_id].find('?') + 1]}\n")
    variants = questions[rand_id][questions[rand_id].find('?') + 1:].split()
    shuffle(variants)
    print("A.", *variants[0].split('_'), "\tB.", *variants[1].split('_'), "\tC.", *variants[2].split('_'), "\tD.", *variants[3].split('_'), "\n")
    answer = input("Please answer A, B, C or D: ").lower()
    while answer not in 'abcd' or answer in '':
        print("Wrong answer!!")
        answer = input("Please answer A, B, C or D: ").lower()

    answer = ord(answer) - 97
    if variants[answer] == questions[rand_id][questions[rand_id].find('?') + 1:].split()[0]:
        right_answers += 1
    else:
        print("Game over")
        break
    del questions[rand_id]
    question_len -= 1


print(f"\nRight answers: {right_answers}\n")

