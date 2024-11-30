
# GhasedakSMS-python

A Python package for interacting with the GhasedakSMS web service API.

## Installation

You can simply install this package with `pip`:

```shell
pip install ghasedak_sms
```

## Usage

```python
import ghasedak_sms

# Create an instance:
sms_api = ghasedak_sms.Ghasedak(api_key="Your APIKEY")

# Check SMS status:

response = sms_api.check_sms_status(ghasedak_sms.CheckSmsStatusInput(ids=['messageId1', 'messageId2'], type0='1'))
print(response)

# Get account information:
response = sms_api.get_account_information()
print(response)

# Get received SMSes:
response = sms_api.get_received_smses(ghasedak_sms.GetReceivedSmsInput(line_number='xxxx', is_read=False))
print(response)

# Get received SMSes with pagination:
response = sms_api.get_received_smses_paging(ghasedak_sms.GetReceivedSmsPagingInput(line_number='xxxx', is_read=False, start_date='2023-01-01', end_date='2023-01-31', page_index=0, page_size=10))
print(response)

# Get OTP template parameters:
response = sms_api.get_otp_parameters(ghasedak_sms.GetOtpParametersInput(template_name='YourTemplateName'))
print(response)

# Send a single SMS:
response = sms_api.send_single_sms(ghasedak_sms.SendSingleSmsInput(message='hello, world!', receptor='09xxxxxxxxx', line_number='xxxx', send_date='', client_reference_id=''))
print(response)

# Send a bulk SMS:
response = sms_api.send_bulk_sms(ghasedak_sms.SendBulkInput(message='hello, world!', receptors=['09xxxxxxxxx', '09xxxxxxxxx'], line_number='xxxx', send_date='', client_reference_id=''))
print(response)

# Send pair-to-pair SMS:
response = sms_api.send_pair_to_pair_sms(ghasedak_sms.SendPairToPairInput(items=[
    ghasedak_sms.SendPairToPairInput.SendPairToPairSmsWebServiceDto(
                line_number='123xxxxx',
                receptor='09xxxxxxxxx',
                message='Message 2',
                client_reference_id='client_ref_id',
                send_date='')], udh=False))
print(response)

# Send OTP SMS (Old Method):
oldotpcommand = ghasedak_sms.SendOldOtpInput(
        send_date='',
        receptors=[
            ghasedak_sms.SendOtpReceptorDto(
                mobile='09xxxxxxxxx',
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
response = sms_api.send_otp_sms_old(oldotpcommand)
print(response)

# Send OTP SMS (New Method):
newotpcommand = ghasedak_sms.SendOtpInput(
        send_date=None,
        receptors=[
            ghasedak_sms.SendOtpReceptorDto(
                mobile='09xxxxxxxxx',
                # client_reference_id='client_ref_id'
            )
        ],
        template_name='newOTP',
        inputs=[
            ghasedak_sms.SendOtpInput.OtpInput(param='Code', value='code'),
            ghasedak_sms.SendOtpInput.OtpInput(param='Name', value='name')
        ],
        udh=False
    )
response = sms_api.send_otp_sms(newotpcommand)
print(response)
```

## License

Released under the MIT License.
