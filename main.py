import random


words = ['apple', 'chair', 'banana', 'table', 'guitar', 'ocean', 'pencil', 'window', 'mirror', 'glass',
'light', 'blanket', 'candle', 'notebook', 'umbrella', 'butterfly', 'clock', 'suitcase', 'strawberry', 'mountain',
'keyboard', 'picture', 'television', 'backpack', 'carpet', 'chocolate', 'cactus', 'pillow', 'magnet', 'giraffe',
'skateboard', 'headphones', 'camera', 'wallet', 'ladder', 'puzzle', 'telescope', 'planet', 'dragon', 'sweater',
'diamond', 'fountain', 'hamster', 'volcano', 'sandwich', 'helicopter', 'parrot', 'watermelon', 'compass', 'stapler',
'sunglasses', 'rainbow', 'island', 'fireplace', 'moon', 'castle', 'trophy', 'microscope', 'avocado', 'elevator',
'basketball', 'flashlight', 'jellyfish', 'pepper', 'seashell', 'marathon', 'kangaroo', 'popcorn', 'dictionary', 'spoon',
'whale', 'hook', 'treasure', 'airplane', 'sunflower', 'penguin', 'saxophone', 'trampoline', 'carousel', 'coconut',
'snowman', 'scorpion', 'meteor', 'chimney', 'pyramid', 'violin', 'lantern', 'robot', 'caterpillar', 'waterfall',
'toaster', 'fireworks', 'statue', 'gorilla', 'iceberg', 'submarine', 'cinnamon', 'ball', 'drawing', 'lemon']

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
