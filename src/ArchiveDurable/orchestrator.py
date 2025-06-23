def orchestrator():
    old_records = call_activity("ListOldRecords")
    blob_paths = call_activity("ExportToBlob", old_records)
    call_activity("DeleteFromCosmos", old_records)
    return blob_paths
