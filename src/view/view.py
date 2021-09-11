import PySimpleGUI as sg


thema = 'DefaultNoMoreNagging'

button_size = (5,1)
input_size = (19,1)

# Constroi a Tela de Login
def login_view():
    sg.theme(thema)

    frame_image = [
        [sg.Image('img/user.png', expand_y=True)]
    ]
    col_dados = [
        [sg.Text('Nome:')],
        [sg.Input('', key='-NOMELOGIN-', size=input_size, focus=True)],

        [sg.Text('Senha:')],
        [sg.Input('', key='-SENHALOGIN-',size=input_size, password_char='*')],

        [sg.Button('Entrar', size=button_size, bind_return_key=True),
            sg.Button('Sair', size=button_size, button_color=('','red'))]
    ]
    layout = [
        [sg.Frame('', frame_image, expand_y=True), sg.Column(col_dados)]
    ]
    return sg.Window('Entrar no Sistema', layout, finalize=True)

#==============================================================================

# Constroi a Tela Principal
def main_view(list_senhas=[]):
    sg.theme(thema)
    # Tabs
    text_size = (6,1)
    tab1_layout = [
        [sg.Input(size=(29,1), enable_events=True, focus=True,
            key='-INPPROCURARSENHA-'), sg.Button('Atualizar', size=(5,1))],
        [sg.Listbox(list_senhas, size=(38,10), enable_events=True,
            key='-LBXSENHA-')],
        [sg.Button('Novo', size=button_size), sg.Button('Logoff',
            size=button_size, button_color=('','red'))],
    ]
    tab2_layout = [
        [sg.Text('ID:', size=text_size), sg.Input(key='-INPIDUSUARIO-',
            size=input_size, disabled=True)],
        [sg.Text('Nome:', size=text_size), sg.Input(key='-INPNOMEUSUARIO-',
            size=input_size)],
        [sg.Text('Senha:', size=text_size), sg.Input(key='-INPSENHAUSUARIO-',
            size=input_size, password_char='*')],
        [sg.Text('Senha*:', size=text_size), sg.Input(key='-INPSENHA*USUARIO-',
            size=input_size, password_char='*')],

        [sg.Checkbox('Para editar marque a aqui.', default=False,
            enable_events=True, key='-CHBEDITARUSUARIO-')],
        [sg.Button('Editar', size=button_size)],
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

#==============================================================================

# Janela para adcionar senha
def new_senha():
    sg.theme(thema)
    text_size = (6,1)
    input_size = (29,1)
    layout = [
        [sg.Text('Nome:', size=text_size), sg.Input('', size=input_size,
            tooltip='App, Plataforma, Site, etc...', focus=True,
            key='-INPNOMESENHA-')],
        [sg.Text('Login:', size=text_size), sg.Input(size=input_size,
            key='-INPLOGINSENHA-')],
        [sg.Text('Senha:', size=text_size), sg.Input(size=input_size,
            key='-INPSENHASENHA-')],

        [sg.Text('', size=text_size), sg.Button('Salvar', size=button_size, 
            bind_return_key=True), sg.Button('Limpar', size=button_size),
            sg.Button('Cancelar', size=button_size, button_color=('','red'))],
    ]
    return sg.Window('Nova Senha', layout, finalize=True)

#==============================================================================

# Janela para alterar e apagar senha
def view_del_update_senha(dados_senha=['','','','']):
    sg.theme(thema)
    text_size = (6,1)
    layout = [
        [sg.Text('ID:', size=text_size), sg.Input(dados_senha[0], size=(29,1),
            disabled=True, key='-INPIDDELUPSENHA-')],
        [sg.Text('Nome:', size=text_size), sg.Input(dados_senha[1], 
            size=(29,1), key='-INPNOMEDELUPSENHA-', focus=True)],
        [sg.Text('Login:', size=text_size), sg.Input(dados_senha[2],
            size=(29,1), key='-INPLOGINDELUPSENHA-')],
        [sg.Text('Senha:', size=text_size), sg.Input(dados_senha[3],
            size=(29,1), key='-INPSENHADELUPSENHA-')],

        [sg.Button('Salvar', size=button_size, bind_return_key=True),
            sg.Button('Limpar', size=button_size), sg.Button('Apagar',
            size=button_size, button_color=('','red')),
            sg.Button('Cancelar', size=button_size, button_color=('','red'))],
    ]
    return sg.Window('Visualizar, Alterar ou Apagar', layout, finalize=True)