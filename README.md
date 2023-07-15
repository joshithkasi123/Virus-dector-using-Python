# Virus-dector using Python

The code provides a basic implementation of a virus detector in Python. It calculates the SHA-256 hash value for each file in the specified directory and its subdirectories.

Here's a breakdown of the code:

1.Importing the necessary libraries:

os library: Provides functions for interacting with the operating system, such as file operations.
hashlib library: Contains cryptographic hash functions, including SHA-256.
Defining the calculate_hash function:

2.Takes a file path as input.
Opens the file in binary mode and iteratively reads it in chunks.
Updates the SHA-256 hash object with each chunk of data.
Returns the hexadecimal representation of the calculated hash value.
Defining the scan_directory function:

3.Takes a directory path as input.
Uses the os.walk function to traverse through the specified directory and its subdirectories.
For each file encountered, it calculates the hash value using the calculate_hash function.
Prints the file path and its corresponding hash value.
Specifying the directory to scan:

4.Set the directory_to_scan variable to the path of the directory you want to scan.
Calling the scan_directory function:

5.Passes the directory_to_scan variable as the argument to the scan_directory function.
To use this code, make sure to replace "C:/Path/To/Directory" with the actual directory path you want to scan. When executed, the code will traverse through the directory and print the file paths along with their respective hash values.

Please note that this is a basic implementation and does not include advanced virus detection techniques.






