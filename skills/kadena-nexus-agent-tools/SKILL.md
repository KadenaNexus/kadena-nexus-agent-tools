---
name: kadena-nexus-agent-tools
description: Check an address before paying it, find the cheapest chain for a transfer, watch for hacks, and record proof of a delivered file. Paid per call over x402.
---

# Kadena Nexus tools for agents

Each tool is one GET that answers JSON, paid per call over x402 version 2 in USDC on Base or Polygon, or KDA on Kadena. No account, no API key.
Ask once without payment to read the price (HTTP 402), then ask again with the payment attached.

## Which tool, when

| Moment | Call | Price |
|---|---|---|
| About to send money to an address you have not paid before | `https://agentpay.kadena.ws/v1/preflight?address=ADDRESS&network=NETWORK` | $0.025 |
| Only need to know if the address is linked to a hack, scam or stolen funds | `https://agentpay.kadena.ws/v1/address-check?address=ADDRESS` | $0.02 |
| Only need to know if Tether or Circle froze the address | `https://agentpay.kadena.ws/v1/freeze-check?address=ADDRESS` | $0.01 |
| Choosing which chain to send on | `https://agentpay.kadena.ws/v1/fees` (all 13) or `https://agentpay.kadena.ws/v1/fees/CHAIN` | $0.01 / $0.002 |
| Checking on a schedule for new hacks and the addresses named | `https://agentpay.kadena.ws/v1/incidents` | $0.03 |
| Checking on a schedule for unusual exchange or bridge outflows | `https://agentpay.kadena.ws/v1/early-warnings` | $0.05 |
| Delivering a file the recipient may want to check later | `https://agentpay.kadena.ws/v1/proof/COMMITMENT` | $0.005 |

Preflight already runs the address check, the freeze check and the fee lookup: do not call those separately as well.

## Acting on Preflight

- `stop`: do not pay. Tell the person why, with the cases given.
- `caution`: ask the person before paying. Caution also means a check could not be read (see `unreadChecks`).
- `nothing found`: no known problem. This is not proof that the address is safe; say so if you report it.

## Spending

- Read the price from the 402 answer and refuse to pay more than the price listed here.
- Pay only the payee named in the 402 answer, on a network you were given money for.
- One paid call per question. Free samples show the answer's shape without paying: `https://agentpay.kadena.ws/v1/sample/TOOL`.

## Receipt Proof

1. Make 32 random bytes as a salt. commitment = SHA-256(salt bytes followed by the 32 bytes of SHA-256 of the file), 64 lowercase hex.
2. Save the salt, the file's SHA-256 and the commitment before paying.
3. Pay `https://agentpay.kadena.ws/v1/proof/COMMITMENT`. Then read `https://agentpay.kadena.ws/v1/proof/status/COMMITMENT` (free) until it says confirmed.
4. Give the recipient the file and the receipt. Anyone can check them at https://kadena.ws/proof/.
A match shows the file was recorded in that block. It does not show who wrote it or that it is correct.

## More

- Catalog: https://agentpay.kadena.ws/v1
- Guide with every answer in full: https://agentpay.kadena.ws/llms-full.txt
- OpenAPI: https://agentpay.kadena.ws/openapi.json
- People: https://kadena.ws/agents/
