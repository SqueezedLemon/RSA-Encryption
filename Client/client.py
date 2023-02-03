import requests
import os
import rsa

os.environ['NO_PROXY'] = '127.0.0.1'
serverPublicKey = requests.get('http://127.0.0.1:5000/getkey')
key = serverPublicKey.content
pk = key.replace(b'\\n', b'\n').decode('ascii')
pk = pk[1:] 
pk = pk[:-1]
key = rsa.PublicKey.load_pkcs1(pk)
loop = 'Y'

while (loop == 'Y'):
    print ("Enter your message to server\n")
    msg = input()
    encryptedMsg = rsa.encrypt(msg.encode(), key)
    print ("Message being sent to server:",encryptedMsg,'\n')
    server = requests.post('http://127.0.0.1:5000/msg', data = encryptedMsg)
    server = str(server.content)
    print (server[1:])
    print("\n Do you want to send another message to server(Y/N)")
    loop = input().upper()