FROM ubuntu:14.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    python-dev \
    python-pip \
    libsasl2-dev \
    libssl-dev \
    libffi-dev \
    xmlsec1

# Install pysaml2 and dependencies
RUN pip install git+https://github.com/rohe/pysaml2#egg=pysaml2
RUN pip install cherrypy

# Pull down SP example
RUN git clone https://github.com/rohe/pysaml2 /root/pysaml2
ENV SP_ROOT=/root/pysaml2/example/sp-wsgi
WORKDIR $SP_ROOT

# Copy configuration to workdir
ADD conf/sp_conf.py $SP_ROOT/
ADD conf/service_conf.py $SP_ROOT/
ADD conf/idp.xml $SP_ROOT/
ADD pki/sp.key $SP_ROOT/sp.key
ADD pki/sp.crt $SP_ROOT/sp.crt
RUN make_metadata.py $SP_ROOT/sp_conf.py > $SP_ROOT/sp.xml
ADD sp.py $SP_ROOT/sp.py

CMD ["./sp.py", "sp_conf"]