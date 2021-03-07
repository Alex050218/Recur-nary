def bin_recursive(num: int, bin_num: str = "") -> str:
    if num > 2147483647:
        raise Exception(f"The value {num} can´t be a binary number")

    if num == 0:
        return bin_num if len(bin_num) >= 1 else "0"
    
    bin_num = f"{num % 2}{bin_num}"
    num = int(num / 2)
    return bin_recursive(num, bin_num)


if __name__ == "__main__":
    num = 2147
    val_bin: str = bin_recursive(num)
    print(f"The binary value {val_bin} is {num} in decimal")
