def show_name(name):
    return f"Hello, {name}!"

def main():
    user_name = input("Enter your name: ")
    greeting = show_name(user_name)
    print(greeting)

if __name__ == "__main__":
    main()
