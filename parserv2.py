import json
import boto3

file_name = 'output.json'

# Begin connection to DynamoDB
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')

# Get array of table names associated with current AWS account
table_names = client.list_tables()

# Read json data from json file and store in json_data
with open(file_name, 'r') as data_file:
    json_data = data_file.read()

# Store list where each item is a dict
img_result_list = json.loads(json_data)

# Check if table exists
def checkExists():
	if not 'imagetags' in table_names['TableNames']:
		#If imagetags table does not exists, create it
		table = dynamodb.create_table(
			TableName = 'imagetags',
			KeySchema =
			[
				{
					'AttributeName': 'username',
					'KeyType': 'HASH'
				}				
			],
			AttributeDefinitions =
			[
				{
					'AttributeName': 'username',
					'AttributeType': 'S'
				}
			],
			ProvisionedThroughput =
				{
					'ReadCapacityUnits': 5,
					'WriteCapacityUnits': 5
				}
		 )
		# Wait until the table exists.
		table.meta.client.get_waiter('table_exists').wait(TableName='imagetags')
	        insertTuples(table)
	else:
	    # If the table exists, insert tuples
	    table = dynamodb.Table('imagetags')
            insertTuples(table)


def insertTuples(table, img_result_list = img_result_list):
	prev_user = ''
	count = 0
	obj = {}
	fields = []
	result = []
	for img in img_result_list:
		# Access each individual images rekognizer output
		file_name = img["File_Name"] #store name
		labels_list = img["Analysis"]["Labels"] #list of tags
                username = str(file_name.split('/')[1].strip()) #get username from filepath
		#Put this item name and labels in a dictionary for easy tuple insert
		if(username != prev_user):
		    if(count > 0):
			obj['username'] = prev_user
			obj['fields'] = fields    
			result.append(obj.copy())
			fields = [] #reset fieilds for next username
			count = 0
		    for label in labels_list:
		        fields.append(label['Name'])
		    count = count + 1
		    prev_user = username
		else:
		    #User is not new
		    for label in labels_list:
		        fields.append(label['Name'])
		    count = count + 1
	# At the end add the last username and list 
	obj['username'] = username
	obj['fields'] = fields
	result.append(obj.copy())
	list_items = []
        for i in result:
	    num = 1
	    #For each username list pair in results
	    item = {}
	    item['username'] = i['username']
	    for tag in i['fields']:
		label_string = 'label' + str(num)
		item[label_string] = tag
	        num += 1
	    list_items.append(item.copy())
	    for user in list_items:
	        table.put_item(Item = user)    
checkExists()

