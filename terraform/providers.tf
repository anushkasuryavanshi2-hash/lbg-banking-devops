
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }

  backend "azurerm" {
    storage_account_name = "lbgbankingtfstate2026"
    container_name       = "tfstate"
    key                  = "banking-dev.tfstate"
    use_cli              = true
    use_azuread_auth     = true
  }
}

provider "azurerm" {
  features {}

  subscription_id = "bdfe5d64-0777-49b7-b8ed-8dd41a3f5c0a"

  use_cli = true
}
