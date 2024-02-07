import boto3

ecr_client = boto3.client('ecr')

repoistory_name = "cloud-native-monitoring"
response = ecr_client.create_repository(
  repositoryName=repoistory_name
)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
