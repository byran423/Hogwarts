

from utils.utils import Utils

class BaseApi:
	json_data = None
	def jsonpath(self,expr):
		return Utils.jsonpath(self.json_data,expr)


class Wework(BaseApi):
	corpid = 1111
	contact_secret = 1111









