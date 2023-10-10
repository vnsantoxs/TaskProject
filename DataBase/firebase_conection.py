import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("./Pytask.json")

firebase_admin.initialize_app(cred)


def login_with_email_and_password(email, password):
    try:
        user = auth.get_user_by_email(email)
        user = auth.sign_in_with_email_and_password(email, password)
        print("Login bem-sucedido!")
        return user
    except:
        print(f"Erro de autenticação")
        return None


def check_authentication(user_token):
    try:
        decoded_token = auth.verify_id_token(user_token)
        uid = decoded_token['uid']
        return uid
    except:
        print(f"Erro de autenticação")
        return None


def send_password_reset_email(email):
    try:
        auth.generate_password_reset_link(email)
        print("Email de redefinição de senha enviado com sucesso!")
        return True
    except:
        print(f"Erro ao enviar o email de redefinição de senha")
        return False


def create_user_with_email_and_password(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print("Usuário criado com sucesso!")
        return user.uid
    except:
        print(f"Erro ao criar usuário:")
        return None


email = "viniciusmelchior.vmls@gmail.com"
senha = "#VMelchior1912"
user1 = create_user_with_email_and_password(email, senha)
user2 = login_with_email_and_password(email, senha)
user3 = send_password_reset_email(email)
use4 = check_authentication("pvpW8m2PZsUU1n8ao1ooahQzrGq1")
