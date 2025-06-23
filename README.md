# billing-records

Cost Optimization Challenge: Managing Billing Records in Azure Serverless Architecture
We have a serverless architecture in Azure, where one of our services stores billing records in Azure Cosmos DB. The system is read-heavy, but records older than three months are rarely accessed.

Over the past few years, the database size has significantly grown, leading to increased costs. We need an efficient way to reduce costs while maintaining data availability.

Current System Constraints
Record Size: Each billing record can be as large as 300 KB.

Total Records: The database currently holds over 2 million records.

Access Latency: When an old record is requested, it should still be served, with a response time in the order of seconds.

Solution Requirements
Please propose a detailed solution to optimize costs while ensuring the following
Simplicity & Ease of Implementation – The solution should be straightforward to deploy and maintain.

No Data Loss & No Downtime – The transition should be seamless, without losing any records or requiring2 service downtime.

No Changes to API Contracts – The existing read/write APIs for billing records must remain unchanged

Solution:
Cosmos db is expensive and while the file size increases, the cost also increases. Since files older than three months are rarely used, those files could be saved in azure blob storage under cool tier. Eventhough slower than cosmos db it saves the cost by 80%.

Also it is mentioned not to change the API contracts, so we can build a data access layer that hides the difference between cosmos db and azure blob storage.

In this repo I have added certain pseudo codes to help understand the logic. 
