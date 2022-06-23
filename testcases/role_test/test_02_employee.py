import pytest
import allure
from operation.employee import queryEmp
from testcases.conftest import employee_data
from common.logger import logger


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("角色人员模块")
class TestQueryEmp():
    @allure.story("用例--员工查询")
    @allure.description("该用例是针对获取员工查询接口的测试")
    @allure.title("测试数据：【 {empname}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("empname,except_result,except_code,except_msg", employee_data["test_queryEmp"])
    def test_queryEmp(self, empname, except_result, except_code, except_msg, login_fixture):
        logger.info("*************** 开始执行用例 ***************")
        token = login_fixture
        result = queryEmp(empname, token)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_role.py"])
