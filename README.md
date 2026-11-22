# Kadena Nexus tools for AI agents

Give an AI agent a check before it pays an address, the cheapest chain for a transfer, hack alerts, and proof of a delivered file. Each tool is one web address that answers JSON and is paid per call over the open [x402](https://www.x402.org) standard, in USDC on Base or Polygon, or in KDA on Kadena. No account, no API key.

| Tool | Address | Price |
|---|---|---|
| Preflight: one verdict before a payment | `https://agentpay.kadena.ws/v1/preflight?address={address}&network={network}` | $0.025 |
| Wallet risk check | `https://agentpay.kadena.ws/v1/address-check?address={address}` | $0.02 |
| USDT and USDC freeze check | `https://agentpay.kadena.ws/v1/freeze-check?address={address}` | $0.01 |
| Hack and exploit alerts | `https://agentpay.kadena.ws/v1/incidents` | $0.03 |
| Early warnings | `https://agentpay.kadena.ws/v1/early-warnings` | $0.05 |
| Gas fees on 13 chains | `https://agentpay.kadena.ws/v1/fees` | $0.01 |
| Gas fee on one chain | `https://agentpay.kadena.ws/v1/fees/{chain}` | $0.002 |
| Receipt Proof | `https://agentpay.kadena.ws/v1/proof/{commitment}` | 0.005 KDA (KDA only for now) |

Prices are read live from the [catalog](https://agentpay.kadena.ws/v1). Every tool has a free sample that shows the shape of its answer: `https://agentpay.kadena.ws/v1/sample/{tool}`.

## Use it

- **Any agent that reads a skill file:** copy [`skills/kadena-nexus-agent-tools/SKILL.md`](skills/kadena-nexus-agent-tools/SKILL.md) into your agent's skills folder. It says which tool to call when, how to act on the answer and what to spend.
- **Coding agents:** [`AGENTS.md`](AGENTS.md) tells an agent working in your repository how to add a pre-payment check.
- **From code:** [`examples/preflight.py`](examples/preflight.py) and [`examples/preflight.mjs`](examples/preflight.mjs) use Coinbase's x402 libraries; the payment happens inside the request.
- **Machine-readable:** [llms.txt](https://agentpay.kadena.ws/llms.txt), [llms-full.txt](https://agentpay.kadena.ws/llms-full.txt), [OpenAPI](https://agentpay.kadena.ws/openapi.json).

## What the answers claim

- Preflight gives `stop`, `caution` or `nothing found`, from the wallet risk check and the freeze check. The fee is cost information and never changes the verdict.
- `nothing found` means nothing is on record. It is not proof that an address is safe.
- An early warning is a reason to look closer, not proof of a theft.
- A Receipt Proof match shows that a file matches a commitment recorded on Kadena in a given block. It does not show who wrote the file or that its content is correct.

Risk and incident data come from [KadenaTrace](https://trace.kadena.ws). More at [kadena.ws/agents](https://kadena.ws/agents/). Contact: Saudi.KDA@kadena.ws · [@KadenaNexus](https://x.com/KadenaNexus) · [t.me/KadenaNexus](https://t.me/KadenaNexus)
