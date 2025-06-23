output "cosmos_account_endpoint" {
  value = azurerm_cosmosdb_account.this.endpoint
}

output "cosmos_account_key" {
  value     = azurerm_cosmosdb_account.this.primary_master_key
  sensitive = true
}
