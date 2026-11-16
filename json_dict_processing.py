def extract_nested_value(obj, keys):
    for key in keys:
        if not isinstance(obj,dict):
            return None
        if key not in obj:
            return None
        obj = obj[key]
    return obj

def process_dictionary_with_config(dictionary, config):
    ans = {}
    for point in config:
        if isinstance(config[point], tuple):
            keys = config[point][0]
            value = extract_nested_value(dictionary, keys)
            if value is None:
                ans[point] = None
            else:
                ans[point] = config[point][1](value)
        else:
            keys = config[point]
            value = extract_nested_value(dictionary, keys)
            ans[point] = value
    return ans

def process_list_of_dicts_with_config(list_of_dicts, config):
    ans = []
    for dictionary in list_of_dicts:
        ans.append(process_dictionary_with_config(dictionary, config))
    return ans

def create_processor(config, list_processor=False):
    if list_processor:
        process = process_list_of_dicts_with_config
    else:
        process = process_dictionary_with_config
    def processor(values):
        return process(values, config)
    return processor