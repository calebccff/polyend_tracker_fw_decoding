#!/usr/bin/python3

import argparse

flash_start = 0x20000fc

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input file", required=True)
parser.add_argument("-o", "--output", help="Output file", required=True)
parser.add_argument("-s", "--start", help="Start address", required=False)

args = parser.parse_args()

f = open(args.input, "r").readlines()
converted = bytearray()

for i in range(0, len(f)):
        line = f[i][1:-1] # strip ":" and \n
        if len(line) == 14:
                print(f"Header line : {i}: {line}")
                continue
        elif len(line) == 26:
                print(f"Other line  : {i}: {line}")
                continue
        elif len(line) != 42:
                print(f"Unknown line: {i}: {line}")
                continue
        c = bytearray.fromhex(line[:-2])
        crc = int(line[-2:], 16)
        calc_crc = (-sum(c) % 0x100) & 0xff
        if crc != calc_crc:
                print(f"CRC error at line {i}, {crc} != {calc_crc} : {line}")
        data = c[4:]
        converted += data

out = open(args.output, "wb")
##padding = bytearray([0xff] * flash_start)
#out.write(padding)
out.write(converted)
