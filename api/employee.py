import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Employee(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Employee, self).__init__(api_root_url, **kwargs)

    def queryEmp(self,**kwargs):
        return self.get("role/v1.0/role/selectEmployeeByRoleId",**kwargs)


emp = Employee(api_root_url)