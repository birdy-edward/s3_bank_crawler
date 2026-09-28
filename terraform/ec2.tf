data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "gha_runner" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  key_name      = var.gha_runner_key_name
  subnet_id = aws_subnet.aws_priv_subnet_us_east_1a.id
  
  user_data = file(var.gha_setup_file)

  tags = {
    Name = "GHA Runner Instance PC"
  }
}