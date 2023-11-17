#!/usr/bin/python3
"""
deploy archive
"""
import datetime
from fabric.api import local, run, env, put
from os.path import exists
env.hosts = ['54.88.43.0', '18.235.249.83']


def do_deploy(archive_path):
    """deploy the archive"""
    if exists(archive_path) is False:
        return False
    try:
        name = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(name))
        spl = name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(spl))
        dis = '/data/web_static/releases/{}/'.format(spl)
        c = 'tar -xzf'
        run('{} /tmp/{} -C /data/web_static/releases/{}/'.format(c, name, spl))
        run('rm /tmp/{}'.format(name))
        run('mv /data/web_static/releases/{}/web_static/* {}'.format(spl, dis))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(spl))
        run('rm -rf /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(dis))
        return True
    except Exception:
        return False
