#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo "Usage: $0 <output_path>"
    exit 1
fi

export PATH_TO_CHECK="$1"

export AWS_ACCESS_KEY_ID="$2"
export AWS_SECRET_ACCESS_KEY="$3"
export AWS_SESSION_TOKEN="$4"
export AWS_DEFAULT_REGION="$5"

if [ -e "$PATH_TO_CHECK" ]; then
    echo "Path already existed"
else
    mkdir -p "$PATH_TO_CHECK"
fi

echo "Crawling..."
sleep 2
echo "Waiting respond..."
python main.py --output_path "$PATH_TO_CHECK"

echo "Perhaps...Completed"

echo "Please provide AWS credential in advance..."

if [ -z "$AWS_ACCESS_KEY_ID" ]; then
    read -r -s -p "Enter access key: " AWS_ACCESS_KEY_ID; echo
fi
if [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
    read -r -s -p "Enter secret access key: " AWS_SECRET_ACCESS_KEY; echo
fi


if [ -z "$AWS_SESSION_TOKEN" ]; then
    read -r -s -p "Enter session token: " AWS_SESSION_TOKEN; echo
fi
if [ -z "$AWS_DEFAULT_REGION" ]; then
    read -r -p "Enter region [us-east-1]: " AWS_DEFAULT_REGION
    AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION:-us-east-1}"
fi

export AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN AWS_DEFAULT_REGION

echo "Verifying AWS credentials..."
if ! aws sts get-caller-identity > /dev/null; then
    echo "AWS credentials are invalid or expired"
    exit 1
fi
echo "AWS credentials OK"

if [ -e "$PATH_TO_CHECK" ]; then
    echo "Logos are placed in $PATH_TO_CHECK/"
    echo "Start uploading..."
    aws s3 cp "./$PATH_TO_CHECK/" s3://nonprod/play_ground --recursive
else
    echo "The path has not established yet..."
fi
