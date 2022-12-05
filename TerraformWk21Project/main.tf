# --- root/main.tf ---
module "EC2" {
    source = "./EC2"
    ami_id = "ami-830c94e3"
    instance_type = "t2.micro"
}