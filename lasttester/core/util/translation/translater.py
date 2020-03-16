#coding:utf-8

import gettext
import os
import locale
from lastrunner.config import config_dir

language, encoding = locale.getdefaultlocale()

appName = 'fisherman'
localedir = os.path.join(config_dir, 'locale')
trans = gettext.translation(appName,localedir,[language])
_ = trans.gettext
