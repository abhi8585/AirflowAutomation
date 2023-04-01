# Insert values in a table
from google.cloud import bigquery
client = bigquery.Client()
dataset_id = "DATASET_ID"
# For this sample, the table must already exist and have a defined schematable_id = ‘test_table_creation’
table_ref = client.dataset(dataset_id).table("uploaded_images")
table = client.get_table(table_ref)
# Creating a list of tuples with the values that shall be inserted into the tablerows_to_insert = [
rows_to_insert=[(2,'image2.png')
]
errors = client.insert_rows(table, rows_to_insert) 
print(errors)