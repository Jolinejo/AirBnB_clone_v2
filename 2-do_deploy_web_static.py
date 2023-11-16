#!/usr/bin/python3
"""
deploy archive
"""
import datetime
from fabric.api import local, run, env, put
from os.path import exists
env.hosts = ['54.236.47.113', '100.25.170.6']


def do_deploy(archive_path):
    """deploy the archive"""
    if exists(archive_path) is False:
        return False
    try:
        name = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(name))
        spl = name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(name.spl))
        dist = "/data/web_static/releases/"
        run('tar -xzf /tmp/{} -C {}{}/'.format(name, dist, spl))
        run('rm /tmp/{}'.format(name))
        run('mv {}{}/web_static/* {}{}/'.format(dist, spl, dist, spl))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(spl))
        run('rm -rf /data/web_static/current')
        run('ln -sf {}{}/ /data/web_static/current'.format(dist, spl))
        return True
    except Exception:
        return False
