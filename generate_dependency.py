import os
from openai import OpenAI
import requests
import time
import json
import pickle
import re
import ast


# action_list = ['navigate_to(cabinet)_1',
# 'open(cabinet)_1',
# 'grasp(plate_1)_1',
# 'close(cabinet)_1',
# 'navigate_to(counter_top)_1',
# 'place_ontop(plate_1, counter_top)_1',
# 'grasp(pie_1)_1',
# 'place_inside(pie_1, plate_1)_1',
# 'navigate_to(cabinet)_2',
# 'open(cabinet)_2',
# 'grasp(plate_2)_1',
# 'close(cabinet)_2',
# 'navigate_to(counter_top)_2',
# 'place_ontop(plate_2,countertop)_1',
# 'grasp(pie_2)_1',
# 'place_inside(pie_2, plate_2)_1',
# 'navigate_to(refrigerator)_1',
# 'open(refrigerator)_1',
# 'navigate_to(countertop)_1',
# 'grasp(plate_1)_2',
# 'grasp(plate_2)_2',
# 'navigate_to(refrigerator)_2',
# 'place_inside(plate_1,refrigerator)_1',
# 'place_inside(plate_2,refrigerator)_1',
# 'close(refrigerator)_1']

# action_list = ['navigate_to(countertop_kelzer_0)',
#             "grasp(paper_coffee_filter_210)",
#             "place_ontop(paper_coffee_filter_210, coffee_maker_212)",
#             "grasp(bottle_of_coffee_211)",
#             "place_ontop(bottle_of_coffee_211, coffee_maker_212)",
#             "grasp(saucer_208)",
#             "place_nextto(saucer_208, coffee_maker_212)",
#             "grasp(electric_kettle_207)",
#             "place_nextto(electric_kettle_207, coffee_maker_212)",
#             "grasp(coffee_cup_209)",
#             "place_ontop(coffee_cup_209,saucer_208)"
#             ]
# define system prompt



def qwen(api_key, prompt, prompt_system):
    assert isinstance(prompt_system, str)
    assert isinstance(prompt, str)

    try:
        client = OpenAI(
            # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
            # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
            api_key=api_key,
            # 以下是北京地域base_url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        completion = client.chat.completions.create(
            model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            messages=[
                {'role': 'system', 'content': prompt_system},
                {'role': 'user', 'content': prompt}
                ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")


def gpt4o_mini(api_key, prompt, prompt_system, max_retries=10000, retry_delay=5):  # It is -o-mini
    # OpenAI API Key

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-5-mini",
        "messages": [
            {
                "role": "system",
                "content": prompt_system
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    print("start querying GPT4o...")
    for attempt in range(1, max_retries + 1):
        try:
            "https://api2.aigcbest.top/v1/chat/completions"
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

            output = response.json()
            return output["choices"][0]['message']["content"]

        except (requests.RequestException, json.JSONDecodeError) as e:
            print(f"[GPT ERROR] Attempt {attempt}/{max_retries}: {e}")
            if attempt < max_retries:
                print(f"Retrying after {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("[GPT ERROR] Maximum retries reached, aborting.")
                raise e
    raise ValueError("Cannot get responses from API")

    # key=api_key

    # client = OpenAI(
    #     base_url="https://api2.aigcbest.top/v1",
    #     api_key=key
    # )

    # response = client.chat.completions.create(
    # model="gpt-4o",
    # messages=[
    #     {"role": "user", "content": prompt},
    #     {"role": "system", "content": prompt_system}
    # ]
    # )
    # print(response)

    # return response.choices[0].message.content


action_dependency={
    'navigate_to(cabinet)_1': [],
    'open(cabinet)_1':['navigate_to(cabinet)_1'],
    'grasp(plate_1)_1':['open(cabinet)_1','navigate_to(cabinet)_1'],
    'close(cabinet)_1':['open(cabinet)_1','navigate_to(cabinet)_1'],
    'navigate_to(counter_top)_1':[],
    'place_ontop(plate_1, counter_top)_1':['navigate_to(counter_top)_1','grasp(plate_1)_1'],
    'grasp(pie_1)_1':['navigate_to(counter_top)_1'],
    'place_inside(pie_1, plate_1)_1':['place_ontop(plate_1, counter_top)_1','grasp(pie_1)_1'],
    'navigate_to(cabinet)_2':[],
    'open(cabinet)_2':['navigate_to(cabinet)_2'],
    'grasp(plate_2)_1':['navigate_to(cabinet)_2','open(cabinet)_2'],
    'close(cabinet)_2':['open(cabinet)_2','navigate_to(cabinet)_2'],
    'navigate_to(counter_top)_2':[],
    'place_ontop(plate_2,countertop)_1':['navigate_to(counter_top)_2','grasp(plate_2)_1'],
    'grasp(pie_2)_1':['navigate_to(counter_top)_2'],
    'place_inside(pie_2, plate_2)_1':['place_ontop(plate_2,countertop)_1','grasp(pie_2)_1'],
    'navigate_to(refrigerator)_1':[],
    'open(refrigerator)_1':['navigate_to(refrigerator)_1'],
    'navigate_to(counter_top)_3':[],
    'grasp(plate_1)_2':['navigate_to(counter_top)_3','place_ontop(plate_1, counter_top)_1'],
    'grasp(plate_2)_2':['navigate_to(counter_top)_3','place_ontop(plate_2,countertop)_1'],
    'navigate_to(refrigerator)_2':[],
    'place_inside(plate_1,refrigerator)_1':['navigate_to(refrigerator)_2','open(refrigerator)_1','grasp(plate_1)_2'],
    'place_inside(plate_2,refrigerator)_1':['navigate_to(refrigerator)_2','open(refrigerator)_1','grasp(plate_2)_2'],
    'close(refrigerator)_1':['open(refrigerator)_1','navigate_to(refrigerator)_2']
}


if __name__ == "__main__":
    system_prompt = """You are an expert at analyzing dependencies between actions in a sequence. Given a list of actions in order, your task is to identify which actions are dependent on the previous actions. For example, action 'B' is dependent on action 'A' if 'B' cannot be performed before 'A' is completed.\n
                       Please Remember for any action, I only need to output the direct dependencies, not the transitive dependencies. For example, if action 'C' depends on 'B', and 'B' depends on 'A', then 'C' directly depends only on 'B'.\n
                       Your output should be in the format of a dictionary, where each key is an action from the list, and its value is a list of actions it directly depends on. If an action has no dependencies, its value should be an empty list.\n
                       Here is an example output format:\n
                       {'action_1': [], 'action_2': ['action_1'], 'action_3': ['action_1', 'action_2'], 'action_4': ['action_2']}\n
                       PLEASE FOLLOW THESE RULES STRICTLY:\n
                        1. Only include actions that are present in the provided list.\n
                        2. The action list is ordered. The current action can ONLY depend on PREVIOUS actions.\n
                        3. Navigation actions (e.g., navigate_to(location)) typically have no dependencies.\n
                        4. Please consider the dependencies at action level, NOT at task level. For example, close(cabinet) may depend on open(cabinet), but it MUST not depend on the entire task of placing items inside the cabinet.\n
                       Do NOT output any explanations or additional text, only provide the dictionary as specified.
                       Now, please analyze the following list of actions and provide the dependencies accordingly.    
                    """

    # load the scene graph
    root_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/data/segmented_activities/'
    action_list_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/action_sequence/'
    save_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/action_dependency/'

    for name in os.listdir(root_path):
        # extract the task name from the file name
        parts = re.split(r'(?=\d)', name, maxsplit=1)
        task_name = parts[0].replace('_', ' ').rstrip()
        file_path = os.path.join(root_path, name)
        scene_graph_file_path = os.path.join(file_path, 'segmented_scene_graph_0.json')

        # extract scene graph
        with open(scene_graph_file_path, 'r', encoding='utf-8') as file:
            f = json.load(file)
            scene_graph_task = f['59']['edges']

        # extract action list
        action_path = os.path.join(os.path.join(action_list_path, name),'action_sequence.pkl')
        with open(action_path, 'rb') as file:
            action_list = pickle.load(file)

        # define user prompt

        user_prompt = f"""
                        I will provide you the initial scene information in the following list:
                        {scene_graph_task}
                        This scene graph record the spatial relationship of the objects in the scene. 
                        ```INPUT:
                        Task Instruction: set up a coffee station.\n
                        Ordered Action List:{action_list}\n
                        ```OUTPUT:
                       """




# output = qwen(api_key="sk-75ff0fac6cbb4d21b68a17e910540b4e",
#               prompt = user_prompt,
#               prompt_system=system_prompt)



        response = gpt4o_mini(api_key ="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",
                    prompt = user_prompt,
                    prompt_system=system_prompt)

        output = ast.literal_eval(response)
        # output=  json.loads(response)
        print(output)

        os.makedirs(os.path.join(save_path, name), exist_ok=True)
        save_file_path = os.path.join(os.path.join(save_path, name), 'action_dependency.json')
        with open(save_file_path, 'w', encoding='utf-8') as file:
            json.dump(output, file, ensure_ascii=False, indent=4)
            print('saved to {}'.format(save_file_path))


# This code is used to analyze the frequency of each action being a dependency in the action_dependency dictionary
# dependecy_cnt = {}

# for action,dependency in action_dependency.items():
#     for act in dependency:
#         if act not in dependecy_cnt:
#             dependecy_cnt[act]=1
#         else:
#             dependecy_cnt[act]+=1

# print(dependecy_cnt)



# max_cnt = max(dependecy_cnt.values())
# keys_with_max = [k for k, v in dependecy_cnt.items() if v == max_cnt]
# print(keys_with_max)