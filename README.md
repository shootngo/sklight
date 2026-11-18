# SKLight Test (V 0.1)

Web Bluetooth test page for Westinghouse SKLight Bluetooth string lights (controller MS18-304-104-52).
Open in Chrome on Android with Bluetooth and Location on.

Protocol taken from the original "Westinghouse Smart Landscape" app (com.ceibacity.rgb):
- FFF3: read 4-byte challenge, answer [a0,a1,FF x12] where a0=mac0^mac1^mac2^r0^r1, a1=mac3^mac4^mac5^r2^r3
- FFF5: keep-alive 0x11 every 2 s
- FFF6: clock [weekday 0=Mon, h, m, s]
- FFF1 commands (7 bytes): FA 01 R G B 00 00 color, FA 02 W warm white, FA 03 01 on / FA 03 02 off, FA 04 0n scene
- FFF2 notifications report state in the same layout without the FA prefix
