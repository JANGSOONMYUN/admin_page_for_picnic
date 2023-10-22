import json

def get_picnic_config(json_path = '../chatgpt_module_for_picnic/character_setting.json'):
    # Load the JSON data from the file
    data = None
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

def set_pre_text(pre_text, json_path = '../chatgpt_module_for_picnic/character_setting.json'):
    json_data = get_picnic_config(json_path)
    json_data['0']['pre_text'] = [pre_text]
    with open(json_path, "w", encoding="utf-8") as json_file:
        # json.dump(json_data, json_file)
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

def get_pre_text(json_path = '../chatgpt_module_for_picnic/character_setting.json'):
    json_data = get_picnic_config(json_path)
    return json_data['0']['pre_text']

def set_post_text(post_text, json_path = '../chatgpt_module_for_picnic/character_setting.json'):
    json_data = get_picnic_config(json_path)
    json_data['0']['post_text'] = [post_text]
    with open(json_path, "w", encoding="utf-8") as json_file:
        # json.dump(json_data, json_file)
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

def get_post_text(json_path = '../chatgpt_module_for_picnic/character_setting.json'):
    json_data = get_picnic_config(json_path)
    return json_data['0']['post_text']
