"""Dictionary Data Parsing Functions."""
META = {}


def flatten_dictionary_with_int(dictionary_data):
    """Return flat meta report dictionary from nested dictionary with ints."""
    meta_dict = META
    meta_dict["report"] = {}
    for item in dictionary_data:
        if type(dictionary_data[item]) is dict:
            for values in dictionary_data[item]:
                if type(dictionary_data[item][values]) is dict:
                    for second_values in dictionary_data[item][values]:
                        if type(dictionary_data[item][values][second_values]) is dict:
                            for third_values in dictionary_data[item][values][second_values]:
                                if type(dictionary_data[item][values][second_values][third_values]) is not list \
                                        or dict or None or type(dictionary_data[item][values][second_values]) is int:
                                    debug_dictionary_data = dictionary_data[item][values][second_values][third_values]
                                    if debug_dictionary_data:
                                        meta_dict["report"][str(
                                            item + "." + values + "." + second_values + "." + third_values)] = \
                                            str(dictionary_data[item][values][second_values][third_values])
                        elif type(dictionary_data[item][values][second_values]) is not list or None \
                                or type(dictionary_data[item][values][second_values]) is int:
                            none_dictionary_data = str(dictionary_data[item][values][second_values])
                            if none_dictionary_data:
                                meta_dict["report"][str(item + "." + values + "." + second_values)] = \
                                    str(dictionary_data[item][values][second_values])
                elif type(dictionary_data[item][values]) is not list or None:
                    values_dictionary_data = dictionary_data[item][values]
                    if values_dictionary_data and str(values_dictionary_data) != "none" \
                            or type(values_dictionary_data) is int:
                        meta_dict["report"][str(item + "." + values)] = str(dictionary_data[item][values])
        elif type(dictionary_data[item]) is list:
            for list_items in dictionary_data[item]:
                dictionary_data_dict = list_items
                if type(dictionary_data_dict) is str:
                    meta_dict["report"][item] = dictionary_data_dict
                else:
                    meta_dict[item] = dictionary_data[item]
        elif type(dictionary_data[item]) is not list or None:
            dictionary_data_item = dictionary_data[item]
            if dictionary_data_item and str(dictionary_data_item) != "none":
                meta_dict["report"][item] = dictionary_data[item]
    return meta_dict


def flatten_dictionary(json_data):
    """Return flat meta report dictionary from nested dictionary."""
    meta = {}
    meta["report"] = {}
    for item in json_data:
        if type(json_data[item]) is dict:
            for values in json_data[item]:
                if type(json_data[item][values]) is dict:
                    for second_values in json_data[item][values]:
                        if type(json_data[item][values][second_values]) is dict:
                            for third_values in json_data[item][values][second_values]:
                                if type(json_data[item][values][second_values][third_values])\
                                        is not list or dict or None:
                                    debug_test = json_data[item][values][second_values][third_values]
                                    if debug_test:
                                        meta["report"][str(item + "." + values + "." + second_values + "." +
                                                           third_values)] = \
                                                str(json_data[item][values][second_values][third_values])
                        elif type(json_data[item][values][second_values]) is not list or None:
                            none_test = str(json_data[item][values][second_values])
                            if none_test:
                                meta["report"][str(item + "." + values + "." + second_values)] =\
                                    str(json_data[item][values][second_values])
                elif type(json_data[item][values]) is not list or None:
                    values_test = json_data[item][values]
                    if values_test and str(values_test) != "none":
                        meta["report"][str(item + "." + values)] = str(json_data[item][values])
        elif type(json_data[item]) is list:
            for list_items in json_data[item]:
                test_dict = list_items
                if type(test_dict) is str:
                    meta["report"][item] = test_dict
                else:
                    meta[item] = json_data[item]
        elif type(json_data[item]) is not list or None:
            test_item = json_data[item]
            if test_item and str(test_item) != '"':
                meta["report"][item] = json_data[item]
    return meta