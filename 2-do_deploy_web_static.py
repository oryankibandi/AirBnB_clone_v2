#!/usr/bin/python3
""" generates a .tgz archive from web_static repo"""


from fabric.api import *
from datetime import datetime
import os

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


def do_deploy(archive_path):
    """
    Distributes an archive to my web-servers
    """
    if not os.path.exists():
        return False

    try:
        tgz_file = archive_path.split('/')[-1]
        put("{}".format(archive_path), "/tmp/{}".format(tgz_file))
        tgz_name = tgz_file.split('.')[0]
        run("mkdir -p /data/web_static/releases/{}".format(tgz_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(tgz_file, tgz_name))
        run("rm /tmp/{}".format(tgz_file))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/current /data/web_static/releases/{}".format(tgz_name))
        return True
    except:
        return False
