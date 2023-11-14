from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from datetime import datetime

def generate_key():
    # 使用当前时间生成一个简单的密钥
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    key = current_time.encode('utf-8')[:16]  # 取前16字节
    return key

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    # 使用 PKCS7 进行填充
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return cipher.iv, ciphertext

# 示例用法
user_input = input("请输入要加密的内容: ")
encryption_key = generate_key()

iv, encrypted_data = encrypt_data(user_input, encryption_key)

print("生成的密钥:", encryption_key)
print("加密后的内容:", encrypted_data)
print("初始向量 (IV):", iv)
