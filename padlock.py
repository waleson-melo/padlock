import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup, popup_yes_no
from src.view.view import *

import src.controller.loginController as lgc
import src.controller.senhasController as sec
import src.controller.usuarioController as usc

# Objetos
login_controller = lgc.LoginController()
senhas_controller = sec.SenhasController()
usuario_controller = usc.UsuarioController()


nome_senhas = []
def get_senhas():
    # Pegando as senhas do banco
    senhas = senhas_controller.searchAllSenhas()
    for i in senhas:
        nome_senhas.append(i[1])
    return nome_senhas

def get_usuario():
    # Pegando o usuario do banco
    usuario = usuario_controller.searchAllUsuarios()
    return usuario[0]

# Inicializa as variaveis da janelas
win_login, win_main, win_new_senha, win_view_del_update_senha = login_view(), None, None, None

# Laço principal de repetição
while True:
    window, event, values = sg.read_all_windows()

    # Funçõs de fechamento das janelas
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        if sg.popup_yes_no('Você deseja realmente sair?') == 'Yes':
            break

#========================================================================================

    # Funções da Janela de Login
    if window == win_login and event == 'Entrar':
        cond_login = [
            values['-NOMELOGIN-'] != '',
            values['-SENHALOGIN-'] != '',
        ]
        if all(cond_login):
            ret_validate = login_controller.validateAccess(values['-NOMELOGIN-'],
                values['-SENHALOGIN-'])
            if ret_validate:
                if win_main !=None:
                    win_main.un_hide()
                else:
                    win_main = main_view(get_senhas())
                win_login.hide()
            else:
                sg.popup('Nome ou Senha não conferem. Tente novamente.')
        else:
            sg.popup('Preencha os campos.')

#========================================================================================

    # Funçoes da Janela Principal
    if window == win_main:
        # Condição de Logoff
        if event == 'Logoff':
            if sg.popup_yes_no('Você deseja realmente fazer Logoff?') == 'Yes':
                win_main.hide()
                # win_main = None
                win_login.un_hide()
            
        if event == 'Novo':
            win_new_senha = new_senha()
            win_main.hide()

        # Searchbox, procurar as senhas enquanto digita
        if values['-INPPROCURARSENHA-'] != '':
            search = values['-INPPROCURARSENHA-'].upper()
            new_search = [x for x in nome_senhas if search in x]
            win_main['-LBXSENHA-'].update(new_search)
        else:
            try:
                win_main['-LBXSENHA-'].update(nome_senhas)
            except:
                pass
        
        if event == 'Atualizar':
            nome_senhas = []
            get_senhas()
            win_main['-LBXSENHA-'].update(nome_senhas)
            sg.popup('Lista atualizada.')
    
        # Evento da seleção de uma senha na listbox
        if event == '-LBXSENHA-' and len(values['-LBXSENHA-']):
            senha = values['-LBXSENHA-']
            dados_senha = senhas_controller.searchSenha(senha[0])
            if dados_senha != None:
                win_view_del_update_senha = view_del_update_senha(dados_senha[0])
                win_main.hide()
            else:
                sg.popup('Erro ao selecionar senha, tente atualizar a lista.')
    
        # # Pegando o usuario do banco e colocando nos campos para edição
        if values['-INPIDUSUARIO-'] == '':
            usuario = get_usuario()
            window['-INPIDUSUARIO-'].update(str(usuario[0]))
            window['-INPNOMEUSUARIO-'].update(str(usuario[1]))
            window['-INPSENHAUSUARIO-'].update(str(usuario[2]))
        
        # Editar usuario
        if values['-CHBEDITARUSUARIO-']:
            window['Editar'].update(disabled=False)
            window['-INPNOMEUSUARIO-'].update(disabled=False)
            window['-INPSENHAUSUARIO-'].update(disabled=False)
            window['-INPSENHA*USUARIO-'].update(disabled=False)
            if event == 'Editar':
                cond_usuario = [
                    values['-INPNOMEUSUARIO-'] != '',
                    values['-INPSENHAUSUARIO-'] != '',
                    values['-INPSENHA*USUARIO-'] != '',
                ]
                if all(cond_usuario):
                    if values['-INPSENHAUSUARIO-'] == values['-INPSENHA*USUARIO-']:
                        ret_update_usuario = usuario_controller.updateUsuario(values['-INPIDUSUARIO-'],
                            values['-INPNOMEUSUARIO-'], values['-INPSENHAUSUARIO-'])
                        if ret_update_usuario[0]:
                            window['Editar'].update(disabled=False)
                            window['-INPNOMEUSUARIO-'].update(disabled=False)
                            window['-INPSENHAUSUARIO-'].update(disabled=False)
                            window['-CHBEDITARUSUARIO-'].update(False)
                            window['-INPSENHA*USUARIO-'].update(False)
                            window['-TAB1SENHA-'].select()
                            sg.popup('Usuário alterado com sucesso.')
                        else:
                            sg.popup_error('Erro ao atualizar usuário.',
                                str(ret_update_usuario[1]))
                    else:
                        sg.popup('As senhas são diferentes.')
                else:
                    sg.popup('Preencha os campos.')
        else:
            window['Editar'].update(disabled=True)
            window['-INPNOMEUSUARIO-'].update(disabled=True)
            window['-INPSENHAUSUARIO-'].update(disabled=True)
            window['-INPSENHA*USUARIO-'].update(disabled=True)

#========================================================================================

    # Funções da Janela Nova senha
    if window == win_new_senha:
        if event == 'Cancelar':
            if sg.popup_yes_no('Deseja mesmo cancelar?') == 'Yes':
                win_new_senha.close()
                win_new_senha = None
                win_main.un_hide()
        
        if event == 'Salvar':
            cond_save = [
                values['-INPNOMESENHA-'] != '',
                values['-INPLOGINSENHA-'] != '',
                values['-INPSENHASENHA-'] != '',
            ] 
            if all(cond_save):
                ret_save_senha = senhas_controller.saveSenha(values['-INPNOMESENHA-'].upper(),
                    values['-INPLOGINSENHA-'], values['-INPSENHASENHA-'])
                
                if ret_save_senha[0]:
                    sg.popup('Senha salva com sucesso.')
                    win_new_senha.close()
                    win_new_senha = None
                    win_main.un_hide()
                else:
                    sg.popup_error('Erro ao salvar senha.', str(ret_save_senha[1]))
            else:
                sg.popup('Preencha os campos!')

        if event == 'Limpar':
            window['-INPNOMESENHA-'].update('')
            window['-INPLOGINSENHA-'].update('')
            window['-INPSENHASENHA-'].update('')

#========================================================================================

    # Funçoes da Janela View del update
    if window == win_view_del_update_senha:
        if event == 'Cancelar':
            if sg.popup_yes_no('Deseja mesmo cancelar?') == 'Yes':
                win_view_del_update_senha.close()
                win_view_del_update_senha = None
                win_main.un_hide()

        if event == 'Limpar':
            window['-INPNOMEDELUPSENHA-'].update('')
            window['-INPLOGINDELUPSENHA-'].update('')
            window['-INPSENHADELUPSENHA-'].update('')

        if event == 'Salvar':
            cond = [
                values['-INPNOMEDELUPSENHA-'] != '',
                values['-INPLOGINDELUPSENHA-'] != '',
                values['-INPSENHADELUPSENHA-'] != '',
            ] 
            if all(cond):
                ret_update_senha = senhas_controller.updateSenha(values['-INPIDDELUPSENHA-'],
                    values['-INPNOMEDELUPSENHA-'].upper(), values['-INPLOGINDELUPSENHA-'],
                    values['-INPSENHADELUPSENHA-'])
                if ret_update_senha[0]:
                    sg.popup('Senha salva com sucesso.')
                    win_view_del_update_senha.close()
                    win_view_del_update_senha = None
                    win_main.un_hide()
                else:
                    sg.popup_error('Erro ao salvar senha', str(ret_update_senha[1]))
            else:
                sg.popup('Preencha os campos!')

        if event == 'Apagar':
            if popup_yes_no('Deseja apagar a senha?') == 'Yes':
                ret_delete_senha = senhas_controller.deleteSenha(values['-INPIDDELUPSENHA-'])
                if ret_delete_senha[0]:
                    sg.popup('Senha apagada com sucesso.')
                    win_view_del_update_senha.close()
                    win_view_del_update_senha = None
                    win_main.un_hide()
                else:
                    sg.popup('Erro ao apagar a senha', str(ret_delete_senha[1]))

window.close()
