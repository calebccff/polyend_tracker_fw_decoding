# Polyend tracker FW decoding

## Hardware specs

The tracker uses a MK66FX1M0VLQ18 180 MHz ARM Cortex-M4F Microcontroller [Technical datasheet](https://www.nxp.com/docs/en/data-sheet/K66P144M180SF5V2.pdf).

The MK66FX1M0VLQ18 has 1.25MB of internal flash.

## File format

Tracker firmware file format.

Several types of command?, predominantly "data" lines and "address" lines.

### Data command

22 characters

```
    :               Colon
0:  10              Constant (command type?)
1:  XXXX            Offset to patch
3:  00              Constant (reserved??)
4:  <32 digits>     16 data bytes
20: XX              Checksum8 2s complement of the whole line
```

There are usually 4096 (0x1000) data lines before each header line.

```
                1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16  CS
-------------------------------------------------------------------
:10  0A00  00   70 47 00 BF 00 80 00 40 DC FC FF 1F 68 FD FF 1F  37
:10  0A10  00   90 F8 04 C0 0C F0 FC 03 03 F1 80 43 10 B5 03 F5  1B
:10  0A20  00   00 43 91 F8 04 E0 D3 F8 00 21 0E F0 FC 03 03 F1  39
:10  0A30  00   80 43 03 F5 00 43 4F EA CE 04 D3 F8 00 31 04 F0  BD
:10  0A40  00   18 04 1B BA E3 40 4F EA CC 04 12 BA 04 F0 18 04  AD
```

### Address command

```
   :               Colon
0: 02              Command type?
1: 0000            Reserved?
3: XX XX XX        Flash offset (?)
6: CS              Checksum
```

The header lines in tracker FW 1.5.0 are:

```
         32-bit
         Address
C  R     1  2  3   CS
---------------------
02 0000  02 10 00  EC
02 0000  02 20 00  DC
02 0000  02 30 00  CC
02 0000  02 40 00  BC
02 0000  02 50 00  AC
02 0000  02 60 00  9C
02 0000  02 70 00  8C
02 0000  02 80 00  7C
02 0000  02 90 00  6C
02 0000  02 A0 00  5C
02 0000  02 B0 00  4C
02 0000  02 C0 00  3C
02 0000  02 D0 00  2C
02 0000  02 E0 00  1C
```

They increment with a difference of 4096 (0x1000)
(which is the number of data lines) so it's likely
that these represent the offset in flash.

### Weird 12 byte line

"Unknown line": 34 characters


```
    :               Colon
0:  0C              Command type
1:  XXXX            Offset to patch (maybe??)
3:  00              Constant (reserved??)
4:  12 bytes        12 data bytes
17: XX              Checksum8 2s complement of the whole line

              1  2  3  4  5  6  7  8  9  10 11 12 CS
----------------------------------------------------
0C  2574  00  85 6B FB 7F B0 B0 A8 00 FF FF 01 00 EA
0C  2938  00  C1 67 FB 7F B0 B0 A8 00 FF FF 01 00 EA
0C  2944  00  B5 67 FB 7F B0 B0 A8 00 FF FF 01 00 EA
0C  2950  00  A9 67 FB 7F B0 B0 A8 00 FF FF 01 00 EA
0C  295C  00  08 B1 01 81 B0 B0 00 84 00 00 00 00 50
0C  29B4  00  08 B1 01 81 B0 B0 00 84 00 00 00 00 F8
0C  29C0  00  08 B1 01 81 B0 B0 00 84 00 00 00 00 EC
0C  2A24  00  D5 66 FB 7F A9 08 B1 00 FF FF 01 00 90
0C  9BA8  00  00 00 00 00 00 00 00 00 00 00 00 00 B1
```
