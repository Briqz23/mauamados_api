import smtplib
import email.message
def is_user_over_eighteen(user_age) ->bool:
    return user_age>=18

def validate_password(senha) -> bool:
    return len(senha) >= 8

def validar_login(login) -> bool:
    return '@maua.br' in login
#https://www.youtube.com/watch?v=S465v4mWsRg
def send_mail(login) -> str:
    sender = 'danielbriquez@gmail.com'
    receivers = [login]
    message = """ From: From Person %s
    To: To Person %s
    Obrigado por criar sua conta no Mauamados! Você pode usar o app ou o nosso site do MAUÁmados para encontrar o seu par perfeito!
    Caso não tenha sido você ou não tenha interesse em prosseguir com sua conta, entre em contato conosco para deletarmos seus dados, conforme protegido pela LGPD.

    Att. equipe MAUÁmados
    """ % (sender, receivers)

    with smtplib.SMTP('host', 587) as server: 
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('username', 'password')
        server.sendmail(sender, receivers, message)
    return ('Email enviado com sucesso')