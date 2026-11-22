# Ask Preflight before paying an address. Pays per call in USDC on Base over x402.
# pip install "x402[evm]" requests
import os
import requests
from eth_account import Account
from x402 import x402ClientSync
from x402.http.clients import wrapRequestsWithPayment
from x402.mechanisms.evm.exact import ExactEvmClientScheme
from x402.mechanisms.evm.signers import EthAccountSigner

account = Account.from_key(os.environ["AGENT_KEY"])  # a wallet holding a little USDC on Base
client = x402ClientSync()
client.register("eip155:8453", ExactEvmClientScheme(signer=EthAccountSigner(account)))
session = wrapRequestsWithPayment(requests.Session(), client)

address = "0x098B716B8Aaf21512996dC57EB0615e2383E2f96"
r = session.get(f"https://agentpay.kadena.ws/v1/preflight?address={address}&network=base")
if r.status_code != 200:                             # not paid: treat as caution, never as nothing found
    raise SystemExit(f"Preflight was not answered ({r.status_code}); ask before paying.")
answer = r.json()
print(answer["verdict"], "-", answer.get("summary"))
if answer["verdict"] == "stop":
    raise SystemExit("Do not pay this address.")
