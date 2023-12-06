import boto3
import os

def download_files_from_s3(bucket_name, s3_keys, destination_folder):
    # Create an S3 client
    s3_client = boto3.client('s3',
aws_access_key_id ='',
aws_secret_access_key = '',
aws_session_token = '',
region_name = 'us-gov-west-1'
)

    for s3_key in s3_keys:
        # Define the local filename to save the file
        head, tail = os.path.split(s3_key)
        local_filename = os.path.join(destination_folder, tail)

        # Download the file from S3
        try:
            s3_client.download_file(bucket_name, s3_key, tail)
            print(f"Downloaded {s3_key} to {tail}")
        except:
            print(f"Failed {s3_key} to {tail}")


# Example usage
bucket_name = 'dev-vfmp-835'
s3_keys = ['eprs-835-split-batch/835E.singlebatch_SM1']  # List of file keys in S3
destination_folder = 'out'  # Local path to store files

bucket_name = 'prod-vfmp-837'
s3_keys = [
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000012547.20230928.042327',
'to-pitandcxm-from-edi-goodbatch837/837I.84146.VFMP.000012772.20230930.044043',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000013099.20231003.052007',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000013202.20231003.070936',
'to-pitandcxm-from-edi-goodbatch837/837I.84146.VFMP.000013212.20231004.052433',
'to-pitandcxm-from-edi-goodbatch837/837I.84146.VFMP.000013332.20231005.055555',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000013333.20231005.062011',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000013435.20231005.071928',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000013446.20231006.032133',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000013995.20231010.073501',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000014127.20231012.062448',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000014444.20231014.082140',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000014913.20231019.054942',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000015016.20231019.093816',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000015027.20231020.055453',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000015140.20231021.054912',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000015477.20231024.033905',
'to-pitandcxm-from-edi-goodbatch837/837I.84146.VFMP.000015823.20231027.055500',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000015822.20231027.055037',
'to-pitandcxm-from-edi-goodbatch837/837I.80214.VFMP.000015840.20231028.061128',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000016162.20231031.055613',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000016266.20231031.074118',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000016383.20231101.073652',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000016395.20231102.050710',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000016497.20231102.064933',
'to-pitandcxm-from-edi-goodbatch837/837I.84146.VFMP.000016508.20231103.032602',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000016511.20231103.071900',
'to-pitandcxm-from-edi-goodbatch837/837P.80214.VFMP.000016523.20231104.062133',
'to-pitandcxm-from-edi-goodbatch837/837P.84146.VFMP.000016797.20231109.045031']

download_files_from_s3(bucket_name, s3_keys, destination_folder,)


# print(f"aws_access_key_id = {response['Credentials']['AccessKeyId']}")
# print(f"aws_secret_access_key = {response['Credentials']['SecretAccessKey']}")
# print(f"aws_session_token = {response['Credentials']['SessionToken']}")
# print('region = us-gov-west-1')


#  s3_client = boto3.client('s3', 
#                       aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY, 
#                       aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY, 
#                       region_name=REGION_NAME
#                       )


# [9:32 AM] Cao, William "Billy" (SAIC)
 

# project-ped-clientzone-prod/vaclaimsxm/outgoing/999.80214.clrnghs.002327756.20231004.065810
# project-ped-clientzone-prod/vaclaimsxm/outgoing/999.80214.clrnghs.002328898.20231107.115058


# project-ped-clientzone-prod/vapit/outgoing
 
# [9:33 AM] Cao, William "Billy" (SAIC)
# Amazon S3
# Buckets
# prod-vfmp-837
# to-pitandcxm-from-edi-goodbatch837/
 