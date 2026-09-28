terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.84.0"

    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.0"
    }
  }
  backend "s3" {
    encrypt        = true
  }
}


provider "aws" {
  region = "us-east-1"
}