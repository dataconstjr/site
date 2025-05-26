import smtplib
from email.message import EmailMessage
import os

__all__ = ['enviar_emails']

def enviar_emails(senha, remetente, destinatarios, assunto, corpo_base, anexos):
    for destinatario in destinatarios:
        nome_destinatario = destinatario["nome"]
        email_destinatario = destinatario["email"]

        # Cria o objeto e-mail e atribui assunto, remetente e email do destinatario
        email = EmailMessage()
        email["Subject"] = assunto
        email["From"] = remetente
        email["To"] = email_destinatario

        # Corpo do e-mail (personalizado pelo nome do destinatário)
        corpo = corpo_base.format(nome=nome_destinatario)
        email.set_content(corpo)

        # Carregando os anexos
        for caminho_anexo in anexos:
            with open(caminho_anexo, "rb") as f:
                # Carregando o arquivo (em binario) e o nome do arquivo
                arquivo = f.read()
                nome_arquivo = os.path.basename(caminho_anexo)
                # Adicionando o anexo
                email.add_attachment(arquivo, filename=nome_arquivo, maintype="application", subtype="octet-stream")

        # Enviar
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(remetente, senha)
            smtp.send_message(email)
            #print(f"📨 E-mail enviado para {nome_destinatario} <{email_destinatario}>")

if __name__ == "__main__":
    # Test code here if needed
    pass