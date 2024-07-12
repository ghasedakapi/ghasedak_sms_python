import datetime

from ghasedak_sms.dto import *
from ghasedak_sms.enums.message_id_type import MessageIdType
from ghasedak_sms.ghasedak import Ghasedak

# Replace 'your_api_key' with your actual API key
api_key = 'your_api_key'
line = '123xxxxxxx'
recipient_phone_number1 = '09xxxxxxxxx'
recipient_phone_number2 = '09xxxxxxxxx'

ghasedak = Ghasedak(api_key)


def print_separator():
    print("_____________________________________")


def test_check_sms_status():
    print_separator()
    query = CheckSmsStatusInput(ids=['2366799', '2366805'], type0=MessageIdType.MESSAGE_ID)
    print("Input for Check SMS Status:", query.__dict__)
    response = ghasedak.check_sms_status(query)
    print("Output for Check SMS Status:", response)


def test_get_account_information():
    print_separator()
    print("Input for Get Account Information: None")
    response = ghasedak.get_account_information()
    print("Output for Get Account Information:", response)


def test_get_received_smses():
    print_separator()
    query = GetReceivedSmsInput(line_number=line, is_read=False)
    print("Input for Get Received SMSes:", query.__dict__)
    response = ghasedak.get_received_smses(query)
    print("Output for Get Received SMSes:", response)


def test_get_received_smses_paging():
    print_separator()
    query = GetReceivedSmsPagingInput(
        line_number=line,
        is_read=False,
        start_date=datetime.datetime.now() - datetime.timedelta(days=90),
        end_date=datetime.datetime.now(),
        page_index=0,
        page_size=10
    )
    print("Input for Get Received SMSes Paging:", query.__dict__)
    response = ghasedak.get_received_smses_paging(query)
    print("Output for Get Received SMSes Paging:", response)


def test_get_otp_parameters():
    print_separator()
    query = GetOtpParametersInput(template_name='newOTP')
    print("Input for Get OTP Parameters:", query.__dict__)
    response = ghasedak.get_otp_parameters(query)
    print("Output for Get OTP Parameters:", response)


def test_send_single_sms():
    print_separator()
    command = SendSingleSmsInput(
        send_date=None,
        line_number=line,
        receptor=recipient_phone_number1,
        message='Your message',
        client_reference_id='client_ref_id',
        udh=False
    )
    print("Input for Send Single SMS:", command.__dict__)
    response = ghasedak.send_single_sms(command)
    print("Output for Send Single SMS:", response)


def test_send_bulk_sms():
    print_separator()
    command = SendBulkInput(
        send_date=None,
        line_number=line,
        receptors=[recipient_phone_number1, recipient_phone_number2],
        message='Your bulk message',
        client_reference_id='client_ref_id',
        is_voice=False,
        udh=False
    )
    print("Input for Send Bulk SMS:", command.__dict__)
    response = ghasedak.send_bulk_sms(command)
    print("Output for Send Bulk SMS:", response)


def test_send_pair_to_pair_sms():
    print_separator()
    command = SendPairToPairInput(
        items=[
            # SendPairToPairInput.SendPairToPairSmsWebServiceDto(
            #     line_number=line,
            #     receptor=recipient_phone_number1,
            #     message='Message 1',
            #     # client_reference_id='client_ref_id',
            #     send_date=datetime.datetime.now()
            # ),
            SendPairToPairInput.SendPairToPairSmsWebServiceDto(
                line_number=line,
                receptor=recipient_phone_number2,
                message='Message 2',
                # client_reference_id='client_ref_id',
                send_date=datetime.datetime.now()
            )
        ],
        udh=False
    )
    print("Input for Send Pair to Pair SMS:", command.__dict__)
    response = ghasedak.send_pair_to_pair_sms(command)
    print("Output for Send Pair to Pair SMS:", response)


def test_send_otp_sms_old():
    print_separator()
    command = SendOldOtpInput(
        send_date=datetime.datetime.now(),
        receptors=[
            SendOtpReceptorDto(
                mobile=recipient_phone_number1,
                # client_reference_id='client_ref_id'
            )
        ],
        template_name='oldOTP',
        param1='param1_value',
        param2='param2_value',
        param3='param3_value',
        param4='param4_value',
        param5='param5_value',
        param6='param6_value',
        param7='param7_value',
        param8='param8_value',
        param9='param9_value',
        param10='param10_value',
        is_voice=False,
        udh=False
    )
    print("Input for Send OTP SMS Old:", command.__dict__)
    response = ghasedak.send_otp_sms_old(command)
    print("Output for Send OTP SMS Old:", response)


def test_send_otp_sms():
    print_separator()
    command = SendOtpInput(
        send_date=None,
        receptors=[
            SendOtpReceptorDto(
                mobile=recipient_phone_number1,
                # client_reference_id='client_ref_id'
            )
        ],
        template_name='newOTP',
        inputs=[
            SendOtpInput.OtpInput(param='Code', value='code'),
            SendOtpInput.OtpInput(param='Name', value='name')
        ],
        udh=False
    )
    print("Input for Send OTP SMS:", command.__dict__)
    response = ghasedak.send_otp_sms(command)
    print("Output for Send OTP SMS:", response)


if __name__ == "__main__":
    test_check_sms_status()
    test_get_account_information()
    test_get_received_smses()
    test_get_received_smses_paging()
    test_get_otp_parameters()
    test_send_single_sms()
    test_send_bulk_sms()
    test_send_pair_to_pair_sms()
    test_send_otp_sms_old()
    test_send_otp_sms()
