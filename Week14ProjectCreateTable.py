import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table (
    TableName = 'FavoriteMovies',
        KeySchema = [
           {
               'AttributeName': 'Movie Name',
               'KeyType': 'HASH'
           },
           {
               'AttributeName': 'Year Released',
               'KeyType': 'RANGE'
           }
           ],
           AttributeDefinitions = [
               {
                   'AttributeName': 'Movie Name',
                   'AttributeType': 'S'
               },
               {
                   'AttributeName':'Year Released',
                   'AttributeType': 'N'
               }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
            }
)