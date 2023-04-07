from beaker import client, sandbox

from app import app

app.build().export("./artifacts")

accounts = sandbox.kmd.get_accounts()
sender = accounts[0]

app_client = client.ApplicationClient(
    client=sandbox.get_algod_client(),
    app=app,
    sender=sender.address,
    signer=sender.signer,
)

app_client.create()

return_value = app_client.call("logger", a="Hey, ", b="Hello All ...!").return_value
print(return_value)
