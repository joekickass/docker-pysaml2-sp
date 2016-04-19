from saml2.assertion import Policy
import saml2.xmldsig as ds

HOST = "localhost"
PORT = 8088
HTTPS = True
SERVER_CERT = "sp.crt"
SERVER_KEY = "sp.key"
CERT_CHAIN = ""
SIGN_ALG = ds.SIG_RSA_SHA512
DIGEST_ALG = ds.DIGEST_SHA512

POLICY = Policy({})
