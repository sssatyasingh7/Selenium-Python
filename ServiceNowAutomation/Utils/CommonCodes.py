import os
import time
import random
import json
from collections import Counter


class CommonUtils:
    @staticmethod
    def thread_sleep(milliSeconds):
        time.sleep(milliSeconds // 1000)

    @staticmethod
    def pause_me(seconds):
        time.sleep(seconds)

    @staticmethod
    def generate_random_number(digit_number):
        return random.randint(10 ** (digit_number - 1), 10 ** digit_number - 1)

    @staticmethod
    def generate_random_number_between_numbers(min_num, max_num):
        return random.randrange(min_num, max_num)

    @staticmethod
    def compare_equals(actual, expected):
        act = type(actual)
        exp = type(expected)
        if (act is list or act is set or act is tuple) or (exp is list or expected is set or exp is tuple):
            return actual.sort().equals(expected.sort())
        else:
            return actual.equals(expected)

    @staticmethod
    def compare_contains(actual, expected):
        return actual.contains(expected)

    @staticmethod
    def return_value(string_value):
        if string_value is not None:
            string_value = string_value.strip()
        return string_value if string_value is not None and len(string_value) is not 0 else None

    @staticmethod
    def read_file_as_string(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    @staticmethod
    def get_working_dir():
        return os.getcwd()

    @staticmethod
    def get_parent_dir_of_dir(dir_path):
        return os.path.dirname(dir_path)

    @staticmethod
    def get_current_project_dir():
        return CommonUtils.get_parent_dir_of_dir(CommonUtils.get_working_dir())

    @staticmethod
    def merge_dictionary(dict1, dict2):
        dict1.update(dict2)
        return dict1

    @staticmethod
    def josn_string_to_map(json_string):
        return json.loads(json_string)

    @staticmethod
    def replace_char_with_other_char(string_value, init_char, final_char):
        return string_value.replace(init_char, final_char)

    @staticmethod
    def get_list_of_words(string_value):
        return string_value.split()

    @staticmethod
    def contains_text_xpath(string_value):
        string_val = ""
        return string_val.join(
            list(map(lambda x: "[contains(.,'{}')]".format(x), CommonUtils.get_list_of_words(string_value))))

    @staticmethod
    def get_file_separator():
        return os.path.sep

    @staticmethod
    def get_number_of_repetation(string_value):
        return dict(Counter(string_value))
