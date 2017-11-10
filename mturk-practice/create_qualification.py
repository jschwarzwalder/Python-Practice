import boto3
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
mturk = boto3.client('mturk',
   aws_access_key_id = "PASTE_YOUR_IAM_USER_ACCESS_KEY",
   aws_secret_access_key = "PASTE_YOUR_IAM_USER_SECRET_KEY",
   region_name='us-east-1',
   # In Sandbox, the get_account_balance() call always returns $10,000. 
   # In order to connect to the live MTurk marketplace, just leave out the endpoint parameter on next line
   endpoint_url = MTURK_SANDBOX
)
print("I have $" + mturk.get_account_balance()['AvailableBalance'] + " in my Sandbox account")



qualification = mturk.create_qualification_type(
	Name='new-qualification',
    Keywords='string',
    Description='This is only a test',
    QualificationTypeStatus='Active',
    RetryDelayInSeconds=123,
    AutoGranted=True
    
)
	# Test='string', XML Question like for HIT
	# TestDurationInSeconds=123,
    # AnswerKey='string',
	# AutoGrantedValue=1

print ("my qualification: \n" + str(qualification))   

#{'QualificationType': {'QualificationTypeId': '385F8X38SRM1P2YZWVXXQL9VG440L8', 'CreationTime': datetime.datetime(2017, 11, 10, 15, 7, 14, tzinfo=tzlocal()), 'Name': 'new-qualification', 'Description': 'This is only a test', 'Keywords': 'string', 'QualificationTypeStatus': 'Active', 'RetryDelayInSeconds': 123, 'IsRequestable': True, 'AutoGranted': True, 'AutoGrantedValue': 1}, 'ResponseMetadata': {'RequestId': 'e3ddbeeb-c66b-11e7-bc87-2fb5cc56b8cb', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'e3ddbeeb-c66b-11e7-bc87-2fb5cc56b8cb', 'content-type': 'application/x-amz-json-1.1', 'content-length': '312', 'date': 'Fri, 10 Nov 2017 23:07:14 GMT'}, 'RetryAttempts': 0}} 