import argparse
from chainsafedb.db_scanner import get_records
from chainsafedb.hasher import hash_record

def scan_database(db_path, table_name="sensitive_table"):
    try:
        records = get_records(db_path, table_name)
        print(f"\nScanning {table_name} from {db_path}...\n")
        for record in records:
            stringified = str(record)
            record_hash = hash_record(stringified)
            print(f"Record: {stringified}")
            print(f"Hash:   {record_hash}\n")
    except Exception as e:
        print(f"❌ Error scanning database: {e}")

def main():
    parser = argparse.ArgumentParser(description="ChainSafeDB CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Scan command
    scan_parser = subparsers.add_parser("scan", help="Scan a database for sensitive records and hash them")
    scan_parser.add_argument("--db", required=True, help="Path to the SQLite database")
    scan_parser.add_argument("--table", default="sensitive_table", help="Name of the table to scan")

    args = parser.parse_args()

    if args.command == "scan":
        scan_database(args.db, args.table)

if __name__ == "__main__":
    main()
