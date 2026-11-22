# AGENTS.md: pre-payment checks with Kadena Nexus

Instructions for a coding agent adding crypto payment safety to this project.

## When code sends money to an address

Before any transfer to an address the app has not paid before, call Preflight and act on the verdict:

```
GET https://agentpay.kadena.ws/v1/preflight?address={address}&network={network}
```

- `stop`: block the transfer and show the `summary` to the user.
- `caution`: ask the user to confirm. Caution also covers a check that could not be read (`unreadChecks`).
- `nothing found`: continue. Do not describe the address as safe.

Do not also call the address check or the freeze check: Preflight runs both.

## Paying for the call

The call is paid per request over x402 (HTTP 402). Use an x402 client so payment happens inside the request:

- Python: `pip install "x402[evm]" requests`, see `examples/preflight.py`.
- Node.js: `npm install @x402/fetch @x402/evm viem`, see `examples/preflight.mjs`.

Rules:
- Read the price from the 402 answer and refuse anything above $0.03 for Preflight.
- Pay only the `payTo` given in the 402 answer, on `eip155:8453` (Base) or `eip155:137` (Polygon).
- Keep the wallet key in an environment variable, never in code.
- Handle a failed or refused payment as `caution`, not as `nothing found`.

## Other tools

See `skills/kadena-nexus-agent-tools/SKILL.md` for fees, hack alerts, early warnings and Receipt Proof.
