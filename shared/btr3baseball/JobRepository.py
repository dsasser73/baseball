import boto3
import uuid

class JobRepository:
    def __init__(self, jobTable):
        self.table = boto3.resource('dynamodb').Table(jobTable)
        
    def getJob(self, jobId):
        try:
            response = self.table.get_item(
                Key={
                    'job-id': jobId
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
            return None
        else:
            item = response['Item']
            return item

    def createJob(self, config):
        # Generate job ID uuid
        jobId = str(uuid.uuid4())

        response = dynamo.put_item(
            Item={
                'job-id': jobId,
                'job-details': config
            }
        )

        return jobId

    def updateForSuccess(self, jobId):
        print('Updating job record for success')
        response =  self.table.update_item(
            Key={
                'job-id': jobId
            },
            UpdateExpression="set #K = :m",
            ExpressionAttributeNames={
                "#K":"job-status"
            },
            ExpressionAttributeValues={
                ':m': "COMPLETE",
            },
            ReturnValues="UPDATED_NEW"
        )
        return response

    def updateForError(self, jobId):
        print('Updating job record for error')

    def updateWithMessageId(self, jobId, messageId):
        response =  table.update_item(
            Key={
                'job-id': jobId
            },
            UpdateExpression="set #K = :m",
            ExpressionAttributeNames={
                "#K":"message-id"
            },
            ExpressionAttributeValues={
                ':m': response.get('MessageId'),
            },
            ReturnValues="ALL_NEW"
        )

        return response['Attributes']

