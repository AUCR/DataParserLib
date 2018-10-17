"""Dictionary Data Parsing Functions."""
# coding=utf-8
META = {}


def flatten_dictionary(dictionary_data):
    """Return flat meta report dictionary from nested dictionary."""
    meta = META
    meta["report"] = {}
    for item in dictionary_data:
        if type(dictionary_data[item]) is dict:
            for values in dictionary_data[item]:
                if type(dictionary_data[item][values]) is dict:
                    for second_values in dictionary_data[item][values]:
                        if type(dictionary_data[item][values][second_values]) is dict:
                            for third_values in dictionary_data[item][values][second_values]:
                                if type(dictionary_data[item][values][second_values][third_values]) is not list \
                                        or dict or None or type(dictionary_data[item][values][second_values]) is int:
                                    print(type(dictionary_data[item][values][second_values][third_values]))
                                    debug_dictionary_data = dictionary_data[item][values][second_values][third_values]
                                    if debug_dictionary_data:
                                        meta["report"][str(
                                            item + "." + values + "." + second_values + "." + third_values)] = \
                                            str(dictionary_data[item][values][second_values][third_values])
                        elif type(dictionary_data[item][values][second_values]) is not list or None \
                                or type(dictionary_data[item][values][second_values]) is int:
                            none_dictionary_data = str(dictionary_data[item][values][second_values])
                            if none_dictionary_data:
                                meta["report"][str(item + "." + values + "." + second_values)] = \
                                    str(dictionary_data[item][values][second_values])
                elif type(dictionary_data[item][values]) is not list or None:
                    values_dictionary_data = dictionary_data[item][values]
                    if values_dictionary_data and str(values_dictionary_data) != "none" \
                            or type(values_dictionary_data) is int:
                        meta["report"][str(item + "." + values)] = str(dictionary_data[item][values])
        elif type(dictionary_data[item]) is list:
            for list_items in dictionary_data[item]:
                dictionary_data_dict = list_items
                if type(dictionary_data_dict) is str:
                    meta["report"][item] = dictionary_data_dict
                else:
                    meta[item] = dictionary_data[item]
        elif type(dictionary_data[item]) is not list or None:
            dictionary_data_item = dictionary_data[item]
            if dictionary_data_item and str(dictionary_data_item) != "none":
                meta["report"][item] = dictionary_data[item]
    return meta
