#!/usr/bin/python3
""" generates a .tgz archive from web_static repo"""

from fabric.api import *
from datetime import datetime


env.hosts = ['3.235.30.193', '35.170.82.237']            
env.user = "ubuntu"
path_to_file = None

def do_pack():
    """
    Generates a .tgz file from web_static repo
    """
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file = "versions/web_static_{}".format(now)
    try:
        run("mkdir -p /versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file))
        path_to_file = file
        return file
    except:
        return None

def do_name():
    run("docker ps")
