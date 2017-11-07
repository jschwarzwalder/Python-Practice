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

HITID = '3Q9SPIIRWJ4KEMM81ZK9CSHOK3QAWE'
HITID = '3FW4EL5A3L69X3TXA02NI3I148I22W'
HITID = '3TRB893CSJS6YYYAFR47GYTAP4NG7H'

new_hit = mturk.delete_hit(HITId = HITID)