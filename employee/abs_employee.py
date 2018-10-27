# @Author: suveshagnihotri
# @Date:   2018-10-28T02:16:03+05:30
# @Last modified by:   suveshagnihotri
# @Last modified time: 2018-10-28T03:13:11+05:30
import abc


class AbsEmployee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_employees(self):
        pass
