# 🔐 ChainSafeDB

ChainSafeDB is a lightweight, open-source CLI tool for tracking the integrity of sensitive data in traditional databases.  
Instead of storing actual data on a blockchain, we hash selected records and optionally log those hashes to a testnet like Polygon for tamper-evident verification.

The tool will also (optionally) track **access events** (view, edit, delete) to sensitive data — creating a permanent audit trail for better visibility and accountability.

---

## 💡 Example Use Case

> A developer wants to track if someone has secretly changed or accessed key financial records in a PostgreSQL database.  
ChainSafeDB will hash those records and log their fingerprints to a testnet. If the hashes ever change, you know something was altered.

---

## 📅 Project Timeline

| Week | Goal |
|------|------|
| 1    | Project setup(✅) |
| 1    | CLI scaffold, hashing logic, Connect database scanning + hashing |
| 2    | Add blockchain testnet logging, Implement access log tracking |
| 3    | Testing, polish, documentation |
| 4    | Final demo + GitHub release |

