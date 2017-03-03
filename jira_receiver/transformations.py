import json


def transform_issue_updated_data(request_data):
    input_dict = json.loads(request_data)
    mapping_dict = {
        "story_number": ("issue", "key"),
        "title": ("issue", "fields", "summary"),
        "released_by": ("user", "displayName"),
        "assignee": ("issue", "fields", "assignee", "displayName"),
        "sign_off_by": ("issue", "fields", "customfield_11300"),
        "estimated_release_date": ("issue", "fields", "customfield_11301")
    }
    return _map_values(input_dict, mapping_dict)


def _get_nested_value(iter_dict, tuple):
    if len(tuple) < 2:
        return ""
    else:
        target_key_index = len(tuple) - 1
        target_key = tuple[target_key_index]

        index = 0
        while index < target_key_index:
            iter_dict = iter_dict.get(tuple[index], {})
            index += 1
        return iter_dict.get(target_key, "")


def _map_values(input_dict, mapping_dict):
    output_dict = dict()
    for key, map in mapping_dict.iteritems():
        output_dict[key] = _get_nested_value(input_dict, map)
    return output_dict
