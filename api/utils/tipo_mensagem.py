def DefineTratamentoMensagem(data):
    tipoMensgem = data.get("data",{}).get("messageType",{})
    options = {
        'audioMessage': mensagemAudio,
        'imageMessage': mensagemTexto,
        'conversation': mensagemImagem,
        'extendedTextMessage': mensagemTextoExtendido
    }



def mensagemTexto(remote_jid, text):
    print(f"RemoteJID: {remote_jid} Text: {text}")

def mensagemTextoExtendido(remote_jid, text):
    print(f"RemoteJID: {remote_jid} Text: {text}")

def mensagemImagem(remote_jid, base64):
    print(f"RemoteJID: {remote_jid} Base64: {base64}")

def mensagemAudio(remote_jid, base64):
    print(f"RemoteJID: {remote_jid} Base64: {base64}")    

