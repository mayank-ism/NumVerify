import sys
import requests

total_args = len(sys.argv)
phone_number = '';

if total_args == 1:
	print "Enter the number to validate."
	phone_number = raw_input()
else:
	phone_number = sys.argv[1]

if len(phone_number) == 10:
	phone_number = '+91' + phone_number
elif len(phone_number) == 11 and phone_number[0] == '0':
	phone_number = '+91' + phone_number[1:]


print "Phone number is " + phone_number

access_key = 'a65976cc48a83b234e1b7177d0b3840f'
url = 'http://apilayer.net/api/validate?access_key=' + access_key + '&number=' + phone_number
response = requests.get(url)
#print response.content
answer = response.content[9:13]

if answer == "true":
	print phone_number + " is valid."
else:
	print phone_number + " is invalid."

