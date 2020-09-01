from Utils.RestApiOperations import RestUtilsForSnow


class GlideRecordForTable:
    __rest_snow = RestUtilsForSnow()

    def __init__(self, table_name):
        self.__api_url = "{}?sysparm_display_value=all".format(table_name)
        self.__add_query = None
        self.__add_encoded_query = None
        self.__init_count = -1
        self.__response = None

    def add_encoded_query(self, encoded_query):
        self.__add_encoded_query = "&sysparm_query=" + encoded_query if self.__add_encoded_query is None else self.__add_encoded_query + "^" + encoded_query

    def add_not_null_query(self, field_key):
        self.add_encoded_query("{}!=null".format(field_key))

    def add_null_query(self, field_key):
        self.add_encoded_query("{}=null".format(field_key))

    def add_query(self, field_key, field_display_value):
        query_string = "{}={}".format(field_key, field_display_value)
        self.__add_query = "&" + query_string if self.__add_query is None else self.__add_query + "&" + query_string

    def order_by(self, field_key):
        self.add_encoded_query("ORDERBY{}".format(field_key))

    def order_by_desc(self, field_key):
        self.add_encoded_query("ORDERBYDESC{}".format(field_key))

    def set_limit(self, limit_count):
        self.__api_url = self.__api_url + "&sysparm_limit={}".format(limit_count)

    def query(self):
        if self.__add_encoded_query is not None:
            self.__api_url = self.__api_url + self.__add_encoded_query
        if self.__add_query is not None:
            self.__api_url = self.__api_url + self.__add_query
        self.__response = self.__rest_snow.glide_record_get_request(self.__api_url)

    def next(self):
        self.__init_count = self.__init_count + 1

    def get_value(self, field_key):
        return self.__rest_snow.get_field_value(self.__response, field_key, self.__init_count)

    def get_display_value(self, field_key):
        return self.__rest_snow.get_field_display_value(self.__response, field_key, self.__init_count)

    def get_list_of_value(self, field_key):
        return self.__rest_snow.get_list_of_value(self.__response, field_key)

    def get_list_of_display_value(self, field_key):
        return self.__rest_snow.get_list_of_display_value(self.__response, field_key)


class GlideRecordUtils:
    pass
