from model.tipsModel import TipsModel

class TipsViewModel:
    def __init__(self):
        self.model = TipsModel()
    
    def tambah_tips(self):
        return self.model.tambah_tips()
    
    def lihat_tips(self):
        return self.model.load_tips_data()