def sorter(textbooks: list) -> list:
    """
    Sort a list of textbooks by subject irrespective of case or symbols.
    :param textbooks:
    :return:
    """
    sorted_list = sorted(textbooks, key=str.casefold)
    return sorted_list
