class AccountInformationResponse:
    def __init__(self, credit, expire_date, plan):
        self.credit = credit
        self.expire_date = expire_date
        self.plan = plan

    def __repr__(self):
        return f"AccountInformationResponse(credit={self.credit}, expire_date={self.expire_date}, plan={self.plan})"


class CheckOtpTemplateResponse:
    def __init__(self, params, message):
        self.params = params
        self.message = message

    def __repr__(self):
        return f"CheckOtpTemplateResponse(params={self.params}, message={self.message})"


class CheckSmsStatusInput:
    def __init__(self, ids, type0):
        self.ids = ids
        self.type = type0

    def __repr__(self):
        return f"CheckSmsStatusInput(ids={self.ids}, type={self.type})"

    def to_dict(self):
        return {
            "Ids": self.ids,
            "Type": str(self.type)
        }


class GetOtpParametersInput:
    def __init__(self, template_name):
        self.template_name = template_name

    def __repr__(self):
        return f"GetOtpParametersInput(template_name={self.template_name})"

    def to_dict(self):
        return {
            "TemplateName": self.template_name
        }


class GetReceivedSmsInput:
    def __init__(self, line_number, is_read=False):
        self.line_number = line_number
        self.is_read = is_read

    def __repr__(self):
        return f"GetReceivedSmsInput(line_number={self.line_number}, is_read={self.is_read})"

    def to_dict(self):
        return {
            "LineNumber": self.line_number,
            "IsRead": self.is_read
        }


class GetReceivedSmsPagingInput:
    def __init__(self, line_number, is_read=False, start_date=None, end_date=None, page_index=0, page_size=10):
        self.line_number = line_number
        self.is_read = is_read
        self.start_date = start_date
        self.end_date = end_date
        self.page_index = page_index
        self.page_size = page_size

    def __repr__(self):
        return (f"GetReceivedSmsPagingInput(line_number={self.line_number}, is_read={self.is_read}, "
                f"start_date={self.start_date}, end_date={self.end_date}, page_index={self.page_index}, page_size={self.page_size})")

    def to_dict(self):
        return {
            "LineNumber": self.line_number,
            "IsRead": self.is_read,
            "StartDate": self.start_date.isoformat() if self.start_date else None,
            "EndDate": self.end_date.isoformat() if self.end_date else None,
            "PageIndex": self.page_index,
            "PageSize": self.page_size
        }


class ReceivedSmsesPagingResponse:
    def __init__(self, index_from, page_index, page_size, total_count, total_pages, has_previous_page, has_next_page,
                 items):
        self.index_from = index_from
        self.page_index = page_index
        self.page_size = page_size
        self.total_count = total_count
        self.total_pages = total_pages
        self.has_previous_page = has_previous_page
        self.has_next_page = has_next_page
        self.items = items

    def __repr__(self):
        return (
            f"ReceivedSmsesPagingResponse(index_from={self.index_from}, page_index={self.page_index}, page_size={self.page_size}, "
            f"total_count={self.total_count}, total_pages={self.total_pages}, has_previous_page={self.has_previous_page}, "
            f"has_next_page={self.has_next_page}, items={self.items})")

    class ReceivedSms:
        def __init__(self, id, message, sender, line_number, receive_date):
            self.id = id
            self.message = message
            self.sender = sender
            self.line_number = line_number
            self.receive_date = receive_date

        def __repr__(self):
            return (f"ReceivedSms(id={self.id}, message={self.message}, sender={self.sender}, "
                    f"line_number={self.line_number}, receive_date={self.receive_date})")


class ReceivedSmsesResponse:
    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return f"ReceivedSmsesResponse(items={self.items})"

    class ReceivedSms:
        def __init__(self, id, message, sender, line_number, receive_date):
            self.id = id
            self.message = message
            self.sender = sender
            self.line_number = line_number
            self.receive_date = receive_date

        def __repr__(self):
            return (f"ReceivedSms(id={self.id}, message={self.message}, sender={self.sender}, "
                    f"line_number={self.line_number}, receive_date={self.receive_date})")


class ResponseDto:
    def __init__(self, is_success=False, status_code=None, message=None):
        self.is_success = is_success
        self.status_code = status_code
        self.message = message

    def __repr__(self):
        return f"ResponseDto(is_success={self.is_success}, status_code={self.status_code}, message={self.message})"


class ResponseDtoWithData(ResponseDto):
    def __init__(self, data, is_success=False, status_code=None, message=None):
        super().__init__(is_success, status_code, message)
        self.data = data

    def __repr__(self):
        return f"ResponseDtoWithData(data={self.data}, is_success={self.is_success}, status_code={self.status_code}, message={self.message})"


class SendBulkInput:
    def __init__(self, send_date=None, line_number=None, receptors=None, message=None, client_reference_id=None,
                 is_voice=False, udh=False):
        self.send_date = send_date
        self.line_number = line_number
        self.receptors = receptors
        self.message = message
        self.client_reference_id = client_reference_id
        self.is_voice = is_voice
        self.udh = udh

    def __repr__(self):
        return (
            f"SendBulkInput(send_date={self.send_date}, line_number={self.line_number}, receptors={self.receptors}, "
            f"message={self.message}, client_reference_id={self.client_reference_id}, is_voice={self.is_voice}, udh={self.udh})")

    def to_dict(self):
        return {
            "SendDate": self.send_date.isoformat() if self.send_date else None,
            "LineNumber": self.line_number,
            "Receptors": self.receptors,
            "Message": self.message,
            "ClientReferenceId": self.client_reference_id,
            "IsVoice": self.is_voice,
            "Udh": self.udh
        }


class SendBulkResponse:
    def __init__(self, cost, line_number, receptors, message, status, send_date, status_description):
        self.cost = cost
        self.line_number = line_number
        self.receptors = receptors
        self.message = message
        self.status = status
        self.send_date = send_date
        self.status_description = status_description

    def __repr__(self):
        return (f"SendBulkResponse(cost={self.cost}, line_number={self.line_number}, receptors={self.receptors}, "
                f"message={self.message}, status={self.status}, send_date={self.send_date}, status_description={self.status_description})")

    class ReceptionInfo:
        def __init__(self, receptor, message_id):
            self.receptor = receptor
            self.message_id = message_id

        def __repr__(self):
            return f"ReceptionInfo(receptor={self.receptor}, message_id={self.message_id})"


class SendOldOtpInput:
    def __init__(self, send_date=None, receptors=None, template_name=None, param1=None, param2=None, param3=None,
                 param4=None, param5=None, param6=None, param7=None, param8=None, param9=None, param10=None,
                 is_voice=False, udh=False):
        self.send_date = send_date
        self.receptors = receptors if receptors else []
        self.template_name = template_name
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5
        self.param6 = param6
        self.param7 = param7
        self.param8 = param8
        self.param9 = param9
        self.param10 = param10
        self.is_voice = is_voice
        self.udh = udh

    def __repr__(self):
        return (
            f"SendOldOtpInput(send_date={self.send_date}, receptors={self.receptors}, template_name={self.template_name}, "
            f"param1={self.param1}, param2={self.param2}, param3={self.param3}, param4={self.param4}, param5={self.param5}, "
            f"param6={self.param6}, param7={self.param7}, param8={self.param8}, param9={self.param9}, param10={self.param10}, "
            f"is_voice={self.is_voice}, udh={self.udh})")

    def to_dict(self):
        return {
            "SendDate": self.send_date.isoformat() if self.send_date else None,
            "Receptors": [receptor.to_dict() for receptor in self.receptors],
            "TemplateName": self.template_name,
            "Param1": self.param1,
            "Param2": self.param2,
            "Param3": self.param3,
            "Param4": self.param4,
            "Param5": self.param5,
            "Param6": self.param6,
            "Param7": self.param7,
            "Param8": self.param8,
            "Param9": self.param9,
            "Param10": self.param10,
            "IsVoice": self.is_voice,
            "Udh": self.udh
        }


class SendOtpReceptorDto:
    def __init__(self, mobile, client_reference_id=None):
        self.mobile = mobile
        self.client_reference_id = client_reference_id

    def __repr__(self):
        return f"SendOtpReceptorDto(mobile={self.mobile}, client_reference_id={self.client_reference_id})"

    def to_dict(self):
        return {
            "Mobile": self.mobile,
            "ClientReferenceId": self.client_reference_id
        }

    def to_dict(self):
        return {
            "Mobile": self.mobile,
            "ClientReferenceId": self.client_reference_id
        }


class SendOtpInput:
    def __init__(self, send_date=None, receptors=None, template_name=None, inputs=None, udh=False):
        self.send_date = send_date
        self.receptors = receptors
        self.template_name = template_name
        self.inputs = inputs if inputs else []
        self.udh = udh

    def __repr__(self):
        return (
            f"SendOtpInput(send_date={self.send_date}, receptors={self.receptors}, template_name={self.template_name}, "
            f"inputs={self.inputs}, udh={self.udh})")

    def to_dict(self):
        return {
            "SendDate": self.send_date.isoformat() if self.send_date else None,
            "Receptors": [receptor.to_dict() for receptor in self.receptors],
            "TemplateName": self.template_name,
            "Inputs": [input.to_dict() for input in self.inputs],
            "Udh": self.udh
        }

    class OtpInput:
        def __init__(self, param, value):
            self.param = param
            self.value = value

        def __repr__(self):
            return f"OtpInput(param={self.param}, value={self.value})"

        def to_dict(self):
            return {
                "Param": self.param,
                "Value": self.value
            }


class SendOtpResponse:
    def __init__(self, line_number, message_body, items, cost):
        self.line_number = line_number
        self.message_body = message_body
        self.items = items
        self.cost = cost

    def __repr__(self):
        return (
            f"SendOtpResponse(line_number={self.line_number}, message_body={self.message_body}, items={self.items}, cost={self.cost})")

    class Data:
        def __init__(self, receptor, cost, message_id, send_date, status, status_description):
            self.receptor = receptor
            self.cost = cost
            self.message_id = message_id
            self.send_date = send_date
            self.status = status
            self.status_description = status_description

        def __repr__(self):
            return (
                f"Data(receptor={self.receptor}, cost={self.cost}, message_id={self.message_id}, send_date={self.send_date}, "
                f"status={self.status}, status_description={self.status_description})")


class SendPairToPairInput:
    def __init__(self, items, udh=False):
        self.items = items
        self.udh = udh

    def __repr__(self):
        return f"SendPairToPairInput(items={self.items}, udh={self.udh})"

    def to_dict(self):
        return {
            "Items": [item.to_dict() for item in self.items],
            "Udh": self.udh
        }

    class SendPairToPairSmsWebServiceDto:
        def __init__(self, line_number, receptor, message, client_reference_id=None, send_date=None):
            self.line_number = line_number
            self.receptor = receptor
            self.message = message
            self.client_reference_id = client_reference_id
            self.send_date = send_date

        def __repr__(self):
            return (
                f"SendPairToPairSmsWebServiceDto(line_number={self.line_number}, receptor={self.receptor}, message={self.message}, "
                f"client_reference_id={self.client_reference_id}, send_date={self.send_date})")

        def to_dict(self):
            return {
                "LineNumber": self.line_number,
                "Receptor": self.receptor,
                "Message": self.message,
                "ClientReferenceId": self.client_reference_id,
                "SendDate": self.send_date.isoformat() if self.send_date else None
            }


class SendPairToPairResponse:
    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return f"SendPairToPairResponse(items={self.items})"

    class PairData:
        def __init__(self, line_number, receptor, message_id, cost, send_date, message, status, status_description):
            self.line_number = line_number
            self.receptor = receptor
            self.message_id = message_id
            self.cost = cost
            self.send_date = send_date
            self.message = message
            self.status = status
            self.status_description = status_description

        def __repr__(self):
            return (
                f"PairData(line_number={self.line_number}, receptor={self.receptor}, message_id={self.message_id}, cost={self.cost}, "
                f"send_date={self.send_date}, message={self.message}, status={self.status}, status_description={self.status_description})")


class SendSingleResponse:
    def __init__(self, receptor, line_number, cost, message_id, message, status, send_date, status_description):
        self.receptor = receptor
        self.line_number = line_number
        self.cost = cost
        self.message_id = message_id
        self.message = message
        self.status = status
        self.send_date = send_date
        self.status_description = status_description

    def __repr__(self):
        return (
            f"SendSingleResponse(receptor={self.receptor}, line_number={self.line_number}, cost={self.cost}, message_id={self.message_id}, "
            f"message={self.message}, status={self.status}, send_date={self.send_date}, status_description={self.status_description})")


class SendSingleSmsInput:
    def __init__(self, send_date=None, line_number=None, receptor=None, message=None, client_reference_id=None,
                 udh=False):
        self.send_date = send_date
        self.line_number = line_number
        self.receptor = receptor
        self.message = message
        self.client_reference_id = client_reference_id
        self.udh = udh

    def __repr__(self):
        return (
            f"SendSingleSmsInput(send_date={self.send_date}, line_number={self.line_number}, receptor={self.receptor}, "
            f"message={self.message}, client_reference_id={self.client_reference_id}, udh={self.udh})")

    def to_dict(self):
        return {
            # "SendDate": self.send_date.isoformat() if self.send_date else None,
            "LineNumber": self.line_number,
            "Receptor": self.receptor,
            "Message": self.message,
            # "ClientReferenceId": self.client_reference_id,
            "Udh": self.udh
        }


class SmsStatusResponseItems:
    def __init__(self, message_id, client_reference_id, message, line_number, receptor, status, price, send_date):
        self.message_id = message_id
        self.client_reference_id = client_reference_id
        self.message = message
        self.line_number = line_number
        self.receptor = receptor
        self.status = status
        self.price = price
        self.send_date = send_date

    def __repr__(self):
        return (
            f"SmsStatusResponseItems(message_id={self.message_id}, client_reference_id={self.client_reference_id}, message={self.message}, "
            f"line_number={self.line_number}, receptor={self.receptor}, status={self.status}, price={self.price}, send_date={self.send_date})")
