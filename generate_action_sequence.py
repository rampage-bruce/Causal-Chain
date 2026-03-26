import requests
import json
import time

import os
from openai import OpenAI
import re
import pickle

def save_list_pickle(data, filepath):
    # Ensure parent directory exists
    parent_dir = os.path.dirname(filepath)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    # Check if file exists; create if not
    if not os.path.exists(filepath):
        open(filepath, "wb").close()

    # Write pickle
    with open(filepath, "wb") as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

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
        print(completion.choices[0].message.content)
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")




def gpt5_mini(api_key, prompt, prompt_system, max_retries=100, retry_delay=5):  # It is -o-mini
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
    #
    # client = OpenAI(
    #     base_url="https://api2.aigcbest.top/v1",
    #     api_key=key
    # )
    #
    # response = client.chat.completions.create(
    # model="gpt-4o",
    # messages=[
    #     {"role": "user", "content": prompt},
    #     {"role": "system", "content": prompt_system}
    # ]
    # )
    # print(response)
    #
    # return response.choices[0].message.content

if __name__ == "__main__":

    example_file_name = '/Users/rampage/PycharmProjects/Simulators/ENACT/data/segmented_activities/freeze_pies_1750762043202007/segmented_scene_graph_0.json'
    with open(example_file_name,'r') as file:
        scene_graph_example = file.read()

    action_domain_file = 'action_domain.txt'
    with open(action_domain_file, 'r', encoding='utf-8') as file:
        action_domain = file.read()


    prompt_system = """You are proficient at planning and I need you to generate symbolic action list according to the task instruct and scene graph information I give you.\n
                    The scene graph record the scene state transition when the action trajectory is performed. I need you to recover the symbolic action list according to the scene graph transition order.\n
                    Please ONLY use the actions in action domain and consider their preconditions and effects.\n
                    Your Answer MUST be ONLY a Python json dict containing a list of actions in order. Don't reply anything else! You Must reply in the format just like the example does."""

    root_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/data/segmented_activities/'
    save_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/action_sequence/'
    for name in os.listdir(root_path):
        # extract the task name from the file name
        parts = re.split(r'(?=\d)', name, maxsplit=1)
        task_name = parts[0].replace('_',' ').rstrip()
        file_path  = os.path.join(root_path, name)
        scene_graph_file_path = os.path.join(file_path, 'segmented_scene_graph_0.json')
        with open(scene_graph_file_path, 'r', encoding='utf-8') as file:
            scene_graph_task = file.read()

        prompt = f"""I will give you scene graphs record in json format. The scene graph json contains sequential scene graph each of which is represented in a number (for example, 59)"
                 The scene graph "59" record the spatial relationship of the objects at the "edges" key. Other scene graphs ONLY record the difference between current scene graph and the previous scene graph.
                 I will also give you an action domain the define all the symbolic actions you can use. Each action contain its name, preconditions and effects. \n
                 This is the action domain: {action_domain}.\n
                 I will give you an example:\n
                 ```INPUT:
                 Task Instruction: freeze pies.\n
                 Scene Graph:{str(scene_graph_example)}.\n
                 ```OUTPUT:
                 {{"Answer":["navigate_to(bottom_cabinet_no_top_gjeoer_0)",
                            "open(bottom_cabinet_no_top_gjeoer_0)",
                            "grasp(tupperware_231)",
                            "close(bottom_cabinet_no_top_gjeoer_0)",
                            "navigate_to(countertop_kelzer_0)",
                            "place_ontop(tupperware_231, countertop_kelzer_0)",
                            "grasp(apple_pie_234)",
                            "place_inside(apple_pie_234, tupperware_231)",
                            "navigate_to(bottom_cabinet_no_top_gjeoer_0)",
                            "open(bottom_cabinet_no_top_gjeoer_0)",
                            "grasp(tupperware_230)",
                            "close(bottom_cabinet_no_top_gjeoer_0)",
                            "navigate_to(countertop_kelzer_0)",
                            "place_ontop(tupperware_230,countertop_kelzer_0)",
                            "grasp(apple_pie_235)",
                            "place_inside(apple_pie_235, tupperware_230)",
                            "navigate_to(fridge_dszchb_0)",
                            "open(fridge_dszchb_0)",
                            "navigate_to(countertop_kelzer_0)",
                            "grasp(tupperware_230)",
                            "grasp(tupperware_231)",
                            "navigate_to(fridge_dszchb_0)",
                            "place_inside(tupperware_230,fridge_dszchb_0)",
                            "place_inside(tupperware_231,fridge_dszchb_0)",
                            "close(fridge_dszchb_0)"]}} \n
                 Remember:
                 1. When using 'navigate_to()', if the object is placed onto or inside a container, please navigate_to(container) instead of navigate_to(object) For example, when you need to grasp a cup on the table, you should call navigate_to(table) instead of navigate_to(cup).\n
                 2. If you need to grasp an object which is not explicitly recorded to placed on or inside a container, you can navigate_to(object) directly. If the object is on the floor, you can also navigate_to(object) too.\n
                 3. You Must navigate_to the container of the object to perform grasp if you the container is not reachable. If you have already been navigated to the container, you don't need to call navigate_to(container) again. Please keep in mind what your current location is.\n
                 4. You are a robot with 2 arms that can grasp objects and can move with wheels. You can hold at MOST 2 objects at the same time.\n
                 5. The output format should strictly follow the format described above.\n
                 Now I need you to generate action list according to the following Task Instruction and Scene Graph:\n
                 ```INPUT:\n
                 Task Instruction:{task_name}.\n
                 Scene Graph:{str(scene_graph_task)}.\n
                 ```OUTPUT:"""

        response = gpt5_mini(api_key='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',
                            prompt = prompt,
                            prompt_system=prompt_system)

        # output = qwen(api_key="sk-75ff0fac6cbb4d21b68a17e910540b4e",
        #               prompt = prompt,
        #               prompt_system=prompt_system)

        print(response)
        output = json.loads(response)
        answer  = output['Answer']

        # number the action list
        ordered_answer = []
        temp_dic = {}
        for action in answer:
            action = action.lower()
            if action in temp_dic:
                temp_dic[action]+=1
                action = action+f'_{temp_dic[action]}'
            else:
                temp_dic[action]=1
                action = action+f'_{temp_dic[action]}'

            ordered_answer.append(action)

        save_file_path = os.path.join(os.path.join(save_path,name), 'action_sequence.pkl')
        save_list_pickle(data=ordered_answer,filepath=save_file_path)
        print('Saved action sequence to {}'.format(save_file_path))


    print("All action sequences are generated.")

