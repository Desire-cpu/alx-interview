#!/usr/bin/python3
"""
Read stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>, skip line if not this format
After every 10 minutes or keyboard interrupt (CTRL + C),
print these from the beginning: number of lines by status code
Possible status codes: 200, 301, 400, 401, 404, 405, and 500
If status code isn't an integer, do not print it
Format: <status code>: <number>
Status code must be printed in ascending order
"""
import sys


def print_metrics(status_code_counts, total_file_size):
    print("Total file size: {}".format(total_file_size))
    for key, val in sorted(status_code_counts.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
current_status_code = 0
line_count = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_count += 1

            if line_count <= 10:
                total_file_size += int(parsed_line[0])
                current_status_code = parsed_line[1]

                if (current_status_code in status_code_counts.keys()):
                    status_code_counts[current_status_code] += 1

            if (line_count == 10):
                print_metrics(status_code_counts, total_file_size)
                line_count = 0

finally:
    print_metrics(status_code_counts, total_file_size)
