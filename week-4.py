def file_read_write():
    try:
        # Step 1: Ask the user for the input filename
        filename = input("Enter the name of the file to read: ")

        # Step 2: Open the file safely
        with open(filename, "r") as f:
            content = f.read()

        # Step 3: Modify the content (example: make text uppercase)
        modified_content = content.upper()

        # Step 4: Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified_content)

        print(f"✅ File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
file_read_write() 
