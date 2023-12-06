'''docstring fill me in'''
import boto3


def lambda_handler(event, context):
    '''docstring fill me in'''
    client = boto3.client('sts', region_name="us-gov-west-1")
    # ilename='saml.txt'
    print(event, context)
    # temp=open( filename, 'r').read().split('\n')
    # samlrep=temp[0]
    response = client.assume_role_with_saml(
        PrincipalArn='arn:aws-us-gov:iam::412819066487:saml-provider/ADFS',
        RoleArn='arn:aws-us-gov:iam::412819066487:role/adfs-project-administrators',
        SAMLAssertion="PHNhbWxwOlJlc3BvbnNlIElEPSJfZDliY2NiOTYtYzY4OC00NDgxLWFhNWEtMjdhN2E0MGE4YzQxIiBWZXJzaW9uPSIyLjAiIElzc3VlSW5zdGFudD0iMjAyMS0wMy0xMlQxNzozMDowMi44NTlaIiBEZXN0aW5hdGlvbj0iaHR0cHM6Ly9zaWduaW4uYW1hem9uYXdzLXVzLWdvdi5jb20vc2FtbCIgQ29uc2VudD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmNvbnNlbnQ6dW5zcGVjaWZpZWQiIHhtbG5zOnNhbWxwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiPjxJc3N1ZXIgeG1sbnM9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphc3NlcnRpb24iPmh0dHA6Ly9wcm9kLmFkZnMuZmVkZXJhdGlvbi52YS5nb3YvYWRmcy9zZXJ2aWNlcy90cnVzdDwvSXNzdWVyPjxzYW1scDpTdGF0dXM+PHNhbWxwOlN0YXR1c0NvZGUgVmFsdWU9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpzdGF0dXM6U3VjY2VzcyIgLz48L3NhbWxwOlN0YXR1cz48QXNzZXJ0aW9uIElEPSJfZTVmZjRlZDctNzRjOC00MzZjLWJmYTEtNmJmZTY2NTFkMzc1IiBJc3N1ZUluc3RhbnQ9IjIwMjEtMDMtMTJUMTc6MzA6MDIuODU5WiIgVmVyc2lvbj0iMi4wIiB4bWxucz0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmFzc2VydGlvbiI+PElzc3Vlcj5odHRwOi8vcHJvZC5hZGZzLmZlZGVyYXRpb24udmEuZ292L2FkZnMvc2VydmljZXMvdHJ1c3Q8L0lzc3Vlcj48ZHM6U2lnbmF0dXJlIHhtbG5zOmRzPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjIj48ZHM6U2lnbmVkSW5mbz48ZHM6Q2Fub25pY2FsaXphdGlvbk1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyIgLz48ZHM6U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxkc2lnLW1vcmUjcnNhLXNoYTI1NiIgLz48ZHM6UmVmZXJlbmNlIFVSST0iI19lNWZmNGVkNy03NGM4LTQzNmMtYmZhMS02YmZlNjY1MWQzNzUiPjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSIgLz48ZHM6VHJhbnNmb3JtIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIiAvPjwvZHM6VHJhbnNmb3Jtcz48ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8wNC94bWxlbmMjc2hhMjU2IiAvPjxkczpEaWdlc3RWYWx1ZT5sZzQ2Kzd2dUhFTFo0M21kTzZoRFU4WUtaRklPSmtWcVR6Ky9ZMGtTMDVjPTwvZHM6RGlnZXN0VmFsdWU+PC9kczpSZWZlcmVuY2U+PC9kczpTaWduZWRJbmZvPjxkczpTaWduYXR1cmVWYWx1ZT5tYk5mclZDSDd4NFJxcUVBcmlMb1BMOUl1WUIyWS91a2x5RDJpT0lndGQxWEFSeEF5c2ZEb1FXb3JwREtBZmRvSWowM0E1UjVNV0dRWkF5WmNFOVZZRERDdFFlVW9HWWZ3VXMvZGwzQkxwWUxQcVVvdHVqY0tpaCtON3JvTUJ4N2QrVkpXclA1ZnpCcDhCUi9qc3VDREppL2MwclFhMTJvbWFnU2IrL0VPTXU4M2VnaHY4b1Q2dWZhSFdKWjd5TFFnZmxuLzVnNlRRM25mNE8zNEdJRXRCTGVuV3Q3NDhIWnVJNEd0ZDI4dW9EcjVJcEV4VGFoWTNibWRzMGVsY01RSVBvUHNrRWJIRzV3M25hUXZGM3pya1ptSzdncFpZQURKOEVZTU1qZ2o1dE8yYXBoUTZTbzEyWHhjaG1EV2ZtV2thSUtUL1JZenp0c1hOZWpadytGMXc9PTwvZHM6U2lnbmF0dXJlVmFsdWU+PEtleUluZm8geG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiPjxkczpYNTA5RGF0YT48ZHM6WDUwOUNlcnRpZmljYXRlPk1JSUM4akNDQWRxZ0F3SUJBZ0lRSDR6c2tWTVNTSXRESGNjbDZ2Q3pvekFOQmdrcWhraUc5dzBCQVFzRkFEQTFNVE13TVFZRFZRUURFeXBCUkVaVElGTnBaMjVwYm1jZ0xTQndjbTlrTG1Ga1puTXVabVZrWlhKaGRHbHZiaTUyWVM1bmIzWXdIaGNOTVRjeE1ESTBNVGt6TVRNNFdoY05NamN4TURJeU1Ua3pNVE00V2pBMU1UTXdNUVlEVlFRREV5cEJSRVpUSUZOcFoyNXBibWNnTFNCd2NtOWtMbUZrWm5NdVptVmtaWEpoZEdsdmJpNTJZUzVuYjNZd2dnRWlNQTBHQ1NxR1NJYjNEUUVCQVFVQUE0SUJEd0F3Z2dFS0FvSUJBUURDZ0ZwcVVOVExZNmd1bG5YcEZJSFN1bzlyOG52cENPVjhBdlJuNkRQUHNPWlVJYmo0c1VhZ2tpVkoreFlFT0FpTS9ac1dxWUxYTFJyYk9oOG45eGEyOUtmOGNiZndxR0lHZFBnQVI2L2hSTDRidnQyTTBaV3p0aU0wemxSZ0JkazY1c3lUL2wrd2lmWGF4TVR2blEyNjdqNXdDYlkwZFNDWjhXZXNEalB6UTlNd0NMdmJjQzVsU2VzWVlYckw1dllEeDBuenRwT3lJRDB4Y0sxemQvTHhQcXViL2NFbWhZMnZlMXpISHFVblR3eG9KL1huamE2THJQZmx5UkJFYi9CRGtRNlpYL3NiUENFUmFVV3ptOHk0ZFJYdk43blhMR3RiV1RiSkFKSVlxUTdsd0E3T1hBeG9lTVo3a1J1VTRhaHVkL0FyajhmaHhJMnpMbkhuTERxckFnTUJBQUV3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQUcvaE5ybURxZ0VoWjhBY3pxdkh3aW91a3N1RUJxcXByOHRLMnEzRDk3ZkpOQmluWnB3SERKZWZma3grOVBiWnpvYU1rQ01ER3ZYck0zQUhyT09HU3l6dnVsQXdHc1FBbnZaM3B1WHdrYVMrOUNVVWJCTUs0S1FuTEpIbExFSC9rNkx1bkliMkZNUUJoT2hkYlJXb1ljcmMxdTYxbGpaMEJLV1JOWHBmN0lMZlZJbzBTQ3JFb0FrZU9RQWRPbVRWcE8reEtPVk1jbXRRY3NWVzBpSmRKaTV4dGdJa0V2cVhKVDhySjBaalkvZEVZaUtMdUNoWDUvQnd6dFlkZWZFcVlyNHAxOGl4M0daOTRYU1ZUWVFjZ0RpS0dmY3FwdmlURW15RGtQRXdzbFVoQlQwQzlaZ1hITTFkTGYra2pjcndwcTh5ckEyMndOcHJabUdqUkQ5SkIvbz08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvS2V5SW5mbz48L2RzOlNpZ25hdHVyZT48U3ViamVjdD48TmFtZUlEIEZvcm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6cGVyc2lzdGVudCI+VkhBMTlcT0lURUNIQ3JvY2tLPC9OYW1lSUQ+PFN1YmplY3RDb25maXJtYXRpb24gTWV0aG9kPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6Y206YmVhcmVyIj48U3ViamVjdENvbmZpcm1hdGlvbkRhdGEgTm90T25PckFmdGVyPSIyMDIxLTAzLTEyVDE3OjM1OjAyLjg1OVoiIFJlY2lwaWVudD0iaHR0cHM6Ly9zaWduaW4uYW1hem9uYXdzLXVzLWdvdi5jb20vc2FtbCIgLz48L1N1YmplY3RDb25maXJtYXRpb24+PC9TdWJqZWN0PjxDb25kaXRpb25zIE5vdEJlZm9yZT0iMjAyMS0wMy0xMlQxNzozMDowMi43NDlaIiBOb3RPbk9yQWZ0ZXI9IjIwMjEtMDMtMTJUMTg6MzA6MDIuNzQ5WiI+PEF1ZGllbmNlUmVzdHJpY3Rpb24+PEF1ZGllbmNlPmh0dHBzOi8vc2lnbmluLmFtYXpvbmF3cy11cy1nb3YuY29tL3NhbWw8L0F1ZGllbmNlPjwvQXVkaWVuY2VSZXN0cmljdGlvbj48L0NvbmRpdGlvbnM+PEF0dHJpYnV0ZVN0YXRlbWVudD48QXR0cmlidXRlIE5hbWU9Imh0dHBzOi8vYXdzLmFtYXpvbi5jb20vU0FNTC9BdHRyaWJ1dGVzL1JvbGVTZXNzaW9uTmFtZSI+PEF0dHJpYnV0ZVZhbHVlPkt1cnQuQ3JvY2tldHRAdmEuZ292PC9BdHRyaWJ1dGVWYWx1ZT48L0F0dHJpYnV0ZT48QXR0cmlidXRlIE5hbWU9Imh0dHBzOi8vYXdzLmFtYXpvbi5jb20vU0FNTC9BdHRyaWJ1dGVzL1JvbGUiPjxBdHRyaWJ1dGVWYWx1ZT5hcm46YXdzLXVzLWdvdjppYW06OjQxMjgxOTA2NjQ4NzpzYW1sLXByb3ZpZGVyL0FERlMsYXJuOmF3cy11cy1nb3Y6aWFtOjo0MTI4MTkwNjY0ODc6cm9sZS9hZGZzLXByb2plY3QtcmVhZG9ubHk8L0F0dHJpYnV0ZVZhbHVlPjxBdHRyaWJ1dGVWYWx1ZT5hcm46YXdzLXVzLWdvdjppYW06OjQxMjgxOTA2NjQ4NzpzYW1sLXByb3ZpZGVyL0FERlMsYXJuOmF3cy11cy1nb3Y6aWFtOjo0MTI4MTkwNjY0ODc6cm9sZS9hZGZzLXByb2plY3QtYWRtaW5pc3RyYXRvcnM8L0F0dHJpYnV0ZVZhbHVlPjwvQXR0cmlidXRlPjwvQXR0cmlidXRlU3RhdGVtZW50PjxBdXRoblN0YXRlbWVudCBBdXRobkluc3RhbnQ9IjIwMjEtMDMtMTJUMTM6NDQ6NDIuMDM0WiIgU2Vzc2lvbkluZGV4PSJfZTVmZjRlZDctNzRjOC00MzZjLWJmYTEtNmJmZTY2NTFkMzc1Ij48QXV0aG5Db250ZXh0PjxBdXRobkNvbnRleHRDbGFzc1JlZj51cm46ZmVkZXJhdGlvbjphdXRoZW50aWNhdGlvbjp3aW5kb3dzPC9BdXRobkNvbnRleHRDbGFzc1JlZj48L0F1dGhuQ29udGV4dD48L0F1dGhuU3RhdGVtZW50PjwvQXNzZXJ0aW9uPjwvc2FtbHA6UmVzcG9uc2U+"
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
    print(
        f"aws_secret_access_key = {response['Credentials']['SecretAccessKey']}")
    print(f"aws_session_token = {response['Credentials']['SessionToken']}")
    print('region = us-gov-west-1')
    print()
    print("=" * 30)
    print("#AWS ENV VARIABLES")
    print("=" * 30)
    print(
        f"export AWS_ACCESS_KEY_ID={response['Credentials']['AccessKeyId']}")
    print(
        f"export AWS_SECRET_ACCESS_KEY={response['Credentials']['SecretAccessKey']}")
    print(
        f"export AWS_SESSION_TOKEN={response['Credentials']['SessionToken']}")
    print('export AWS_DEFAULT_REGION=us-gov-west-1')

# print()
# print("=" * 30)
# print("#Visual Studio Code os.environ VARIABLES")
# print("=" * 30)
# # Used in Visual Studio Code app.py file
# print('os.environ["APP_ENV"] = "sandbox"')
# print('os.environ["AWS_ACCESS_KEY_ID"] = "{}"'.format(
#     response['Credentials']['AccessKeyId']))
# print('os.environ["AWS_SECRET_ACCESS_KEY"] = "{}"'.format(
#     response['Credentials']['SecretAccessKey']))
# print('os.environ["AWS_SESSION_TOKEN"] = "{}"'.format(
#     response['Credentials']['SessionToken']))
# print('os.environ["AWS_DEFAULT_REGION"] = "us-gov-west-1"')
# print()
