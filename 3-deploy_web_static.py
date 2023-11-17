#!/usr/bin/python3
"""full deploy"""
import datetime
from fabric.api import local, run, env, put
from os.path import exists
env.hosts = ['54.88.43.0', '18.235.249.83']


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
        run('mkdir -p /data/web_static/releases/{}/'.format(name.split('.')[0]))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(name, name.split('.')[0]))
        run('rm /tmp/{}'.format(name))
        spl = name.split('.')[0]
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(spl, spl))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(spl))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(name.split('.')[0]))
        return True
    except:
        return False


def deploy():
    """full deployment"""
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
