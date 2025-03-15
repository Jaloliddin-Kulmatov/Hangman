import random


words = ['olma', 'stul', 'banan', 'stol', 'gitara', 'okean', 'qalam', 'deraza', 'ko‘zgu', 'shisha',
'chiroq', 'adyol', 'sham', 'daftar', 'soyabon', 'kapalak', 'soat', 'chamadon', 'qulupnay', 'tog‘',
'klaviatura', 'rasm', 'televizor', 'ryukzak', 'gilam', 'shokolad', 'kaktus', 'yostiq', 'magnit', 'jirafa',
'skeytbord', 'naushnik', 'kamera', 'hamyon', 'narvon', 'jumboq', 'teleskop', 'sayyora', 'ajdaho', 'sviter',
'olmos', 'favvora', 'hamster', 'vulqon', 'sendvich', 'vertolyot', 'to‘tiqush', 'tarvuz', 'kompas', 'stapler',
'quyosh ko‘zoynak', 'kamalak', 'orol', 'kamin', 'oy', 'qal’a', 'kubok', 'mikroskop', 'avokado', 'lift',
'basketbol', 'fonar', 'meduza', 'qalampir', 'dengiz chig‘anog‘i', 'marafon', 'kanguru', 'popkorn', 'lug‘at', 'qoshiq',
'kit', 'zanjirli ilgak', 'xazina', 'samolyot', 'kungaboqar', 'pingvin', 'saksofon', 'batut', 'karusel', 'kokos',
'qor odam', 'chayon', 'meteor', 'mo‘ri', 'piramida', 'skripka', 'fonus', 'robot', 'tırtıl', 'sharshara',
'toster', 'mushakbozlik', 'haykal', 'gorilla', 'aysberg', 'suvosti kemasi', 'dolchin', 'sharcha', 'chizma', 'limon'  ]

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
random_word = random.choice(words)
 #print(random_word)
word_length = len(random_word)
display_list = []
lives = 6

Game_over = False

while not Game_over:
    display = ""
    guess = str(input("Guess a letter: ")).lower()

    if guess in display_list:
        print(f"You've already guessed {guess}")

    for letter in random_word:
        if letter == guess:
            display += letter
            display_list += letter

        elif letter in display_list:
            display += letter
        else:
            display += "_"
    if guess not in random_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print(f"IT WAS <{random_word}>! YOU LOSE")
            Game_over = True
    print(stages[lives])
    print(display)
    print(f"****************************<{lives}>/6 LIVES LEFT****************************")




    if "_" not in display:
        print("You won")

