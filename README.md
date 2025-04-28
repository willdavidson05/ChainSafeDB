![ChainSafeDB](https://github.com/user-attachments/assets/57637be5-7adb-4baa-965b-10f9c4967e40)

**Track, audit, and protect sensitive database records — backed by blockchain.**

ChainSafeDB is an open-source CLI tool that detects tampering and tracks access to sensitive database records by logging cryptographic fingerprints locally and optionally onto a blockchain network.

---

## Features

- Scan and hash important database records
- Log access events (view, edit, delete)
- Optional blockchain logging (Polygon Mumbai testnet)
- Tamper-evident history without exposing actual data
- Lightweight and easy-to-use CLI interface

---

## How It Works

##### GOING TO ADD DIAGRAM HERE

- Records are scanned from a traditional database
- Each record is hashed using SHA-256
- Hashes are logged locally and/or committed to a blockchain smart contract
- Later verification detects any tampering by comparing hashes

---

## Example Use Case

A financial auditing team needs to track who accesses or modifies sensitive transaction records.  
ChainSafeDB allows them to:
- Hash critical records
- Store fingerprints securely
- Detect and prove if any unauthorized changes occur

---

## Quick Start

### Local Mode (No Blockchain)

```bash
python3 -m chainsafedb.cli scan --db examples/sample.db
```

### Simulated Blockchain Logging

```bash
python3 -m chainsafedb.cli scan --db examples/sample.db --enable-chain
```

### Real Blockchain Logging (Optional)

First deploy `LogHash.sol` to Polygon Mumbai using Remix.

Then run:

```bash
python3 -m chainsafedb.cli scan \
  --db examples/sample.db \
  --enable-chain \
  --rpc-url "https://polygon-mumbai.infura.io/v3/YOUR_INFURA_ID" \
  --private-key "YOUR_PRIVATE_KEY" \
  --contract "0xYourDeployedContract" \
  --abi contracts/LogHash.abi.json
```

---

## Team

- Parker Taranto
-  Will Davidson


