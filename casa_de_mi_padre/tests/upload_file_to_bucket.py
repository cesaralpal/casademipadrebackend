from google.cloud import storage

def upload_file_to_bucket(file, project_id, bucket_name):
    # Create a storage client with explicit project ID
    storage_client = storage.Client(project=project_id)

    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Upload the file
    blob = bucket.blob(file.filename)
    blob.upload_from_string(file.read(), content_type=file.content_type)

    # Get the URL of the uploaded file
    file_url = blob.public_url

    return file_url
