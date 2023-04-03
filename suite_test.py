import unittest
import HtmlTestRunner

from test_login import TestLogin
from test_order import TestOrder
from test_place_order import TestPlaceOrder
from test_site import TestSite


class TestSuite(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPlaceOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSite)
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
            (
                combine_reports=True,
                report_title='TestReport',
                report_name='Test Result'
            )

        runner.run(teste_de_rulat)
