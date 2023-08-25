def set_to_comma_separated_string(input_set: set) -> str:
    """Convert a set to a comma-separated string"""

    """Validate the input data"""
    if not isinstance(input_set, set):
        raise TypeError("Input must be a set")

    output_string = ", ".join(str(elem) for elem in input_set)
    return output_string


if __name__ == '__main__':
    print(set_to_comma_separated_string({'wolf', 'fox', 'donkey', 'rabbit'}))
