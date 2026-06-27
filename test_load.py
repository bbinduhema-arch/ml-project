import os
import sys

print("Testing imports...")
try:
    import silk_worm
    print("silk_worm imported successfully")
except Exception as e:
    print(f"Error importing silk_worm: {e}")

try:
    import silk_leaf
    print("silk_leaf imported successfully")
except Exception as e:
    print(f"Error importing silk_leaf: {e}")

try:
    import price
    print("price imported successfully")
except Exception as e:
    print(f"Error importing price: {e}")

print("Testing model files existence...")
if os.path.exists('modellll.h5'):
    print("modellll.h5 exists")
else:
    print("modellll.h5 NOT found")

if os.path.exists('model2.h5'):
    print("model2.h5 exists")
else:
    print("model2.h5 NOT found")
