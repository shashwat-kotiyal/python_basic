from collections import namedtuple
from dataclasses import dataclass
# Nodes
    # AP, Edge, CSO-Server, CSO-App ( UI, backend rest calls), Moxn, Attenuator, OTA Machine, Amarisoft

# functionality
    # running a remote command
        # ssh_utiltiy
        # kubectl command ( complexity)
    # calling an API
        # api_call

# logging
# is should fill the execution data in a database
# exceptions
# config cretation automation ( config data classes)

# frlib
    # ap.py
    # cso.py
    # csoapi.py ( submodule api call)
    # csoweb.py
    # utils
        # ssh_utility
        # constants AP-models, device-ids
        # kube_utility ( command builder)
    # config
        # data_classes ( setup definitions as a dataclass)
        #@dataclass
        #class AP:
        #    SSH_IP: str
        #    SSH_USERNAME: str
        #AP_CONFIG = AP(SSH_IP="123.32.12.11", SSH_USERNAME="root")
        # exceptions
    # general_utils
        # helper_functions ( read a tcpdump )
    # __init__.py

#ride
# bin
    # scripts emailing, reports listeners
    # not allow in develop force user to make a branch switch ( shell script), package check, requirement text-> main.py

# data
    # resources

# logs
    # per execution with tampstamps

# Test-Suite
    # robo files .robo keywords are being called

# cn_library
    # custom robo libraries ( python implemented using lib ) .py implementation

# Mysql db for execution result storage ( time, build number, pass, fail, reason, setup name)
# groupby, charting, graphing
# execution( jenkins server)-> call script on mysql server( gcp host)-> that script will populate on rwo for this execution in table ( mysql server)----
# ---> grafana will consume this data (gcp host) ( queries for data)

# they want to know the latest passed build
#

from frlib import CSO, Edge
from frlib.cso import privateCSO
c = CSO()


# performance and scaling
# Lazy Loading
    # when we are working with thousands APs ( loading the complete logs)
    # file iteration ( file.read())
    # long running ( while loop which iterate if data available on socket)

