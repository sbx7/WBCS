import ctypes
path = input("Enter the path of the image:")
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
print("Done!")