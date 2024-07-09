
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
sms_api = ghasedak_sms.Ghasedak(baseurl="http://your_base_url/api/v1", apikey="Your APIKEY")

# Check SMS status:
response = sms_api.check_sms_status(ids=['messageId1', 'messageId2'], type='1')
print(response)

# Get account information:
response = sms_api.get_account_information()
print(response)

# Get received SMSes:
response = sms_api.get_received_smses(linenumber='xxxx', isread=False)
print(response)

# Get received SMSes with pagination:
response = sms_api.get_received_smses_paging(linenumber='xxxx', isread=False, startdate='2023-01-01', enddate='2023-01-31', pageindex=0, pagesize=10)
print(response)

# Get OTP template parameters:
response = sms_api.get_otp_template_parameters(templatename='YourTemplateName')
print(response)

# Send a single SMS:
response = sms_api.send_single_sms(message='hello, world!', receptor='09xxxxxxxxx', linenumber='xxxx', senddate='', checkid='')
print(response)

# Send a bulk SMS:
response = sms_api.send_bulk_sms(message='hello, world!', receptors=['09xxxxxxxxx', '09xxxxxxxxx'], linenumber='xxxx', senddate='', checkid='')
print(response)

# Send pair-to-pair SMS:
response = sms_api.send_pair_to_pair_sms(items=[{'message': 'hello', 'receptor': '09xxxxxxxxx', 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''}], udh=False)
print(response)

# Send OTP SMS:
response = sms_api.send_otp_sms(receptor='09xxxxxxxxx', message='Your OTP message')
print(response)
```

## License

Released under the MIT License.
