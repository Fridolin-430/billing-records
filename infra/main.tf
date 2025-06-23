provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "billing-archiver-rg"
  location = "East US"
}

module "cosmosdb" {
  source = "./modules/cosmos"
}

module "storage" {
  source = "./modules/storage"
}

module "function_apps" {
  source = "./modules/functions"
}
