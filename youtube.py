from typing import List
import pdb
import cabinet_sdk as c

# test cabinet_sdk library is installed and working  
c.welcome('Youtube Sorter')

## PROCESS DATA INTO FORMAT THAT CAN BE UPLOADED TO CABINET 
# note: this is specific to this data set (youtube thumbnails) 

# turn csv metadata into List[dicts] 
def create_metadata_list() -> list:
    with open('mini_metadata.csv',newline='') as csvfile:
        count = 0
        metadata = [] 
        while True:
            entry_line= csvfile.readline()
            if not entry_line:
                break
            entry_list= entry_line.strip().split(',')
            # if title split because it contianed commas, recreate single title
            if len(entry_list) > 4:
                title_split = entry_list[3:]
                title = ', '.join(title_split) 
                entry_list[3] = title 
            entry_metadata = {'blob_type':'youtube','photo_id': entry_list[0], 'channel':entry_list[1],'category':entry_list[2],'title':entry_list[3]}
            metadata.append(entry_metadata)
    return metadata[1:]

metadatas = create_metadata_list()

# use metadata info to generate list of file_paths to corresponding thumbnail
def create_paths_list(md) -> list:
    paths = []
    for i in md:
        channel = i['channel']
        id = i['photo_id']
        path = 'images/'+f'{channel}/'+f'{id}.jpg'
        paths.append(path)
    return paths
    
paths = create_paths_list(metadatas) 

# Create a list of tuples with t[0]=metadata:dict, t[1]=img_file_path:str
def create_upload_tuples(metadatas:list, paths:list) -> list: 
    upload_tups = []
    for i in range(len(paths)):
        upload_tups.append((metadatas[i],paths[i]))
    return upload_tups

blob_info:tuple = create_upload_tuples(metadatas,paths)

#UPLOAD BLOBS
# iterate through list of tuples and add each blob+metadata to Cabinet 
def upload_bulk_data(blob_info:List[tuple]):
    for tup in blob_info:
        try:  
            print(c.upload(tup[0], tup[1]))
        except Exception as e: 
            print(e.args[0])
            continue

# upload_bulk_data(blob_info) 

#BLOB_TYPES
print(c.blob_types())

#FIELDS 
print(c.fields('youtube'))

# SEARCH
matching_entries = c.search('youtube',{'category':'Science'})
for key in matching_entries:
    pass
    # print(key, matching_entries[key])

# UPDATE

# RETRIEVE - not working think its cus sdk version is old 
resp_bytes = c.retrieve('fruit', '108')
print(resp_bytes[:20])
