import unittest
import json
from unittest.mock import patch, MagicMock
from lmctl.client.api import BehaviourScenariosAPI
from lmctl.client.client_request import TNCOClientRequest

class TestBehaviourScenariosAPI(unittest.TestCase):

    def setUp(self):
        self.mock_client = MagicMock()
        self.behaviour_scenarios = BehaviourScenariosAPI(self.mock_client)

    def test_all_in_project(self):
        mock_response = [{'id': 'Test', 'name': 'Test'}]
        self.mock_client.make_request.return_value.json.return_value = mock_response
        response = self.behaviour_scenarios.all_in_project('Test')
        self.assertEqual(response, mock_response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest.build_request_for_json(method='GET', endpoint='api/behaviour/scenarios', query_params={'projectId': 'Test'}))

    def test_get(self):
        mock_response = {'id': 'Test', 'name': 'Test'}
        self.mock_client.make_request.return_value.json.return_value = mock_response
        response = self.behaviour_scenarios.get('Test')
        self.assertEqual(response, mock_response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest.build_request_for_json(method='GET', endpoint='api/behaviour/scenarios/Test'))

    def test_create(self):
        test_obj = {'name': 'Test'}
        body = json.dumps(test_obj)
        mock_response = MagicMock(headers={'Location': '/api/behaviour/scenarios/123'})
        self.mock_client.make_request.return_value = mock_response
        response = self.behaviour_scenarios.create(test_obj)
        self.assertEqual(response, {'id': '123', 'name': 'Test'})
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='POST', endpoint='api/behaviour/scenarios', headers={'Content-Type': 'application/json'}, body=body))

    def test_update(self):
        test_obj = {'id': '123', 'name': 'Test'}
        body = json.dumps(test_obj)
        response = self.behaviour_scenarios.update(test_obj)
        self.assertIsNone(response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='PUT', endpoint='api/behaviour/scenarios/123', headers={'Content-Type': 'application/json'}, body=body))

    def test_delete(self):
        response = self.behaviour_scenarios.delete('123')
        self.assertIsNone(response)
        self.mock_client.make_request.assert_called_with(TNCOClientRequest(method='DELETE', endpoint='api/behaviour/scenarios/123'))
    

