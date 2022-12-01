terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.23.0"
    }
  }
}

resource "random_string" "random" {
  count = 1  
  length  = 4
  special = false
  upper   = false
}

provider "docker" {}


resource "docker_image" "nodered_image" {
  name = "nodered/node-red:latest"
}

resource "docker_container" "nodered_container" {
  count = 1  
  name  = join("-", ["nodered", random_string.random[count.index].result])
  image = docker_image.nodered_image.latest
  ports {
    internal = 1880
    #external = 1880
  }
}

output "ip-address" {
    value = [for i in docker_container.nodered_container[*]: join(":", [i.ip_address],i.ports[*]["external"])]
    description = "The IP address and external port of the container"
}

output "container-name" {
    value = docker_container.nodered_container[*].name
    description = "The name of the container"

}

