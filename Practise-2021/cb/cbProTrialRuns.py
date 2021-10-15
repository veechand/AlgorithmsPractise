import cbpro
from constants import cbPassphrase, cbApiSecret, cbProPublicKey

class MyTradingPlatform(object):
	def __init__(self, client):
		self.client = client
	"""
	 Gets the list of available products for the provided client
	 Returns :
	   list: of string Representing the ID of the product
	   Example: ["BTC-USD", "ETH-USD"]
	"""
	def get_available_products(self):
		products = self.client.get_products()
		return map(lambda x:x["id"], products)
	"""
	  Get the order book for a particular product. For details about
	  levels refer <link>
	  Return:  dict
	"""
	def get_product_order_book(self, product_id):
		return self.client.get_product_order_book(product_id, level=1)

	def buy(self, price, size, order_type, product_id):
		return self.client.buy(product_id, order_type, price=price, size=size)

	def get_order_details(self, order_id):
		return self.client.get_order(order_id)

if __name__ == "__main__":
	public_client = cbpro.PublicClient()

	# products = myTradingPlatform.get_available_products(public_client)
	# print(products)
	# order_book = myTradingPlatform.get_product_order_book(public_client, "BTC-USD")
	# print(order_book)
	auth_client = cbpro.AuthenticatedClient(cbProPublicKey, 
											cbApiSecret, 
											cbPassphrase,
											api_url="https://api-public.sandbox.pro.coinbase.com")
	myTradingPlatform = MyTradingPlatform(auth_client)
	# available_products = myTradingPlatform.get_available_products(auth_client)
	# print(available_products)
	# order_details = myTradingPlatform.buy(auth_client, '100.0', '0.01', 'limit', 'BTC-USD')
	# print(order_details)
	order_details = myTradingPlatform.get_order_details("21f534d1-0aa6-423b-98cd-99981fd5988e")
	print(order_details)
