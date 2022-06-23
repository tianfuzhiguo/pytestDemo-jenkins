from core.result_base import ResultBase
from api.employee import emp
from common.logger import logger


def queryEmp(empname,token):
    """
    查询角色
    :param rolename: 角色名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "search": empname,
        "page": 1,
        "pageNum":10
    }
    header={"token":token}
    res = emp.queryEmp(params=payload,headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()["message"]
    result.response = res
    logger.info("查询角色 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
