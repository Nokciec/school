class User():
	
	def __init__(
		self,
		login,
		password,
		employee_id,
		is_admin
		):
		self.login = login
		self.password = password
		self.employee_id = employee_id
		self.is_admin = is_admin
		

	@classmethod
	def empty(cls):
		"""
		Empty constructor, use only when the object is about to get loaded from database
		"""
		return cls(None, None, None, None)
