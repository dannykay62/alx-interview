#!/usr/bin/python3
"""reads stdin line by line and computes metrics:
    Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size> (see input
    format above)
    Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    if a status code doesn’t appear or is not an integer, don’t print
    anything for this status code
    format: <status code>: <number>
    status codes should be printed in ascending order
"""
import sys


# status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
#                       "402": 0, "403": 0, "404": 0, "405": 0, "500": 0}
if __name__ == "__main__":
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "402": 0, "403": 0,
                  "404": 0, "405": 0, "500": 0}

    total_count = 1
    file_size = 0

    def parse_func(line):
        """read line, parse and grab the data"""
        try:
            line_parsed = line.split()
            status_code = line_parsed[-2]
            if status_code in stat_codes.keys():
                stat_codes[status_code] += 1
            return int(line_parsed[-1])
        except Exception:
            return 0

    def print_stat():
        """Print in order"""
        print("File size: {}".format(file_size))
        for key in sorted(stat_codes.keys()):
            if stat_codes[key]:
                print("{}: {}".format(key, stat_codes[key]))

    try:
        for line in sys.stdin:
            file_size += parse_func(line)
            if total_count % 10 == 0:
                print_stat()
            total_count += 1
    except KeyboardInterrupt:
        print_stat()
        raise
    print_stat()
