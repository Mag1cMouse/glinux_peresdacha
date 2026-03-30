def greet(name: str) -> str:
    return f"Привет, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def get_info() -> dict:
    return {
        "author": "Student",
        "subject": "Linux & DevOps",
        "topic": "CI/CD with GitHub Actions",
    }


def main():
    print("=== Консольное приложение ===")
    print(greet("Мир"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    info = get_info()
    print("\nИнформация о проекте:")
    for key, value in info.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
