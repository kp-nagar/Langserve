from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:4002/ask/")
response = remote_chain.invoke({"item": "computer"})
print(response)