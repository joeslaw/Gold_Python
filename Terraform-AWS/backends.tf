terraform {
  cloud {
    organization = "joeyslaw"

    workspaces {
      name = "joeyslaw-dev"
    }
  }
}