from saml2 import BINDING_HTTP_POST
from saml2.extension.idpdisc import BINDING_DISCO
from saml2.saml import NAME_FORMAT_URI

try:
    from saml2.sigver import get_xmlsec_binary
    xmlsec_path = get_xmlsec_binary(["/opt/local/bin", "/usr/local/bin", "/usr/bin/"])
except ImportError:
    xmlsec_path = '/usr/bin/xmlsec1'

# Make sure the same port number appear in service_conf.py
HOST = "localhost"
PORT = 8088
BASE = "https://%s:%s" % (HOST, PORT)

CONFIG = {
    "entityid": "%s/sp.xml" % BASE,
    "service": {
        "sp": {
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/acs/post" % BASE, BINDING_HTTP_POST)
                ],
            },
            "authn_requests_signed": False,
            "want_assertions_signed": True
        },
    },
    "metadata": {
        "local": ["idp.xml"],
    },
    "key_file": "sp.key",
    "cert_file": "sp.crt",
    "xmlsec_binary": xmlsec_path
}