class Player:
    def __init__(self, user_name):
        self.user_name = user_name
        self.used_word_list = []

    def __repr__(self):
        return f"{self.user_name,self.used_word_list}"

    def used_coun(self):
        '''получение количества использованных слов'''
        return int(len(self.used_word_list))

    def ap_in_spisok_used_word(self, user_word):
        '''добавление слова в использованные слова'''
        self.used_word_list.append(user_word)

    def twise_used(self, user_word):
        '''проверка использования данного слова до этого'''
        for word in self.used_word_list:
            if user_word == word:
                return True
        return False