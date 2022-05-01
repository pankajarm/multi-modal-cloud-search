from clip_client import Client

c = Client('grpc://0.0.0.0:51000')
c.profile()

# text test
r = c.encode(['First do it', 'then do it right', 'then do it better'])
print(r.shape)  # [3, 512] 

# image test
r = c.encode(['https://clip-as-service.jina.ai/_static/favicon.png'])  # remote image
print(r.shape)  # [3, 512]