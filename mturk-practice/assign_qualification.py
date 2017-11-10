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



qualification = mturk.associate_qualification_with_worker(
	QualificationTypeId='3GYFFIV9O7JFOL6SRMAIZ0VAJ8GYDQ',
    WorkerId='AI5E2DKKVGEDF',
    SendNotification=True
)
	

print ("my qualification: \n" + str(qualification))   

#{'QualificationType': {'QualificationTypeId': '385F8X38SRM1P2YZWVXXQL9VG440L8', 'CreationTime': datetime.datetime(2017, 11, 10, 15, 7, 14, tzinfo=tzlocal()), 'Name': 'new-qualification', 'Description': 'This is only a test', 'Keywords': 'string', 'QualificationTypeStatus': 'Active', 'RetryDelayInSeconds': 123, 'IsRequestable': True, 'AutoGranted': True, 'AutoGrantedValue': 1}, 'ResponseMetadata': {'RequestId': 'e3ddbeeb-c66b-11e7-bc87-2fb5cc56b8cb', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'e3ddbeeb-c66b-11e7-bc87-2fb5cc56b8cb', 'content-type': 'application/x-amz-json-1.1', 'content-length': '312', 'date': 'Fri, 10 Nov 2017 23:07:14 GMT'}, 'RetryAttempts': 0}} 

# My worker sandbox id Your Worker ID: AI5E2DKKVGEDF
# Taldar, Taneem: A3W3ZDEZCZBE67
