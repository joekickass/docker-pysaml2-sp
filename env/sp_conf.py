from saml2 import BINDING_HTTP_REDIRECT
from saml2 import BINDING_HTTP_POST
from saml2.extension.idpdisc import BINDING_DISCO
from saml2.saml import NAME_FORMAT_URI

xmlsec_path = '/usr/bin/xmlsec1'

# Make sure the same port number appear in service_conf.py
BASE = "http://localhost:8088"

CONFIG = {
    "entityid": "%s/%ssp.xml" % (BASE, ""),
    "service": {
        "sp": {
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/acs/post" % BASE, BINDING_HTTP_POST)
                ],
                "discovery_response": [
                    ("%s/disco" % BASE, BINDING_DISCO)
                ]
            }
        },
    },
    "xmlsec_binary": xmlsec_path,
    "metadata": {
        "local": ["idp.xml"],
    },
    "name_form": NAME_FORMAT_URI,
}
