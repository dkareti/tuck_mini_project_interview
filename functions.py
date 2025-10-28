#import libraries
import os 
import json


def read_json() -> json:
    '''
    This function attempts to read the json file that is passed in. 
    If it suceeds, the json object is returned. Otherwise, an error 
    message is printed.
    '''
    try:
        # right now hardcode the .json file, but in the future get the .json from the custom GPT
        with open('./dev/test.json', 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f'An error occured when reading the json file: {e}')
        return None
    
def access_field() -> str:
    '''
    This function is designed to return the 'gptOutput' field.
    '''
    
    json_info = read_json()
    specific_data = json_info['gptOutput']

    return specific_data
    
def modify_json(markdown: str, additional_info: str, json_obj: json) -> str:
    '''
    This function will modify the markdown object, assuming it is not corrupt.
    It will append the additional info to the markdown string.
    
    '''
    tot = markdown + additional_info

    json_obj['gptOutput'] = tot



    return json_obj

    

