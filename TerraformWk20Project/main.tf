resource "aws_vpc" "main" {
    cidr_bock = "10.1.0.0/16"

    tags = {
        Name = "Wk20Project VPC"
    }

}