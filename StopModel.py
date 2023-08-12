
import boto3
import time


def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')
    
def main():
    
    model_arn='arn:aws:rekognition:us-east-1:288936085333:project/skin_undertone_balanced/version/skin_undertone_balanced.2023-08-12T14.56.33/1691841392358'
    stop_model(model_arn)

if __name__ == "__main__":
    main() 