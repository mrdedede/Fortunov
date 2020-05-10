import random

class MarkovGraph:
    def __init__(self, adjacency_list = {'': {}}, cur_state = None):
        self.adjacency_list = adjacency_list
        if cur_state:
            self.cur_state = cur_state
        else:
            self.cur_state = ''
    
    def add_link(self, previous_word, new_word):
        try:
            self.adjacency_list[previous_word][new_word] += 1
        except KeyError:
            try:
                self.adjacency_list[previous_word][new_word] = 1
            except KeyError:
                self.adjacency_list[previous_word] = {new_word: 1}
    
    def next_state(self):
        try:
            possibilities = list(self.adjacency_list[self.cur_state].keys())
            choice_list = []
            for possibility in possibilities:
                for index in range(self.adjacency_list[self.cur_state][possibility]):
                    choice_list.append(possibility)
            self.cur_state = random.choice(choice_list)
        except KeyError:
            self.cur_state = ''
        return self.cur_state