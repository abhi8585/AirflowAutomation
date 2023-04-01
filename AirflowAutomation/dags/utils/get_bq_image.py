from google.cloud import storage
# from twitterImageWithTextUpdate import TwitterImagewithTextUpdate


class Image:

    def __init__(self):
        pass

    def download_image_file(self,image_file_name, project_name):
        # Initialize a client object
        client = storage.Client(project=project_name)

        # Set the bucket name and image file name
        bucket_name = "twitter_coding_tutorial"
        # image_file_name = "twitter_python_keywords/BoolDataTypeKeyword_ManimCE_v0.17.2.png"

        # Get a reference to the bucket and image file
        bucket = client.bucket(bucket_name)
        image_blob = bucket.blob(image_file_name)

        # Download the image file and save it locally as a .png file
        image_data = image_blob.download_as_bytes()
        image_name = image_file_name.split("/")[1]
        with open(image_name, "wb") as f:
            f.write(image_data)
        return True

# image_file_name = "twitter_coding_tutorial/twitter_python_keywords/BoolDataTypeKeyword_ManimCE_v0.17.2.png"
# download_image_file()

# get file names

    def get_file_names(self,folder_path,project_name):
        from google.cloud import storage
        # Initialize a client object
        client = storage.Client(project=project_name)

        # Set the bucket name and folder path
        bucket_name = "twitter_coding_tutorial"
        # Get a reference to the bucket and the folder
        bucket = client.bucket(bucket_name)
        folder = bucket.blob(folder_path)

        # Get the names of all the image files in the folder
        image_names = []
        for blob in bucket.list_blobs(prefix=folder_path):
            if blob.name.endswith(".jpg") or blob.name.endswith(".png") or blob.name.endswith(".jpeg"):
                image_names.append(blob.name)
        return image_names
# Print the list of image names

# main function to download all files from a folder
    # def download_files(self, file_path):
    #     for file in file_path:
    #         self.download_image_file(file)
        # ins = TwitterImagewithTextUpdate()
        # image_name = file.split("/")[1]
        # ins.updateImageWithText(image_name)

# folder_path = "twitter_python_keywords"
# image_names = get_file_names(folder_path)
# download_files(image_names)
