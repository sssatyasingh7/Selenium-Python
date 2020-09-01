from Utils.CommonCodes import CommonUtils
import sys


class Configuration:
    __keys = {}

    def __init__(self):
        if len(self.__keys.keys()) ==  0:
            try:
                with open(
                        CommonUtils.get_current_project_dir() + CommonUtils.get_file_separator() + "config.properties") as config_prop:
                    for line in config_prop:
                        if "=" in line:
                            name, value = line.split("=")
                            self.__keys[name.strip()] = value.strip()
            except:
                sys.exit("Configuration File Not Found, please add")

    def get_properties(self, prop_key):
        try:
            return self.__keys.get(prop_key)
        except:
            print("Property Key {} not found in 'configure.properties file".format(prop_key))
            return None

    def get_user_name(self):
        return self.get_properties("USER_NAME")

    def get_password(self):
        return self.get_properties("PASSWORD")

    def get_base_url(self):
        base_url = self.get_properties("BASE_URL")
        if base_url is not None and base_url.endswith("/"):
            base_url = base_url[:len(base_url) - 1]
        return base_url

    def get_browser_name(self):
        browser_name = self.get_properties("BROWSER_NAME")
        if browser_name is None:
            browser_name = "chrome"
        return browser_name

class DriverInitializer:
    pass
