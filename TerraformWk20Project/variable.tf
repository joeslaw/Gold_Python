variable "public_subnet_cidr" {
  type = list(string)
  description = "Public Subnet CIDR #1 & #2 Values"
  default = ["10.1.1.0/24", "10.1.2.0/24"]
}