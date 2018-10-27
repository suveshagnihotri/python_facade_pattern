# @Author: suveshagnihotri
# @Date:   2018-10-28T02:23:50+05:30
# @Last modified by:   suveshagnihotri
# @Last modified time: 2018-10-28T03:15:38+05:30

from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_employee import AbsEmployee


class MainFactory(object):
    @staticmethod
    def create_facade(module_name):
        module = import_module('.' + module_name, __package__)
        classes = getmembers(module,
                             lambda m:(
                                 isclass(m)
                                 and not isabstract(m)
                                 and issubclass(m, AbsEmployee))
        )
        print(classes)
        return classes[0][1]()
