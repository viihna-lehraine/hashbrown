import hashlib
import os

def calculate_file_hash(file_path, algorithm):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None
    
    try:
        hash_func = getattr(hashlib, algorithm)
        hash_obj = hash_func()
    except AttributeError:
        print(f"Error: Unsupported algorithm '{algorithm}'")
        return None
    
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Error: An error occured while reading the file. {e}")
        return None
    
def main():
    print("Welcome to Hashbrown v0.01")
    print("This program will help you calculate the hash of a file using a variety of algorithms.")

    file_path = input("Please enter the file path: ")

    algorithms = [
        'md4', 'md5', 'sha1', 'sha224', 'sha256', 'sha385', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'blake2b', 'blake2s', 'shake_256', 'ripemd160', 'whirlpool'
    ]

    print("\nSupported algorithms:")
    for i, algo in enumerate(algorithms, 1):
        print(f"{i}, {algo}")

    try: 
        choice = int(input("\nEnter the number of the desired algorithm:"))
        if 1 <= choice <= len(algorithms):
            algorithm = algorithms[choice - 1]
        else:
            print("Error: Invalid input. Please run the program again and enter a number.\n(INPUT OUTSIDE ACCEPTED RANGE)")
            return
    except ValueError:
        print("Error: Invalid input. Plase run the program again and enter a number.\n(VALUE ERROR)")
        return

    hash_value = calculate_file_hash(file_path, algorithm)
    if hash_value:
        print(f"\nThe {algorithm} hash of the file is: {hash_value}")

if __name__ == "__main__":
    main()