class BasicWord:
    def __init__(self, original_word, word_list):
        self.original_word = original_word
        self.word_list = word_list

    def __repr__(self):
        return f"{self.original_word, self.word_list}"

    def verify(self, user_word):
        '''проверку введенного слова в списке допустимых подслов'''
        self.user_word = user_word
        for word in self.word_list:
            if user_word == word:
                return True
        return False

    def coun(self):
        '''подсчет количества подслов'''
        return int(len(self.word_list))