# McDonald's Ireland Receipt Code Decoder

This project provides a tool to decode McDonald's Ireland receipt codes, extracting valuable information such as order numbers, store IDs, and purchase timestamps from the receipt codes.

## Overview

McDonald's Ireland uses a specific encoding system for their receipt codes that contains several pieces of information:
- Store ID
- Order ID
- Purchase timestamp
- Check digit

The codes are encoded using a custom base-25 system with a specific character mapping.

## Features

- Decodes McDonald's Ireland receipt codes
- Extracts the following information:
  - Store ID
  - Order ID (last 2 digits)
  - Purchase timestamp
  - Validates check digit

## Code Format

The receipt code follows this format: `XXXX-XXXX-XXXX` where:
- First 3 characters: Store ID
- Next 3 characters: Order ID (encoded)
- Next 5 characters: Timestamp (minutes since 2016-02-01 00:00)
- Last character: Check digit

## Character Encoding

The project uses a base-25 encoding system with the following character mapping:
```
Decimal: 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Base 25: C  M  7  W  D  6  N  4  R  H  F  9  Z  L  3  X  K  Q  G  V  P  B  T  J  Y
```

## Usage

1. Clone this repository
2. Run the decoder with your receipt code:

```python
from code_to_order import decode_receipt_code

# Example code
code = "9HYW-XRZH-PTB3"
result = decode_receipt_code(code)
print(result)
```

## Requirements

- Python 3.x
- datetime
- No external dependencies required

## Disclaimer

This project is for educational purposes only. The decoding system was reverse-engineered and may not work with all receipt codes or may stop working if McDonald's changes their encoding system.

## License

MIT License