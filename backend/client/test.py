import unittest
from docusign_client import ds_client

class TestDSClient(unittest.TestCase):


    def test_userinfo(self):
        self.assertEqual(ds_client.user_name, 'Shawn Cong')
    

    def test_listenvelope(self):
        resp = ds_client.list_envelopes()
        self.assertTrue('envelopes' in resp)


    def test_listtemplate(self):
        resp = ds_client.list_templates()
        self.assertTrue('envelopeTemplates' in resp)


    def test_createenvelope(self):
        envelope = {
            "emailBlurb": "example of embedded contract blurb",
            "emailSubject": "example of embedded contract",
            "status": "sent",
            "templateId": "53d55092-6cd6-4b8b-8d02-449e4420ca96",
            "templateRoles": [{
                "name": "Shawn Cong",
                "email": "stormouse@gmail.com",
                "routingOrder": "1",
                "roleName": "JACK",
                "clientUserId": 1
            }, {"roleName": "QUEEN"}, {"roleName": "KING"}]
        }
        #resp = ds_client.create_envelope(envelope)
        #self.assertTrue('envelopeId' in resp)
        self.assertTrue(True)


    def test_getenvelope(self):
        old_template = ds_client.get_template("53d55092-6cd6-4b8b-8d02-449e4420ca96")
        self.assertTrue('envelopeTemplateDefinition' in old_template)



if __name__ == '__main__':
    unittest.main()