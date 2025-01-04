# Pix QR Code Generator

This is a Python-based tool to generate Pix QR codes, a payment system in Brazil. The tool takes dynamic inputs such as the recipient's name, Pix key, city, value, and transaction ID, and generates a valid Pix QR code.

## Features:
- Generates Pix QR code with customizable parameters.
- Supports dynamic values such as name, key, city, and amount.
- Uses CRC16 checksum for data integrity.
- Saves the generated QR code as a PNG image file.

## How to Use:

1. Just Do It in the code:
   ```python
   #                          name                       key                  city     value     txtId
   payloadCool = Payload('Michael Jackson', 'michaeljackson123@gmail.com', 'NEW YORK', 10.00, 'division')
   payloadCool.generatePayLoadCode()
