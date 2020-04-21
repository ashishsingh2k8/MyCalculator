import json
import sys
import unittest

import rootpath
from flask import Flask
from mock import patch

sys.path.append(rootpath.detect())

from api.myCalculator_V1 import mycalc_blueprint_v1

app = Flask(__name__)
app.register_blueprint(mycalc_blueprint_v1, url_prefix='')

class TestMyCalculatorV1(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_calculate_success_response(self):
        expression = "1 + 1"
        expected = 2.0
        res = self.app.get(
            '/v1/calculate', query_string=dict(expression=expression),
            follow_redirects=True)
        self.assertEqual(res.status, '200 OK')
        self.assertEqual(res.json['result'], expected)

    def test_calculate_failure_response(self):
        expression = "1 + &"
        expected = 2.0
        res = self.app.get(
            '/v1/calculate', query_string=dict(expression=expression),
            follow_redirects=True)
        self.assertEqual(res.json['result'], 'Bad parameters')
        self.assertEqual(res.status_code, 400)

    def test_calculate_failure_response_without_expression(self):
        res = self.app.get(
            '/v1/calculate',
            follow_redirects=True)
        self.assertEqual(res.json['result'], 'No expression found')
        self.assertEqual(res.status_code, 404)

    @patch('api.myCalculator_V1.calulator')
    def test_calculate_with_unknown_exception(self, mock_calculator):
        expression = "1 + 1"
        mock_calculator.run.side_effect = \
            KeyError("Unknown Exception")
        res = self.app.get(
            '/v1/calculate', query_string=dict(expression=expression),
            follow_redirects=True)
        self.assertEqual(res.status, '500 INTERNAL SERVER ERROR')
        self.assertEqual(res.status_code, 500)
        self.assertTrue("Unknown Exception" in str(res.json))