#!/usr/bin/python3
"""
create file archive
"""
import datetime
from fabric.api import local

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
