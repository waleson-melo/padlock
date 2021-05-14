import src.model.senhasModel as sm


class SenhasController:
    def __init__(self):
        self.senhas_model = sm.SenhasModel()

    def searchAllSenhas(self):
        return self.senhas_model.selectAll()

    def searchSenha(self, nome):
        return self.senhas_model.select(nome)

    def saveSenha(self, nome, login, senha):
        return self.senhas_model.save(nome, login, senha)

    def updateSenha(self, codigo, nome, login, senha):
        return self.senhas_model.update(codigo, nome, login, senha)

    def deleteSenha(self, codigo):
        return self.senhas_model.delete(codigo)
