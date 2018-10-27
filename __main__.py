# @Author: suveshagnihotri
# @Date:   2018-10-28T02:59:34+05:30
# @Last modified by:   suveshagnihotri
# @Last modified time: 2018-10-28T03:21:15+05:30

from employee import PROVIDER
from employee.main_factory import MainFactory


def main():
    facade = MainFactory.create_facade(PROVIDER)
    return facade.get_employees()


if __name__ == '__main__':
    result = main()
    print(result)
