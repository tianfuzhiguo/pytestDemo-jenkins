import pytest
import os
from common.read_data import data
from testcases.conftest import role_data
from common.mysql_operate import db
from common.logger import logger
#conftest中的装饰器在其所在目录中可以直接使用，无需导入

@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return role_data.get(testcase_name)

@pytest.fixture()
def deleteRole(rolename):
    """新增角色前，先删除数据，用例执行之后，再次删除以清理数据"""
    del_sql = role_data["init_sql"]["delete_role"]
    print(77777777777777777777777777)
    db.execute_db(del_sql)
    print(88888888888888888888888888)
    logger.info("执行前置SQL：{}".format(del_sql))
    yield
    #db.execute_db(del_sql)
    #logger.info("执行后置SQL：{}".format(del_sql))