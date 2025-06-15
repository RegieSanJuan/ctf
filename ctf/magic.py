#!/usr/bin/env python3

import os
import threading
import argparse

def decrypt_chunk(start, end, xor_key, data):
    return bytearray([data[i] ^ ord(xor_key[i % len(xor_key)]) for i in range(start, end)])

def main(threads, filename, output_filename):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    jpg_enc_path = os.path.join(cur_path, filename)

    if not os.path.isfile(jpg_enc_path):
        print(f"Unable to find encrypted JPG at: '{jpg_enc_path}'")
        exit(1)

    with open(jpg_enc_path, "rb") as jpg_enc:
        jpg_enc_data = jpg_enc.read()

    jpg_magic = b"\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01"
    jpg_enc_magic = jpg_enc_data[:len(jpg_magic)]

    print(f"JPG Magic:           {' '.join(['{:02X}'.format(b) for b in jpg_magic])}")
    print(f"JPG Encrypted Magic: {' '.join(['{:02X}'.format(b) for b in jpg_enc_magic])}")

    xor_key = "".join([chr(jpg_enc_magic[i] ^ jpg_magic[i]) for i in range(len(jpg_magic))])
    print(f"XOR Key used:        {' '.join(['{:02X}'.format(ord(b)) for b in xor_key])}")

    chunk_size = len(jpg_enc_data) // threads
    results = [bytearray() for _ in range(threads)]
    thread_list = []

    def thread_worker(i, start, end):
        results[i] = decrypt_chunk(start, end, xor_key, jpg_enc_data)

    for i in range(threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != threads - 1 else len(jpg_enc_data)
        t = threading.Thread(target=thread_worker, args=(i, start_index, end_index))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    decrypted_data = bytearray().join(results)

    with open(output_filename, "wb") as jpg_dec:
        jpg_dec.write(decrypted_data)

    with open(output_filename, "rb") as jpg_dec:
        jpg_dec_data = jpg_dec.read()

    jpg_dec_magic = jpg_dec_data[:len(jpg_magic)]

    print(f"JPG Dec Magic:       {' '.join(['{:02X}'.format(b) for b in jpg_dec_magic])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decrypt a jpg.enc file.")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of threads to use.")
    parser.add_argument("-f", "--filename", default="my_magic_bytes.jpg.enc", help="Input filename.")
    parser.add_argument("-o", "--output", default="output.jpg", help="Output filename.")
    args = parser.parse_args()

    main(args.threads, args.filename, args.output)
