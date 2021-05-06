class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def setNome(self, nome):
        self.nome = nome

    def setDataNascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento

    def getNome(self):
        return self.nome

    def getDataNascimento(self):
        return self.data_nascimento