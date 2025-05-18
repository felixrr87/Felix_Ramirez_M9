from flask_login import LoginManager, UserMixin

# Inicializamos el login manager
login_manager = LoginManager()

# Modelo de usuario para la autenticación
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Cargar usuario por ID
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

