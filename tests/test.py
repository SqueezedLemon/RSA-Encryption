import requests
import os
import rsa
import unittest

class TestMessage(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(msg, server_response)


if __name__ == '__main__':

    os.environ['NO_PROXY'] = '127.0.0.1'
    serverPublicKey = requests.get('http://127.0.0.1:5000/getkey')
    key = serverPublicKey.content
    pk = key.replace(b'\\n', b'\n').decode('ascii')
    pk = pk[1:] 
    pk = pk[:-1]
    key = rsa.PublicKey.load_pkcs1(pk)

    msg = "This is a test message. Hello Server!"
    encryptedMsg = rsa.encrypt(msg.encode(), key)
    server = requests.post('http://127.0.0.1:5000/test', data = encryptedMsg)
    server_response = str(server.content)
    server_response = server_response[2:]
    server_response = server_response[:-1]

    unittest.main()