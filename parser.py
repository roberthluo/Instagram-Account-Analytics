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
					'AttributeName': 'filename',
					'KeyType': 'HASH'
				}
			],
			AttributeDefinitions =
			[
				{
					'AttributeName': 'filename',
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
	for img in img_result_list:
		# Access each individual images rekognizer output
		file_name = img["File_Name"] #store name
		labels_list = img["Analysis"]["Labels"] #list of tags

		# Put this item name and labels in a dictionary for easy tuple insert
		item = {}
		item['filename'] = file_name

		count = 1
		# Add each label to the item
		for label in labels_list:
			label_string = 'label' + str(count)
			item[label_string] = label['Name']
			count+=1

		# Put the item in the DB
		table.put_item(Item = item)
checkExists()
