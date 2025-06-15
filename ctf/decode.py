import base64

inner_b64 = "MjQ3Q1RGe2RhODA3OTVmOGE1Y2FiMmUwMzdkNzM4NTgwN2I5YTkxfQ=="

decoded_bytes = base64.b64decode(inner_b64)
decoded_str = decoded_bytes.decode('utf-8')

print(decoded_str)
