#!/usr/bin/python3
"""full deploy"""
import datetime
from fabric.api import local, run, env, put
from os.path import exists
env.hosts = ['54.236.47.113', '100.25.170.6']


def do_pack():
    """
    web_static_<year><month><day><hour><minute><second>.tgz
    """
    try:
        now = datetime.datetime.now()
        now = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        name = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(name))
        return name
    except Exception:
        return None


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


def deploy():
    """full deployment"""
    file_path = do_pack()
    if file_path is None:
        return False
    return(do_deploy(file_path))
