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
    bucket         = "unavailable-dispatch-terraform-backend"
    key            = "terraform-backend-file.tfstate"
    region         = "ap-southeast-2"
    encrypt        = true
  }
}


provider "aws" {
region = "ap-southeast-2"
}