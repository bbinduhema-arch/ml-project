with open('model2.h5', 'rb') as f:
    header = f.read(8)
    print(f"Header: {header}")
    if header == b'\x89HDF\r\n\x1a\n':
        print("Valid HDF5 signature")
    else:
        print("Invalid HDF5 signature")
