import src.model.usuarioModel as um


class UsuarioController:
    def __init__(self):
        self.usuario_model = um.UsuarioModel()

    def searchAllUsuarios(self):
        return self.usuario_model.selectAll()

    def searchUsuario(self, codigo):
        return self.usuario_model.select(codigo)

    def saveUsuario(self, nome, senha):
        return self.usuario_model.save(nome, senha)

    def updateUsuario(self, codigo, nome, senha):
        return self.usuario_model.update(codigo, nome, senha)

    def deleteUsuario(self, codigo):
        return self.usuario_model.delete(codigo)
