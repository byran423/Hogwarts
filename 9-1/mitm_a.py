from mitmproxy import ctx, addons


class AD:
	def __init__(self):
		self.num = 0

	def request(self,flow):
		self.num += 1
		ctx.log.info(f"我们看到了{self.num}流水")

# mitmproxy插件addons需要添加实例化对象
addons = [
	AD()
]










