# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
# 
#################################################################################

from . import models
from . import wizards
from . import controllers

def pre_init_check(cr):
    from giga.service import common
    from giga.exceptions import Warning
    version_info = common.exp_version()
    server_serie = version_info.get('server_serie')
    if server_serie != '15.0':
        raise Warning(
            'Module support giga series 15.0 found {}.'.format(server_serie))
    return True