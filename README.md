# Cabinet Sandbox - Youtube thumbnails Example
### Description
Cabinet sandbox exists to provide an example of the Cabinet system at work. In this example (youtube.py), a dataset of thumbnail images and their assoicated metadata are uploaded to Cabinet. The other functions in the cabinet_sdk library are then demonstrated using the uploaded data

### The Data
A file system containing youtube video thumnbnails and a csv with associated metadata.

Link to dataset: https://www.kaggle.com/datasets/praneshmukhopadhyay/youtube-thumbnail-dataset 

## Setup
1. Create 'youtube' table in Cabinet database
    * this must be done from the cabinet_api repository
    * Navigate to cabinet_api/src/db_setup.py and add the following to the custom_blob_types dictionary: KEY = 'youtube', VALUE = {'photo_id':'VARCHAR', 'channel':'VARCHAR', 'category':'VARCHAR', 'title':'VARCHAR'}
    * Edit initialize fn as needed to have youtube table created in desired environment(s)
    * Navigate to cabinet_api/src/classes.py 
    * Define the Youtube Class and add it to Blob_type and blob_classes
2. Install cabinet_sdk from https://test.pypi.org/project/cabinet-sdk/
    * Before installing cabinet_sdk `pip install pyyaml` - pyyaml is used by cabinet_sdk but for some reason causes an error when installed as a dependent of cabinet_sdk so must be installed seperately first. 
3. Download the dataset and unzip the contents
    * make sure the metadata is in a file called metadata.csv and images are in a folder caled images
5. Make sure the cabinet_api is running and that ENV is set to the desired environment before attempting to run youtube.py
6. Run youtube_example.ipybn 