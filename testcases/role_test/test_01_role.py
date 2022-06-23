import pytest
import allure
from operation.role import queryRole
from operation.role import addRole
from testcases.conftest import role_data
from common.logger import logger


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("角色管理模块")
class TestRole():
    queryRoleNum=1
    addRoleNum=1
    @allure.story("用例--角色查询")
    @allure.description("该用例是针对获取角色查询接口的测试")
    @allure.title("测试数据：【 {rolename}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("rolename,except_result,except_code,except_msg",role_data["test_queryRole"])
    def test_queryRole(self, rolename, except_result,except_code, except_msg,login_fixture):
        logger.info("*************** 开始执行用例{} ***************".format("test_queryRole,查询角色第"+str(self.queryRoleNum)+"组数据"))
        self.queryRoleNum+=1
        token=login_fixture
        result = queryRole(rolename,token)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--新增角色")
    @allure.description("该用例是针对获取新增角色接口的测试")
    @allure.title("测试数据：【 {rolename}，{desc}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("rolename,desc,except_result,except_code,except_msg", role_data["test_addRole"])
    def test_addRole(self, rolename, desc,except_result,except_code, except_msg,login_fixture,deleteRole):
        logger.info("*************** 开始执行用例{} ***************".format("test_addRole新增角色第"+str(self.addRoleNum)+"组数据"))
        self.addRoleNum += 1
        token=login_fixture
        deleteRole
        result = addRole(rolename,desc,token)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_role.py"])
