data "aws_availability_zones" "available_zones" {
  state = "available"
}

resource "aws_vpc" "birdy_vpc" {
  cidr_block           = var.vpc_cidr_block
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name        = "unavailable_dispatch_vpc"
    Environment = "Production"
  }
}

resource "aws_subnet" "aws_pub_subnet_us_east_1a" {
    vpc_id = aws_vpc.birdy.id
    cidr_block = var.pub_cidr_block
    available_zones = "us-east-1a"
    map_public_ip_on_lauche = true
    tags = {
      Name = "public_subnet"
    }
}


resource "aws_subnet" "aws_priv_subnet_us_east_1a" {
    vpc_id = aws_vpc.birdy.id
    cidr_block = var.priv_cidr_block
    available_zones = "us-east-1a"
    map_public_ip_on_lauche = false
    tags = {
      Name = "private_subnet"
    }
}


resource "aws_eip" "nat" {
  domain = "vpc"

  tags = {
    Name = "my-nat-eip"
  }
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id
  subnet_id = aws_subnet.public.id
  tags = {
    Name = "my-nat-gateway
  }
}

resource "aws_route_table" "priv_route_us_east_1a" {
  vpc_id = aws_vpc.birdy_vpc

  route {
    cidr_block = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }

  tags = {
    Name = "priv_route_table_for_Internet_connection"
  }
}


resource "aws_route_table_association" "priv_subnet_us_east_1a" {
  subnet_id = aws_subnet.aws_priv_subnet_us_east_1a.id
  route_table_id = aws_route_table.priv_route_us_east_1a
}