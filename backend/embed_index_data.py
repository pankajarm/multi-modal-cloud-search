from docarray import DocumentArray
from clip_client import Client

# get data
da = DocumentArray.pull('ttl-original', show_progress=True, local_cache=True)

# get client
c = Client(server='grpc://0.0.0.0:51000')
da = c.encode(da, show_progress=True)
da.save_binary("../data_da.bin", compress='lz4')