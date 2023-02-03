from flask import Flask
from flask import request
import rsa
import jsonpickle

app = Flask(__name__)

# Generating Private and Public Key of the server.
# Please open the homepage first before running client.

@app.route("/")
def key_generation():
    try:
        file_private = open("private.pem", "r")
        file_public = open("public.pem", "r")

        return "<p>Keys Generated and Server is ready.</p>"
    except:
        file_private = open("private.pem", "w")
        file_public = open("public.pem", "w")
        publicKey, privateKey = rsa.newkeys(2048)
        publicKeyPkcs1PEM = publicKey.save_pkcs1().decode('utf8')
        privateKeyPkcs1PEM = privateKey.save_pkcs1().decode('utf8')
        file_private.write(privateKeyPkcs1PEM)
        file_public.write(publicKeyPkcs1PEM)

        return "<p>Keys Generated and Server is ready.</p>"


@app.route("/msg",methods=['POST'])
def msg():
    file_private = open("private.pem", "r")
    privateKey = rsa.PrivateKey.load_pkcs1(file_private.read())
    msg = request.data
    print (msg)
    decryptMessage = rsa.decrypt(msg, privateKey).decode()
    print("decrypted string: ", decryptMessage)
    response = "Message received by server"
    return (response)

@app.route("/getkey")
def getkey():
    file_public = open("public.pem", "r")
    response = file_public.read()
    return jsonpickle.encode(response)

@app.route("/test",methods=['POST'])
def test():
    file_private = open("private.pem", "r")
    privateKey = rsa.PrivateKey.load_pkcs1(file_private.read())
    msg = request.data
    print (msg)
    decryptMessage = rsa.decrypt(msg, privateKey).decode()
    print("decrypted string: ", decryptMessage)
    return decryptMessage

if __name__ == "__main__":
    app.run(debug=True ,port=8080,use_reloader=False)