# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-28 23:25:43
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-06-28 23:38:59

# import importlib
# foo = importlib.machinery.SourceFileLoader("module.name", "").load_module()
# w = __import__("")
# 
from website_status_cli import main as x

print x.website_up()
print x.website_code()