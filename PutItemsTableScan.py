import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('FavoriteMovies')

with table.batch_writer() as batch:
    batch.put_item(Item={'Movie Name': 'Moneyball', 'Year Released': 2011,})
    batch.put_item(Item={'Movie Name': 'Fight Club', 'Year Released': 1999,})
    batch.put_item(Item={'Movie Name': 'Catch Me If You Can', 'Year Released': 2002,})
    batch.put_item(Item={'Movie Name': 'Burnt', 'Year Released': 2015,})
    batch.put_item(Item={'Movie Name': 'Happy Gilmore', 'Year Released': 1996,})
    batch.put_item(Item={'Movie Name': 'The Big Short', 'Year Released': 2015,})
    batch.put_item(Item={'Movie Name': 'Dodgeball', 'Year Released': 2004,})
    batch.put_item(Item={'Movie Name': 'Ford v Ferrari', 'Year Released': 2019,})
    batch.put_item(Item={'Movie Name': 'Gone in 60 Seconds', 'Year Released': 2000,})
    batch.put_item(Item={'Movie Name': 'John Wick', 'Year Released': 2014,})
    batch.put_item(Item={'Movie Name': "Ocean's Eleven", 'Year Released': 2001,}
    )
response = table.scan()
response['Items']

print(response)