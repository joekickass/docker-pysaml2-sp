# Docker image for pysaml2 SP

To run the Service Provider (SP) run:

    docker run -p 8088:<port in service_conf.py> -v <host dir>:<data_dir> -e DATA_DIR=<data_dir> pysaml2-sp

The volume bound must contain the necessary configuration files:

    <host dir>/
    ├── idp.xml
    ├── service_conf.py
    └── sp_conf.py

where `idp.xml` is the Identity Providers (IdPs) metadata and `service_conf.py` and `sp_conf.py` are the the configuration files
for the pysaml2 SP, see the [example configurations](https://github.com/rohe/pysaml2/tree/f8cea469d70255adae71e81c19b71efc928d1445/example/sp-wsgi) in the pysaml2 project.

**Metadata for the SP will be written to the mounted host directory as specified by the environment variable: `DATA_DIR`.**

## Even simpler

Only add the IdPs metadata in [env/idp.xml](env/idp.xml), then:

    cd vagrant && vagrant up

The SP should be reachable at [http://localhost:8088](http://localhost:8088).
