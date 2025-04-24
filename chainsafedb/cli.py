import argparse
from chainsafedb.db_scanner import get_records
from chainsafedb.hasher import hash_record
from chainsafedb.audit_log import AuditLogger
from chainsafedb.blockchain_logger import BlockchainLogger

class MockBlockchainLogger:
    def log_hash(self, data_hash):
        print(f"🧪 (Simulated) Logged hash to blockchain: {data_hash}")

def scan_database(db_path, table_name, enable_chain, rpc_url, private_key, contract, abi):
    try:
        records = get_records(db_path, table_name)

        # Use real blockchain logger if all chain flags provided, else use mock
        if enable_chain and all([rpc_url, private_key, contract, abi]):
            blockchain_logger = BlockchainLogger(
                rpc_url=rpc_url,
                private_key=private_key,
                contract_address=contract,
                abi_path=abi
            )
            print("✅ Blockchain logging enabled.")
        else:
            blockchain_logger = MockBlockchainLogger()
            print("ℹ️ Blockchain logging disabled or incomplete config — using mock logger.")

        audit_logger = AuditLogger(blockchain_logger=blockchain_logger)

        print(f"\nScanning {table_name} from {db_path}...\n")
        for record in records:
            stringified = str(record)
            record_hash = hash_record(stringified)
            print(f"Record: {stringified}")
            print(f"Hash:   {record_hash}\n")

            audit_logger.record_event(
                action_type="view",
                user="admin",
                record_id=record[0],
                record_data=record
            )

    except Exception as e:
        print(f"❌ Error scanning database: {e}")

def main():
    parser = argparse.ArgumentParser(description="ChainSafeDB CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan a database and log access events")
    scan_parser.add_argument("--db", required=True, help="Path to the SQLite database")
    scan_parser.add_argument("--table", default="sensitive_table", help="Table to scan")

    # Optional blockchain logging
    scan_parser.add_argument("--enable-chain", action="store_true", help="Enable blockchain logging")
    scan_parser.add_argument("--rpc-url", help="Blockchain RPC URL")
    scan_parser.add_argument("--private-key", help="Private key for signing")
    scan_parser.add_argument("--contract", help="Smart contract address")
    scan_parser.add_argument("--abi", help="Path to ABI JSON file")

    args = parser.parse_args()

    if args.command == "scan":
        if args.enable_chain:
            has_all_chain_args = all([
            args.rpc_url,
            args.private_key,
            args.contract,
            args.abi
        ])
        else:
            has_all_chain_args = False


        scan_database(
            db_path=args.db,
            table_name=args.table,
            enable_chain=args.enable_chain,
            rpc_url=args.rpc_url if has_all_chain_args else None,
            private_key=args.private_key if has_all_chain_args else None,
            contract=args.contract if has_all_chain_args else None,
            abi=args.abi if has_all_chain_args else None
        )


if __name__ == "__main__":
    main()
