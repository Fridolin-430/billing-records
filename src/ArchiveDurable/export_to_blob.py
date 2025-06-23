def export_to_blob(records):
    for batch in split(records, 100):
        compressed = gzip(json.dumps(batch))
        blob_path = f"billing/archived/{batch_start_date}.json.gz"
        blob.upload(blob_path, compressed)
        index.save(record_ids, blob_path)  # optional
    return blob_paths
