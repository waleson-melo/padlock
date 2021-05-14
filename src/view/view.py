import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button


thema = 'DefaultNoMoreNagging'

# Constroi a Tela de Login
def login_view():
    sg.theme(thema)

    layout = [
        [sg.Text('Nome:', size=(5, 1)), sg.Input(key='-NOMELOGIN-', 
            size=(19, 1))],
        [sg.Text('Senha:', size=(5, 1)), sg.Input(key='-SENHALOGIN-',
            size=(19, 1), password_char='*')],
        [sg.Text('', size=(5, 1)), sg.Button('Entrar', size=(5, 1)),
            sg.Button('Sair', size=(5, 1))]
    ]
    return sg.Window('Entrar no Sistema', layout, finalize=True)

#========================================================================================

# Constroi a Tela Principal
def main_view(list_senhas=[]):
    sg.theme(thema)
    # Tabs
    tab1_layout = [
        [sg.Input(size=(29,1), enable_events=True, focus=True, key='-INPPROCURARSENHA-'),
            sg.Button('Atualizar', size=(5,1))],
        [sg.Listbox(list_senhas, size=(38,6), enable_events=True,
            key='-LBXSENHA-')],
        [sg.Button('Novo', size=(5, 1)), sg.Button('Logoff', size=(5, 1))],
    ]
    tab2_layout = [
        [sg.Checkbox('Para editar marque a aqui.', default=False, enable_events=True,
            key='-CHBEDITARUSUARIO-')],
        [sg.Text('Id:', size=(5,1)), sg.Input(key='-INPIDUSUARIO-',
            size=(19,1), disabled=True)],
        [sg.Text('Nome:', size=(5, 1)), sg.Input(key='-INPNOMEUSUARIO-',
            size=(19, 1))],
        [sg.Text('Senha:', size=(5, 1)), sg.Input(key='-INPSENHAUSUARIO-',
            size=(19, 1), password_char='*')],
        [sg.Text('Senha*:', size=(5, 1)), sg.Input(key='-INPSENHA*USUARIO-',
            size=(19, 1), password_char='*')],
        [sg.Button('Editar', size=(5, 1))],
    ]
    # Tabs Group
    tab_group_layout = [
        [sg.Tab('Senhas', tab1_layout, key='-TAB1SENHA-')],
        [sg.Tab('Usuário', tab2_layout, key='-TAB2SENHA-')],
    ]

    layout = [
        [sg.TabGroup(tab_group_layout, enable_events=True,
            key='-TABGROUPSENHA-')],
    ]
    return sg.Window('Gerenciador de Senhas', layout, finalize=True)

#========================================================================================

# Janela para adcionar senha
def new_senha():
    sg.theme(thema)

    layout = [
        [sg.Text('Nome:', size=(5, 1)), sg.Input('Plataforma(Ex.: Google, Facebook...)',
            size=(29,1), focus=True, key='-INPNOMESENHA-')],
        [sg.Text('Login:', size=(5, 1)), sg.Input(size=(29,1), focus=True,
            key='-INPLOGINSENHA-')],
        [sg.Text('Senha:', size=(5, 1)), sg.Input(size=(29,1), focus=True,
            key='-INPSENHASENHA-')],
        [sg.Button('Salvar', size=(5,1)), sg.Button('Limpar', size=(5,1)),
            sg.Button('Cancelar', size=(5,1))],
    ]
    return sg.Window('Nova Senha', layout, finalize=True)

#========================================================================================

# Janela para alterar e apagar senha
def view_del_update_senha(dados_senha=['','','','']):
    sg.theme(thema)

    layout = [
        [sg.Text('Id:', size=(5,1)), sg.Input(dados_senha[0], size=(29,1), disabled=True,
            key='-INPIDDELUPSENHA-')],
        [sg.Text('Nome:', size=(5,1)), sg.Input(dados_senha[1], size=(29,1),
            key='-INPNOMEDELUPSENHA-')],
        [sg.Text('Login:', size=(5,1)), sg.Input(dados_senha[2], size=(29,1),
            key='-INPLOGINDELUPSENHA-')],
        [sg.Text('Senha:', size=(5,1)), sg.Input(dados_senha[3], size=(29,1),
            key='-INPSENHADELUPSENHA-')],
        [sg.Button('Salvar', size=(5,1)), sg.Button('Limpar', size=(5,1)),
            sg.Button('Apagar', size=(5,1)), sg.Button('Cancelar', size=(5,1))],
    ]
    return sg.Window('Visualizar, Alterar ou Apagar', layout, finalize=True)