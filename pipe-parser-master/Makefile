.PHONY:

LAMBDA_NAME=pipe-parser

export AWS_DEFAULT_REGION=us-east-1

export S3_AWS_ACCESS_KEY_ID=
export S3_AWS_SECRET_ACCESS_KEY=

export AWS_ACCESS_KEY_ID=$(S3_AWS_ACCESS_KEY_ID)
export AWS_SECRET_ACCESS_KEY=$(S3_AWS_SECRET_ACCESS_KEY)

export S3_BUCKET=ewfweffwewefwewefwefwefwe
export FILENAME=asdfb.12115.20230101.20360

ACCOUNT=
REPO=$(ACCOUNT).dkr.ecr.us-east-1.amazonaws.com

run:
	python main.py

call:
	curl -XPOST localhost:8080/2015-03-31/functions/function/invocations -d @event-sample.json

create_upload_role:
	# needs cloudwatch logs and s3 permissions too
	aws iam create-role --role-name lambda-ex --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

upload:
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $(REPO)
	docker build . -t $(REPO)/$(LAMBDA_NAME):latest
	docker push $(REPO)/$(LAMBDA_NAME):latest

createlambda:
	aws lambda create-function \
	--function-name $(LAMBDA_NAME) \
	--package-type Image \
	--code ImageUri=$(REPO)/$(LAMBDA_NAME):latest \
	--role arn:aws:iam::$(364348584564):role/lambda-ex

uploaddoc:
	aws s3 rm s3://$(S3_BUCKET)/incoming/$(FILENAME)
	aws s3 cp ./data/$(FILENAME) s3://$(S3_BUCKET)/incoming/
