import unittest
from mock import MagicMock, Mock
from cbpro import PublicClient, AuthenticatedClient
from cbProTrialRuns import MyTradingPlatform

class TradingPlatformTest(unittest.TestCase):
	def setUp(self):
		self.client = Mock()
		self.client.get_products.return_value = [
                    {
                        "id": "BTC-USD",
                        "display_name": "BTC/USD",
                        "base_currency": "BTC",
                        "quote_currency": "USD",
                        "base_min_size": "0.01",
                        "base_max_size": "10000.00",
                        "quote_increment": "0.01"
                    }
                ] 
		self.auth_client = Mock()
		self.trading_platform = MyTradingPlatform()

	def test_get_available_products(self):
		output = self.trading_platform.get_available_products(self.client)
		self.assertEqual(len(output), 1)


if __name__ == '__main__':
    unittest.main()


"""
pip install mock
pip install unittest2
"""