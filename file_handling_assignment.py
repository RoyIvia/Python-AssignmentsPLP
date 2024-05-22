try:
    # File Creation
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1.\n")
        file.write("Line 2: 12345\n")
        file.write("Last line of text.")

    # File Reading and Display
    with open("my_file.txt", 'r') as file:
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line.strip())  # Strip newline characters for clean display

    # File Appending
    with open("my_file.txt", 'a') as file:
        file.write("\n\nAdditional line 1.\n")
        file.write("Line 6: 67890\n")
        file.write("Another new line added.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except Exception as e:
    print("Error:", e)
finally:
    print("File handling completed.")
