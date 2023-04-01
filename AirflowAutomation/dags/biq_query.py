from google.cloud import bigquery
project_name, dataset_name, table_name = None, None, None
client = bigquery.Client()

query = f"""
    select * from `{project_name}.{dataset_name}.{table_name}`
"""
results = client.query(query)
for row in results:
    id = row['id']
    description = row['description']
    print(id,description)
