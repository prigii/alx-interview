#!/usr/bin/python3
""" Log parsing """

import sys


def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None


def print_statistics(total_file_size, lines_by_status):
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(lines_by_status):
        print(f"{status_code}: {lines_by_status[status_code]}")


def main():
    total_file_size = 0
    lines_by_status = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip_address, status_code, file_size = parse_line(line.strip())

            if ip_address is None:
                continue

            total_file_size += file_size
            lines_by_status[status_code] = lines_by_status.get(status_code, 0)
            + 1

            if i % 10 == 0:
                print_statistics(total_file_size, lines_by_status)

    except KeyboardInterrupt:
        pass  # Handle KeyboardInterrupt (Ctrl+C)

    finally:
        print_statistics(total_file_size, lines_by_status)


if __name__ == "__main__":
    main()
