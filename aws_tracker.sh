#!/bin/bash

############################################################
#Author: Sudhanshu
#Date: 10th April,2026
#
#Version:v1
#
#This script will report the AWS resource usage
############################################################
set -x

#AWS S3
#List S3 Buckets
echo "S3 list"
aws s3 ls

echo "EC2 LIST"
#AWS EC2
#List EC2 instances
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId'

echo "Lambda List"

#AWS LAMBDA
#List AWS LAMBDA 
aws lambda list-functions

echo "IAM user"
#AWS IAM USERS
#List IAM users
aws iam list-users


