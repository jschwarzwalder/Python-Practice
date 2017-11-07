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

question = open(file='questions.xml',mode='r').read()
new_hit = mturk.create_hit(
    Title = 'Is this Tweet happy, angry, excited, scared, annoyed or upset?',
    Description = 'Read this tweet and type out one word to describe the emotion of the person posting it: happy, angry, scared, annoyed or upset',
    Keywords = 'text, quick, labeling',
    Reward = '0.15',
    MaxAssignments = 1,
    LifetimeInSeconds = 172800,
	RequesterAnnotation='Gummi bears cookie lollipop danish bear claw marzipan chocolate bar. Dragée danish halvah caramels. Tootsie roll toffee jelly beans bonbon topping fruitcake pudding. Chocolate muffin jujubes dragée marzipan pastry biscuit muffin chocolate bar. Jujubes cho',
    AssignmentDurationInSeconds = 600,
    AutoApprovalDelayInSeconds = 14400,
    #Question = '<ExternalQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd"> <ExternalURL>https://s3.us-east-2.amazonaws.com/mturk-api-tst/index.html</ExternalURL><FrameHeight>700</FrameHeight></ExternalQuestion>'
	Question = question
)
print("A new HIT has been created. You can preview it here:")
print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
print("HITID: "+ new_hit['HIT']['HITId'])
# Remember to modify the URL above when you're publishing
# HITs to the live marketplace.
# Use: https://worker.mturk.com/mturk/preview?groupId=