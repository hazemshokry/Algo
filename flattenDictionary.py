def flatten_dictionary(dd, prefix=''):
    return {prefix + '.' + k if prefix else k: v
            for kk, vv in dd.items()
            for k, v in flatten_dictionary(vv, kk).items()
            } if isinstance(dd, dict) else {prefix: dd}

def convert_flatten(d, parent_key=''):
    items = []
    for k, v in d.items():
        new_key = parent_key + '.' + k if parent_key else k

        if isinstance(v, dict):
            items += (convert_flatten(v, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == '__main__':
    dictionary = {
        "Key1": "1",
        "Key2": {
            "a": "2",
            "b": "3",
            "c": {
                "d": "3",
                "e": {
                    "": "1"
                }
            }
        }
    }
    print(flatten_dictionary(dictionary))
    print(convert_flatten(dictionary))
