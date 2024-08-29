# lib/list_crud.py

def create_an_empty_list():
    '''Creates and returns an empty list.'''
    return []

def create_a_list():
    '''Creates and returns a list of length 4.'''
    return [1, 2, 3, 4]

def add_element_to_end_of_list(lst, element):
    '''Adds an element to the end of a list.'''
    lst.append(element)
    return lst

def add_element_to_start_of_list(lst, element):
    '''Adds an element to the start of a list.'''
    lst.insert(0, element)
    return lst

def remove_element_from_end_of_list(lst):
    '''Removes an element from the end of a list.'''
    if lst:
        lst.pop()
    return lst

def remove_element_from_start_of_list(lst):
    '''Removes an element from the start of a list.'''
    if lst:
        lst.pop(0)
    return lst

def retrieve_first_element_from_list(lst):
    '''Retrieves the first element from a list.'''
    if lst:
        return lst[0]
    return None  # Handle the case where the list might be empty

def retrieve_element_from_index(lst, index):
    '''Retrieves the element from the list at a given index.'''
    if 0 <= index < len(lst):
        return lst[index]
    return None  # Handle the case where the index is out of range

def retrieve_last_element_from_list(lst):
    '''Retrieves the last element from a list.'''
    if lst:
        return lst[-1]
    return None  # Handle the case where the list might be empty
