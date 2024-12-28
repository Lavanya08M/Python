def main():
    file_name = input("File name: ").strip().lower()
    
    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith((".jpeg", ".jpg")):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")

if __name__ == "__main__":
    main()