import pickle

class Board_manager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.boards = []
    
    def save(self):
        file = open(self.file_name, 'wb')
        pickle.dump(self.boards, file)
        file.close()
    
    def load(self):
        file = open(self.file_name, 'rb')
        self.boards = pickle.load(file)
        file.close()