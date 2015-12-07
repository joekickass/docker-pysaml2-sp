#!/bin/sh

cd ${DATA_DIR:?"Need to set DATA_DIR non-empty"}
export PYTHONPATH="${DATA_DIR}"

# generate SAML metadata
make_metadata.py sp_conf.py > sp.xml

# start the Service Provider
exec /tmp/src/pysaml2/example/sp-wsgi/sp.py sp_conf
