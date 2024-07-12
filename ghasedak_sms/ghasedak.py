import requests
from requests import RequestException

from ghasedak_sms.dto import ResponseDto
from ghasedak_sms.helper import Helper


class Ghasedak:
    def __init__(self, api_key):
        self.url = "https://gw.ghasedak.me/Rest/api/v1/WebService/"
        self.headers = {
            "Accept": "application/json",
            "cache-control": "no-cache",
            "ApiKey": api_key
        }

    def check_sms_status(self, query, cancellation_token=None):
        query_string = Helper.build_query_string(f"{self.url}CheckSmsStatus", {"Type": str(query.type)}, "Ids",
                                                 query.ids)
        try:
            response = requests.get(query_string, headers=self.headers)
            response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def get_account_information(self, cancellation_token=None):
        try:
            response = requests.get(f"{self.url}GetAccountInformation", headers=self.headers)
            response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def get_received_smses(self, query, cancellation_token=None):
        query_string = Helper.build_query_string(f"{self.url}GetReceivedSmses",
                                                 {"LineNumber": query.line_number, "IsRead": str(query.is_read)})
        try:
            response = requests.get(query_string, headers=self.headers)
            response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def get_received_smses_paging(self, query, cancellation_token=None):
        query_string = Helper.build_query_string(f"{self.url}GetReceivedSmsesPaging", {
            "LineNumber": query.line_number,
            "IsRead": str(query.is_read),
            "StartDate": str(query.start_date),
            "EndDate": str(query.end_date),
            "PageIndex": str(query.page_index),
            "PageSize": str(query.page_size)
        })
        try:
            response = requests.get(query_string, headers=self.headers)
            response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def get_otp_parameters(self, query, cancellation_token=None):
        query_string = Helper.build_query_string(f"{self.url}GetOtpTemplateParameters",
                                                 {"TemplateName": query.template_name})
        try:
            response = requests.get(query_string, headers=self.headers)
            response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def send_single_sms(self, command, cancellation_token=None):
        try:
            response = requests.post(f"{self.url}SendSingleSMS", headers=self.headers, json=command.to_dict())
            # response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def send_bulk_sms(self, command, cancellation_token=None):
        try:
            response = requests.post(f"{self.url}SendBulkSMS", headers=self.headers, json=command.to_dict())
            # response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def send_pair_to_pair_sms(self, command, cancellation_token=None):
        try:
            response = requests.post(f"{self.url}SendPairToPairSMS", headers=self.headers, json=command.to_dict())
            # response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def send_otp_sms_old(self, command, cancellation_token=None):
        try:
            response = requests.post(f"{self.url}SendOtpWithParams", headers=self.headers, json=command.to_dict())
            # response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()

    def send_otp_sms(self, command, cancellation_token=None):
        try:
            response = requests.post(f"{self.url}SendOtpSMS", headers=self.headers, json=command.to_dict())
            # response.raise_for_status()
        except RequestException as ex:
            return ResponseDto(is_success=False, message=str(ex), status_code=response.status_code if response else 500)

        return response.json()
