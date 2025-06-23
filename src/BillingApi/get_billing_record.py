def get_billing_record(id):
    record = cosmos.get(id)
    if record:
        return record
    else:
        blob_path = index.lookup(id)  # or compute blob from ID
        blob_data = blob.read(blob_path)
        decompressed = json.loads(gzip.decompress(blob_data))
        for r in decompressed:
            if r['id'] == id:
                return r
        return 404
