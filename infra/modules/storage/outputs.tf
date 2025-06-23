output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}

output "archive_container_name" {
  value = azurerm_storage_container.archive.name
}
