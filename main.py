from utils import load_random_word
from players import *

print("What's you name ?")
name = input()
name_player = Player(name)
word = load_random_word()


print(f"Hi, {name}")
print(f"Составьте {word.coun()} слов из слова {word.original_word}")
print("Слова должны быть не короче 3 букв")
print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
print(" Поехали, ваше первое слово?")

while name_player.used_coun() != word.coun():
    user_answer = input()
    if user_answer == "stop" or user_answer == "стоп":
        break
    elif len((user_answer)) < 3:
        print("слишком короткое слово")
        continue
    elif word.verify(user_answer) == False:
        print("неверно")
        continue
    elif name_player.twise_used(user_answer) == True:
        print("уже использовано")
        continue
    else:
        name_player.used_word_list.append(user_answer)
        print("верно")

print(f"Игра завершена, вы угадали {name_player.used_coun()} слов!")






