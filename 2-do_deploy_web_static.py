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
        run('mkdir -p /data/web_static/releases/{}/'.format(name.split('.')[0]))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(name, name.split('.')[0]))
        run('rm /tmp/{}'.format(name))
        spl = name.split('.')[0]
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(spl, spl))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(spl))
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.format(name.split('.')[0]))
        return True
    except:
        return False
