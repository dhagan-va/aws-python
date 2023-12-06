3/16/2021
Created lambda function in AWS called project-ped-aws-saml.
The code for the lambda (lambda_function.py) is in the folder project-ped-aws-saml.

NOTE: You get 1 hour before the credentials exipire.

1. Login to AWS and go to the lambda service and open the lambda function called project-ped-aws-saml.
2. Go to the section Code Source.
3. Double click on the lambda_function.py to edit the source code.
4. Read the section "Copy the "SAML Responses:" text" on how to get the Saml response in the file VAEC_How_To_Guide_AWS_Temp_Creds_for_CLI_with_VA_SSO.pdf.
5. Once you have this copied in the clipboard, paste it in the code on line 15 of the lambda_function.py. The previous saml response will be there, so you will need
   to select it and delete between the quotes. Then paste the new one.

      SAMLAssertion="...paste the new saml response here..."

6. Now click the Deploy button to save the code and deploy the new change.
7. Now click the Test button to run the code and you will have the new security credentials needed for 3 types of need.

To debug in Visual Studio, copy the output of the 4 lines of code under:
Visual Studio Code os.environ VARIABLES

Note: The python code reads the AWS environment variable, so you will need that. Here's an Example:

#Code for local debugging
os.environ['APP_ENV']='sandbox'  // MAKE SURE YOU HAVE THIS FIRST
os.environ["AWS_ACCESS_KEY_ID"] = "fill me in"
os.environ["AWS_SECRET_ACCESS_KEY"] = "fill me in"
os.environ["AWS_SESSION_TOKEN"] = "fill me in"
os.environ["AWS_DEFAULT_REGION"] = "us-gov-west-1"


In launch.json

        {
            "name": "Python: ped-835-batch-jobs ",
            "type": "python",
            "request": "launch",
            "program": "app.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}\\scripts\\aws\\python\\cdk\\ped-835-batch-jobs",
            "envFile": "${workspaceRoot}\\scripts\\aws\\python\\dev.env"
        },

This is the python code below. You can see that we need to set the APP_ENV along with the AWS credentials in the above code.

#Load app specific environment variable
app_env = os.environ['APP_ENV']

#Load config settings file
settings = ConfigUtil.read_config()

batch_jobs_settings = ConfigUtil.read_config(directory="../" + settings['BatchJobsProj'])
comp_envs_settings = ConfigUtil.read_config(directory="../" + settings['ComputeEnvProj'])
lambdas_settings = ConfigUtil.read_config(directory="../" + settings['LambdasProj'])

stack_cpe_name = settings['StackNameCpe'].replace("app_env", app_env)

###############################################################################################




https://prod.adfs.federation.va.gov/adfs/ls/idpinitiatedsignon.aspx

alias python='/c/Program\ Files/Amazon/AWSCLI/runtime/python.exe'
python -m pip install boto3


https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html


I tried to install to automate this -
https://medium.com/@tsriharsha/understanding-sso-to-aws-console-via-saml-ef76c898c4bd