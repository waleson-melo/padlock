import src.model.loginModel as lm


class LoginController:
    def __init__(self):
        self.lgm = lm.LoginModel()

    def validateAccess(self, nome, senha):
        return self.lgm.validate(nome, senha)
