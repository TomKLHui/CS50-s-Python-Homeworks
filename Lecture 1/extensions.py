def main():
    file=input("File name: ")
    print(type(file))

def type(FILE):
    suffix=str.strip(FILE).lower().rsplit(sep=".")[-1]
    match suffix:
        case "jpg":
            return "image/jpeg"
        case "gif" | "jpeg" | "png":
            return "image/"+suffix
        case "pdf":
            return "application/"+suffix
        case "txt":
            return "text/plain"
        case "zip":
            return "application/"+suffix
        case _:
            return "application/octet-stream"

main()
