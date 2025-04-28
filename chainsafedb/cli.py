import argparse
from chainsafedb.db_scanner import get_records
from chainsafedb.hasher import hash_record
from chainsafedb.audit_log import AuditLogger
from chainsafedb.blockchain_logger import BlockchainLogger


def scan_database(db_path, table_name="sensitive_table", blockchain_logger=None):
    try:
        records = get_records(db_path, table_name)
        print(f"\nScanning {table_name} from {db_path}...\n")
        audit_logger = AuditLogger(blockchain_logger=blockchain_logger)

        for record in records:
            stringified = str(record)
            record_hash = hash_record(stringified)
            print(f"Record: {stringified}")
            print(f"Hash:   {record_hash}\n")

            # Log view action
            audit_logger.record_event(action_type="view", user="admin", record_id=record[0], record_data=record)
    except Exception as e:
        print(f" Error scanning database: {e}")

def main():
    parser = argparse.ArgumentParser(description="ChainSafeDB CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Scan command
    scan_parser = subparsers.add_parser("scan", help="Scan a database for sensitive records and hash them")
    scan_parser.add_argument("--db", required=True, help="Path to the SQLite database")
    scan_parser.add_argument("--table", default="sensitive_table", help="Name of the table to scan")

    #  Blockchain options
    scan_parser.add_argument("--enable-chain", action="store_true", help="Enable blockchain logging")
    scan_parser.add_argument("--rpc-url", type=str, default=None, help="RPC URL for blockchain network")
    scan_parser.add_argument("--private-key", type=str, default=None, help="Private key for signing blockchain transactions")
    scan_parser.add_argument("--contract", type=str, default=None, help="Deployed contract address")
    scan_parser.add_argument("--abi", type=str, default=None, help="Path to the contract ABI JSON file")

    args = parser.parse_args()

    blockchain_logger = None

    if args.command == "scan":
        if args.enable_chain:
            if not all([args.rpc_url, args.private_key, args.contract, args.abi]):
                print(" Missing blockchain parameters. Please provide --rpc-url, --private-key, --contract, and --abi.")
                return

            blockchain_logger = BlockchainLogger(
                rpc_url=args.rpc_url,
                private_key=args.private_key,
                contract_address=args.contract,
                abi_path=args.abi
            )

        scan_database(args.db, args.table, blockchain_logger)

if __name__ == "__main__":
    main()

