from urllib.parse import urlencode, urljoin


class Helper:
    @staticmethod
    def build_query_string(base_url, query_params, array_key=None, array_values=None):
        query_string = f"{base_url}?{urlencode(query_params)}"
        if array_key and array_values:
            for value in array_values:
                query_string += f"&{array_key}={value}"
        return query_string




