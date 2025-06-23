variable "resource_group_name" {
  type        = string
  description = "The name of the resource group"
}

variable "location" {
  type        = string
  description = "Azure region for Cosmos DB"
}

variable "cosmos_account_name" {
  type        = string
  description = "The name of the Cosmos DB account"
}

variable "database_name" {
  type        = string
  description = "The name of the Cosmos database"
}

variable "container_name" {
  type        = string
  description = "The name of the Cosmos DB container"
}
