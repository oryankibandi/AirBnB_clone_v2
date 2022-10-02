#!/usr/bin/python3
""" generates a .tgz archive from web_static repo"""

from fabric.api import *
from datetime import datetime
from fabric.operations import run, put, sudo, local
import os

env.hosts = ['3.235.30.193', '35.170.82.237']
env.user = "ubuntu"
path_to_file = None

def do_pack():
    """
    Generates a .tgz file from web_static repo
    """
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file = "versions/web_static_{}.tgz".format(now)
    tgz_name = file.split('/')[-1]
    try:
        local("mkdir -p ./versions")
        local("tar -cvzf {} ./web_static"
              .format(tgz_name))
        local("mv {} versions".format(tgz_name))
        path_to_file = file
        return file
    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to my web-servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        tgz_file = archive_path.split('/')[-1]
        put("{}".format(archive_path), "/tmp/{}".format(tgz_file))
        tgz_name = tgz_file.split('.')[0]
        sudo("mkdir -p /data/web_static/releases/{}".format(tgz_name))
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(tgz_file, tgz_name))
        sudo("rm /tmp/{}".format(tgz_file))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/current /data/web_static/releases/{}".format(tgz_name))
        return True
    except:
        return False

def deploy():
    """
    Creates and distributes an archive to the web servers,
    using the function deploy
    """
    global path_to_file
    try:
        if path_to_file is None:
            path_to_file = do_pack()
        if path_to_file is None:
            return False
        success = do_deploy(path_to_file)
        return success
    except:
        return False

def do_clean(number=0):
    """
    deletes unnecessary files in versions/ and
    /data/web_static/releases on the server
    """
    num = int(number)
    if num == 0:
        num = 1
    files = local("ls -lt ./versions", capture=True)
    server_files = run("ls -lt /data/web_static/releases")
    new_files = files.split("\n")
    new_server_files = server_files.split("\n")

    for item in new_files[num:]:
        local("rm versions/{}".format(item.split(" ")[-1]))

    for item in new_server_files[num:]:
        if item.split(" ")[-1] == 'test':
            continue
        else:
            # print("deleting...{}".format(item.split(" ")[-1]))
            sudo("rm -rf /data/web_static/releases/{}".format(item.split(" ")[-1]))
