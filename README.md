![ChainSafeDB](https://github.com/user-attachments/assets/57637be5-7adb-4baa-965b-10f9c4967e40)

**Track, audit, and protect sensitive database records — backed by blockchain.**

ChainSafeDB is an open-source CLI tool that detects tampering and tracks access to sensitive database records by logging cryptographic fingerprints locally and optionally onto a blockchain network (Ethereum Sepolia testnet).

---

## Project Interaction Summary

- The **ChainSafeDB CLI** acts as the main controller that starts the scanning and logging process based on user commands.

- The **DB Scanner** (`db_scanner.py`) connects to a specified SQLite database and fetches records from the target table.

- Each **record** is passed to the **Hasher** (`hasher.py`), which generates a secure SHA-256 hash fingerprint of the record's contents.

- For every record scanned, an **Audit Event** is created using the **Audit Logger** (`audit_log.py`), recording metadata like timestamp, user action ("view"), and the generated fingerprint.

- If blockchain logging is enabled:
  - The **Blockchain Logger** (`blockchain_logger.py`) takes the fingerprint and:
    - Builds a transaction to the deployed **LogHash smart contract** (`LogHash.sol`) on the **Ethereum Sepolia testnet**.
    - Signs and broadcasts the transaction using the user's **Infura endpoint** and **private key**.
    - The smart contract emits an immutable event containing the fingerprint hash.

- The **smart contract** acts as a permanent, tamper-proof registry of database record fingerprints, ensuring that any unauthorized modification of the database can later be detected by hash mismatch.

---

## Summary of Components

| Element | Role |
|:--------|:-----|
| CLI | User entry point |
| DB Scanner | Pulls records from database |
| Hasher | Creates tamper-evident SHA-256 hashes |
| Audit Logger | Records local access events |
| Blockchain Logger | Sends fingerprints to smart contract if enabled |
| Smart Contract | Stores hashes permanently on Sepolia blockchain |

## System Architecture

Database (SQLite)
       │
       ▼
[DB Scanner (db_scanner.py)]
       │
       ▼
[Hasher (hasher.py)]
       │
       ▼
[Audit Logger (audit_log.py)]
       │
       ├── (Locally saves access event)
       │
       └── (If blockchain enabled)
             │
             ▼
    [Blockchain Logger (blockchain_logger.py)]
             │
             ▼
    [Ethereum Sepolia Smart Contract (LogHash.sol)]


---

## Features

- Scan and hash important database records
- Log access events (view, edit, delete)
- Blockchain logging (Ethereum Sepolia testnet) (optional)
- Tamper-evident history without exposing actual data
- Lightweight and easy-to-use CLI interface

---

## Example Use Case

A financial auditing team needs to track who accesses or modifies sensitive transaction records.  
ChainSafeDB allows them to:
- Hash critical records
- Store fingerprints securely
- Log blockchain proofs of access
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

First, deploy LogHash.sol using Hardhat or Remix to Sepolia.

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

## Project Details

- **Smart Contract (Deployed on Sepolia Testnet):**  
  [View Contract on Etherscan](https://sepolia.etherscan.io/address/0xEd81578d72276fdA029306675d1026ec94e03209)

- **Infura Project ID:**  
  `c19848ad6a3e4c95a4434d585770847d`
  
---

## Development Process

- **Database Integration**  
  Functions were built to connect to and scan SQLite databases, pulling records from a sensitive table.

- **Cryptographic Hashing**  
  Each record is hashed using the SHA-256 algorithm to generate tamper-evident fingerprints.

- **Audit Logging**  
  An `AuditLogger` component records structured access events such as "view" actions.

- **Blockchain Smart Contract**  
  We developed a lightweight Solidity smart contract (`LogHash.sol`) to store fingerprints on the Ethereum Sepolia testnet.

- **Blockchain Interaction**  
  Using Web3.py, the CLI interacts with the smart contract, sending hashes during scans.

- **CLI Development**  
  Built a command-line interface using `argparse`, allowing both local and blockchain logging.

- **Hardhat Deployment**  
  The smart contract was deployed to Sepolia using Hardhat and Infura RPC endpoints.

- **Testing and Error Handling**  
  Extensive testing was done to handle blockchain-specific errors like "replacement transaction underpriced."

---


## Team

- Parker Taranto
-  Will Davidson


