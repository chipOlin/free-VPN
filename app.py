import random


def get_random_configs(file_path: str, count: int = 100) -> list[str]:
    """Read file and return random lines."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    return random.sample(lines, min(count, len(lines)))


def main():
    file_path = "All_Configs_Sub.txt"
    configs = get_random_configs(file_path, 100)

    with open("random_100.txt", "w", encoding="utf-8") as f:
        for config in configs:
            f.write(config + "\n")


if __name__ == "__main__":
    main()
