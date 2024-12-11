from model.tugasModel import TugasModel

class TugasViewModel:
    def __init__(self, username):
        self.model = TugasModel(username)
    
    def add_tugas(self, date, matkul, judul, desc, diff, dl):
        return self.model.add_tugas(date, matkul, judul, desc, diff, dl)
    
    def get_tugas(self):
        return self.model.get_tugas()
    
    def selesai_tugas(self, tugasID):
        return self.model.selesai_tugas(tugasID)