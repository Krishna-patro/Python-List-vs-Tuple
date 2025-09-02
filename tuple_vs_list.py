def demonstrate_differences():
    """
    Demonstrates the key technical differences between a Python list and a tuple.
    """
    # Lists are mutable (can be changed).
    my_list = [1, 2, 3]
    print(f"Original List: {my_list}")
    my_list.append(4)
    print(f"List after adding an element: {my_list}")
    my_list[0] = 99
    print(f"List after changing an element: {my_list}")

    # Tuples are immutable (cannot be changed).
    my_tuple = (1, 2, 3)
    print(f"\nOriginal Tuple: {my_tuple}")

    try:
        my_tuple[0] = 99
    except TypeError as e:
        print(f"Trying to change a tuple element results in a: {e}")

    try:
        my_tuple.append(4)
    except AttributeError as e:
        print(f"Trying to append to a tuple results in an: {e}")

    print("\n--- Summary of Differences ---")
    print("1. Mutability:")
    print("   - Lists are MUTABLE.")
    print("   - Tuples are IMMUTABLE.")

    print("\n2. Performance & Memory:")
    print("   - Tuples are generally slightly faster and use less memory.")

if __name__ == "__main__":
    demonstrate_differences()
