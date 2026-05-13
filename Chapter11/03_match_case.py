n =int(input("Enter status code :"))
def http_status(n):
    match n:
        case 200:
            return "ok"
        case 201:
            return "Created"
        case 404:
            return "Not found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
        
print(http_status(n))
