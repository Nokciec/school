import CONSTANTS
from .models import Users
from User import User

class LoginManager:
	@staticmethod
	def authenticate(login, password):

		users_data = Users.objects.all()

		for user_id in users_data:

			user = User.empty()
			
			if user.login == login:
				if user.password == password:
					if user.is_admin:
						return CONSTANTS.LOGIN_ADMIN
					else:
						return CONSTANTS.LOGIN_CLIENT

				else:
					return CONSTANTS.LOGIN_FAILED

		return CONSTANTS.LOGIN_FAILED
