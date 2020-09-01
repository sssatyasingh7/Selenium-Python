import requests as request
from Utils.CommonCodes import CommonUtils
from Utils.ConfigurationFile import Configuration


class RestUtils:
    __json_response = None

    @classmethod
    def get_request(cls, url_value, user_name, password):
        response = request.get(url_value, auth=(user_name, password))
        response.status_code = request.codes.ok
        cls.__json_response = response.json()
        return cls.__json_response

    @classmethod
    def get_field_value_from_response(cls, field_key, field_return_key, count=0, response=__json_response):
        try:
            return CommonUtils.return_value(str(response['result'][count].get(field_key).get(field_return_key)))
        except:
            print("Field Attribute is not available in Response Json File to parse")
            return None

    @classmethod
    def get_list_of_field_value_from_response(cls, field_key, field_return_key, response=__json_response):
        try:
            return list(filter(
                lambda x: CommonUtils.return_value(lambda x: str(x.get(field_key).get(field_return_key))) is not None,
                response['result']))
        except:
            print("Field Attribute is not available in Response Json File to parse")
            return []


class RestUtilsForSnow():
    __api_url = "/api/now/table/"
    __response_display_all_query = "?sysparm_display_value=true"
    __config = Configuration()
    __rest_utils = RestUtils()

    def glide_record_get_request(self, api_url):
        return self.__rest_utils.get_request(
            self.__config.get_base_url() + self.__api_url + api_url, self.__config.get_user_name(), self.__config.get_password())

    def get_field_value(self, response, field_key, count=0):
        return self.__rest_utils.get_field_value_from_response(field_key, 'value', count, response)

    def get_field_display_value(self, response, field_key, count=0):
        return self.__rest_utils.get_field_value_from_response(field_key, 'display_value', count, response)

    def get_list_of_value(self, response, field_key):
        return self.__rest_utils.get_list_of_field_value_from_response(field_key, 'value', response)

    def get_list_of_display_value(self, response, field_key):
        return self.__rest_utils.get_list_of_field_value_from_response(field_key, 'display_value', response)
