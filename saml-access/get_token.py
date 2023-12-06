#!/usr/bin/python
import boto3
client = boto3.client('sts', region_name="us-gov-west-1")
filename = 'saml.txt'
#temp = open(filename, 'r', encoding='utf-8').read().split('\n')
#samlrep = temp[0]
samlrep = ''

# response = client.assume_role_with_saml(
#     PrincipalArn='arn:aws-us-gov:iam::412819066487:saml-provider/ADFS',
#     RoleArn='arn:aws-us-gov:iam::412819066487:role/adfs-project-administrators',
#     SAMLAssertion=samlrep
# )

response = client.assume_role_with_saml(
    PrincipalArn='arn:aws-us-gov:iam::227763086662:saml-provider/ADFS',
    RoleArn='arn:aws-us-gov:iam::227763086662:role/adfs-project-administrators',
    SAMLAssertion=samlrep
)

print(response['Credentials'])

# for key, value in response['Credentials'].items():
#         print key, value


print('\n' * 10)
print("=" * 30)
print("#AWS CONFIG CREDENTIALS FILE")
print("=" * 30)

print('[tempaccount]')
print(f"aws_access_key_id = {response['Credentials']['AccessKeyId']}")
print(f"aws_secret_access_key = {response['Credentials']['SecretAccessKey']}")
print(f"aws_session_token = {response['Credentials']['SessionToken']}")
print('region_name = \'us-gov-west-1\'')
print()

print('.py')
print(f"aws_access_key_id = '{response['Credentials']['AccessKeyId']}',")
print(f"aws_secret_access_key = '{response['Credentials']['SecretAccessKey']}',")
print(f"aws_session_token = '{response['Credentials']['SessionToken']}',")
print('region_name = \'us-gov-west-1\'')
print()
print("=" * 30)
print("#AWS ENV VARIABLES")
print("=" * 30)
print(f"export AWS_ACCESS_KEY_ID={response['Credentials']['AccessKeyId']}")
print(f"export AWS_SECRET_ACCESS_KEY={response['Credentials']['SecretAccessKey']}")
print(f"export AWS_SESSION_TOKEN={response['Credentials']['SessionToken']}")
print('export AWS_DEFAULT_REGION=us-gov-west-1')
