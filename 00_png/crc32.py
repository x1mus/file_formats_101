def convert_hex_to_binary_list(message):
    # Convert the hex values to a binary string
    binary = "{0:b}".format(int(message, 16))

    # Adding 0 on the left to be sure this a a multiple of 8 bits
    while len(binary) % 8 != 0:
        binary = "0" + binary

    # Return the list of bytes
    return [binary[i:i+8] for i in range(0, len(binary), 8)]


def invert_bits(message):
    inverted_message = ""
    for bit in message:
        if bit == "0":
            inverted_message += "1"
        else:
            inverted_message += "0"

    return inverted_message


def main():
    message = "494844520000038C000002D00806000000"
    poly = "104C11DB7"
    poly_binary = "{0:b}".format(int(poly, 16))
    expected_crc = "DBF1FE9A"
    print("INITIAL VALUES :")
    print("================")
    print("Message in hex :", message)
    print("Poly in hex :", poly)
    print("Poly in binary :", poly_binary)
    print("Expected CRC :", expected_crc)
    print()


    bytes_list = convert_hex_to_binary_list(message)
    print("Initial input message :")
    print("=======================")
    print(bytes_list)
    print()

    """First step:
    =====================
    - Reverse the input bits for each bytes
    """
    temp = []
    for byte in bytes_list:
        temp.append(byte[::-1])
    bytes_list = temp
    del temp
    print("Each bytes reversed input message :")
    print("===================================")
    print(bytes_list)
    print()

    """Second step:
    =====================
    - Adding padding to the input (4 bytes of 0)
    """
    i = 0
    while i < 4:
        bytes_list.append("00000000")
        i += 1
    print("Padding added to input message :")
    print("================================")
    print(bytes_list)
    print()


    """Third step:
    =====================
    - Concatenate the bytes to a string of bits
    """
    final_input_binary = ""
    for byte in bytes_list:
        final_input_binary += byte
    print("Concatinating the bytes to a string of bits :")
    print("===================================")
    print(final_input_binary)
    print()

    """Fourth step:
    =====================
    - Make the division and save the remainder
    """
    print("Modulo 2 division:")
    print("===================================")
    msg_bits = len(final_input_binary) - 32 # remember, we added padding
    # Initial CRC is sometimes used to avoid poor error checking quality in
    # edge cases where the data is simply 0000000...
    initial_crc = "11111111111111111111111111111111"
    remainder = final_input_binary
    counter = 0
    start = True
    while counter < msg_bits:
      if start:
          poly = initial_crc
          start = False
      else:
          poly = poly_binary
      print(remainder)
      print("--------------------------------")
      print(poly)

      interim = ""
      bit_pos = 0
      for bit in remainder:
        if bit_pos < len(poly):
          poly_bit = poly[bit_pos]
          if poly_bit == "1" and bit == "1":
            interim += "0"
          elif poly_bit == "1" or bit == "1":
            interim += "1"
          else:
            interim += "0"
        else:
          interim += bit
        bit_pos += 1
      remainder = interim
      print(remainder)
      # shift zeros out
      first_zeros = 1
      interim = ""
      for bit in remainder:
        if bit == "0" and first_zeros == 1 and counter < msg_bits:
          counter += 1
          print(f"{counter}: shift 1 bit left")
        else:
          interim += bit
          first_zeros = 0

      remainder = interim

    print("Computed the remainder :")
    print("========================")
    print(remainder)
    print()

    """Fifth step:
    =====================
    - XOR the remainder with 0xFF (Invert the bits)
    """
    remainder = invert_bits(remainder)
    print("Inverted remainder :")
    print("====================")
    print(remainder)
    print()

    """Last step:
    =====================
    - Reverse the entire binary
    """
    remainder = remainder[::-1]
    print("Reversed remainder :")
    print("====================")
    print(remainder)
    print()


    """Displaying results
    """
    remainder = hex(int(remainder, 2))
    print("Obtained results :")
    print("==================")
    print("Computed CRC :", str(remainder)[2:].upper())
    print("Expected CRC :", expected_crc)
    print()


    print("Are the CRC equivalent ?")
    print("========================")
    if str(remainder)[2:].upper() == expected_crc:
        print("They are !")
    else:
        print("They aren't !")


if __name__ == "__main__":
    main()