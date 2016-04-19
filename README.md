# Docker image for pysaml2 SP

SAML 2.0 SP Docker image using [pysaml2](https://github.com/rohe/pysaml2).

## Run

Run the Service Provider (SP):

    make

It should be reachable at [https://localhost:8088](https://localhost:8088).

## Configure

Configuration files are found in:
- [service_conf.py](conf/service_conf.py) - web service configuration
- [sp_conf.py](conf/sp_conf.py) - pysaml2 configuration
- [idp.xml](conf/idp.xml) - IdP metadata

TLS/SSL and assertion signing is enabled by default (using the same cert).

See example configurations [here](https://github.com/rohe/pysaml2/tree/master/example/sp-wsgi).

## Keys

Sample keys are found in:
- [sp.crt](pki/sp.crt) - Public, self-signed cert in PEM format.
- [sp.key](pki/sp.key) - Private RSA key for the cert.

Keys are generated with the following commands:

    # Generate cert
    openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout sp.key -out sp.crt
    chmod 600 sp.key

    # Check key
    openssl rsa -in sp.key -check

    # Check cert
    openssl x509 -in sp.crt -text -noout

    # Convert key & cert to PKCS#12 (used by google chrome import)
    openssl pkcs12 -export -out sp.pfx -inkey sp.key -in sp.crt

    # check pfx
    openssl pkcs12 -info -in sp.pfx