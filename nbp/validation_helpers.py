from os.path import isfile, isdir

def validate_is_path(field, value, error):
    validate(field, value, self.__is_file_or_dir, 'dir or file', error)

def validate_is_dir(field, value, error):
    validate(field, value, isdir, 'dir', error)

def validate_is_file(field, value, error):
    validate(field, value, isfile, 'file', error)

def is_file_or_dir(path):
    return isfile(path) or isdir(path)

def validate(field, path, func, entity, error):
    if not func(path):
        error(field, "Must be a valid path to " + entity)
