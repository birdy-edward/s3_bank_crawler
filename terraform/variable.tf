variable "vpc_cidr_block" {
    description = "the CIDR range of VPC"
    type = string
    default = "100.95.108.0/22"
}


variable "pub_cidr_block" {
    description = "the CIDR range of public subnet"
    type = string
    default = "100.95.111.64/26"
}


variable "priv_cidr_block" {
    description = "the CIDR range of private subnet"
    type = string
    default = "100.95.108.00/24"
}

variable "gha_setup_file" {
    description = "GHA scripts used internally when initiating EC2"
    type = string
}