def exibir_mensagem():
    print("Sistema de Controle de Atendimento - versão atualizada")

def cadastrar_atendimento(beneficiario, procedimento):
    return {
        "beneficiario": beneficiario,
        "procedimento": procedimento
    }

if __name__ == "__main__":
    exibir_mensagem()
