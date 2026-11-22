// Ask Preflight before paying an address. Pays per call in USDC on Base over x402.
// npm install @x402/fetch @x402/evm viem
import { wrapFetchWithPaymentFromConfig } from "@x402/fetch";
import { ExactEvmScheme } from "@x402/evm/exact/client";
import { privateKeyToAccount } from "viem/accounts";

const account = privateKeyToAccount(process.env.AGENT_KEY); // a wallet holding a little USDC on Base
const fetchWithPay = wrapFetchWithPaymentFromConfig(fetch, {
  schemes: [{ network: "eip155:8453", client: new ExactEvmScheme(account) }],
});

const address = "0x098B716B8Aaf21512996dC57EB0615e2383E2f96";
const res = await fetchWithPay(`https://agentpay.kadena.ws/v1/preflight?address=${address}&network=base`);
if (res.status !== 200) {                          // not paid: treat as caution, never as nothing found
  console.error(`Preflight was not answered (${res.status}); ask before paying.`);
  process.exit(2);
}
const answer = await res.json();
console.log(answer.verdict, "-", answer.summary);
if (answer.verdict === "stop") process.exit(1); // do not pay this address
