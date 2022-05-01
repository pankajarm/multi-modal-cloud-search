from docarray import DocumentArray, Document
from clip_client import Client

# get type of input data
print("This verison currently supports input data type image (local path) or text from url")
input_data_type = input("Enter type of input data (image/text): ")

# now based upon user data type decide which documentarray to create
if input_data_type == "image":
    # get data path from user
    image_data_path = input("Enter local directory path for your image data: ")
    data_da = DocumentArray.from_files([image_data_path+'/*.png', image_data_path+'/*.jpg', image_data_path+'/*.jpeg'])

elif input_data_type == "text":
    # https://www.gutenberg.org/files/1342/1342-0.txt
    text_url = input("Enter raw text url: ")
    d = Document(uri=text_url).load_uri_to_text()
    data_da = DocumentArray(Document(text=s.strip()) for s in d.text.replace('\r\n', '').split('.') if s.strip())
# data_da = DocumentArray.pull('ttl-original', show_progress=True, local_cache=True)

# get client
c = Client(server='grpc://0.0.0.0:51000')
data_da = c.encode(data_da, show_progress=True)
data_da.save_binary("../data_da.bin", compress='lz4')