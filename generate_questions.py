import argparse
import os
import pickle
import re
from openai import OpenAI
import base64
import mimetypes
import io
from PIL import Image
import httpx
import json
import ast
import time
import openai


def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def local_image_to_data_url(path):
    img = Image.open(path).convert("RGB")
    img.thumbnail((512, 512))

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)

    data = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{data}"


def qwen(api_key, prompt, image_url_list):
    try:
        # 初始化OpenAI客户端
        client = OpenAI(
            # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
            # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
            api_key=api_key,
            # 以下是北京地域base_url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            http_client=httpx.Client(timeout=120.0)
        )

        multimodal_content = []

        multimodal_content.append({
            "type": "text", "text": prompt
        })

        for idx, image_url in enumerate(image_url_list):
            image_path = os.path.join(image_file, image_url)
            image_url = local_image_to_data_url(image_path)
            multimodal_content.append({
                "type": "image_url",
                "image_url": image_url,
            })
            multimodal_content.append({
                "type": "text",
                "text": f"Label: {idx + 1}"
            })

        messages = [{
            "role": "user",
            "content": multimodal_content,
        }]

        reasoning_content = ""  # 定义完整思考过程
        answer_content = ""  # 定义完整回复
        is_answering = False  # 判断是否结束思考过程并开始回复
        enable_thinking = True
        # 创建聊天完成请求
        completion = client.chat.completions.create(
            model="qwen3-vl-plus",
            messages=messages,
            stream=True,
            # enable_thinking 参数开启思考过程，thinking_budget 参数设置最大推理过程 Token 数
            # qwen3-vl-plus、 qwen3-vl-flash可通过enable_thinking开启或关闭思考、对于qwen3-vl-235b-a22b-thinking等带thinking后缀的模型，enable_thinking仅支持设置为开启，对其他Qwen-VL模型均不适用
            extra_body={
                'enable_thinking': enable_thinking},

            # 解除以下注释会在最后一个chunk返回Token使用量
            # stream_options={
            #     "include_usage": True
            # }
        )

        if enable_thinking:
            print("\n" + "=" * 20 + "思考过程" + "=" * 20 + "\n")

        for chunk in completion:
            # 如果chunk.choices为空，则打印usage
            if not chunk.choices:
                print("\nUsage:")
                print(chunk.usage)
            else:
                delta = chunk.choices[0].delta
                # 打印思考过程
                if hasattr(delta, 'reasoning_content') and delta.reasoning_content != None:
                    print(delta.reasoning_content, end='', flush=True)
                    reasoning_content += delta.reasoning_content
                else:
                    # 开始回复
                    if delta.content != "" and is_answering is False:
                        print("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")
                        is_answering = True
                    # 打印回复过程
                    print(delta.content, end='', flush=True)
                    answer_content += delta.content
        return answer_content, reasoning_content
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")


def gpt(api_key,
        prompt,
        image_url_list,
        image_file,
        model,
        max_output_tokens=512,
        temperature=0):
    time.sleep(5)  # time sleep to avoid speed limit
    client = OpenAI(api_key=api_key)
    content = [{"type": "input_text", "text": prompt}]

    for img_name in image_url_list:
        path = os.path.join(image_file, img_name)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image not found: {path}")
        encoded = encode_image(path)

        content.append({
            "type": "input_image",
            "image_url": f"data:image/png;base64,{encoded}"
        })

    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "user",
                "content": content
            }
        ],
        max_output_tokens=max_output_tokens,
        temperature=temperature
    )

    try:
        output_text = response.output_text

    except AttributeError:
        # fallback for safety
        output_text = response.output[0].content[0].text
    return output_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # root path
    action_sequence_root_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/action_sequence/'
    image_map_root_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/action_observation_map/'
    dependency_root_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/action_dependency/'
    image_root_path = '/Users/rampage/PycharmProjects/Simulators/ENACT/data/segmented_activities/'

    results = []

    task_names = os.listdir(action_sequence_root_path)

    for task_name in task_names:
        # load action list
        action_sequence_file_path = os.path.join(action_sequence_root_path, task_name)
        action_list_file_path = os.path.join(action_sequence_file_path, 'action_sequence.pkl')
        with open(action_list_file_path, 'rb') as file:
            # Use pickle.load() to read the list from the file
            action_list = pickle.load(file)
        print(f"successfully load the action sequence from {task_name}")


        # load action image map
        try:
            image_map_file_path = os.path.join(image_map_root_path, task_name)
            with open(os.path.join(image_map_file_path,"action_sequence.json"), 'rb') as json_file:
                action_image_map = json.load(json_file)
            print(f"successfully load the action image mapping from {task_name}")
        except FileNotFoundError:
            print(f"cannot find the action observation map from {task_name}. Skipping.")
            continue

        # load action dependency
        action_dependency_file_path = os.path.join(dependency_root_path, task_name)
        try:
            with open(os.path.join(action_dependency_file_path,"action_dependency.json"), 'rb') as json_file:
                action_dependency = json.load(json_file)
            print(f"successfully load the action dependency from {task_name}")
        except FileNotFoundError:
            print(f"cannot find the action dependency from {task_name}. Skipping.")
            continue

        # load image
        image_file = os.path.join(os.path.join(image_root_path, task_name),'external_sensor1')
        image_url_list = [] # A list for generate questions

        # {image_name_1: 1, image_name_2: 2}
        image_name_map = {}
        index = 1
        for action, image_list in action_image_map.items():
            if len(image_list) > 0:
                for image in image_list:
                    if image not in image_name_map:
                        image_name_map[image] = index
                        index += 1
                        image_url_list.append(image)

        def idx_to_image_name(idx):
            """
            Turn image index in the question to the original image name
            :param idx:
            :return:
            """
            image_name  = next((k for k, v in image_name_map.items() if v == idx), None)
            return image_name

        def image_name_to_idx(image_name):
            """
            Turn image name into corresponding image index
            :param image_name:
            :return:
            """
            return image_name_map[image_name]


        # select the most dependent action as key actions:
        action_dependency_count = {}
        for (action, dependency_list) in action_dependency.items():
            for dependency in dependency_list:
                if dependency not in action_dependency_count:
                    action_dependency_count[dependency] = 1
                else:
                    action_dependency_count[dependency] += 1

        # select the most dependended actions
        # selected_actions = [max(action_dependency_count, key=action_dependency_count.get)]
        selected_actions = [action for action in action_dependency_count if action_dependency_count[action] >= 1]
        print(f"selected actions: {selected_actions}")
        # traverse all the selected actions
        for action in selected_actions:
            if action_image_map[action] ==[]:
                print("The chosen action does not have any corresponding images")
                continue
            # Get the test image names
            test_images = action_image_map[action]
            # Get the test image index
            test_images_idx = [image_name_to_idx(image) for image in test_images]
            # test_images = [20, 21]

            answer_actions = [a for a in action_dependency if action in action_dependency[a]]
            answer_observation = [action_image_map[a] for a in answer_actions]

            system_prompt="""
            You are proficient at action relation understanding and I need you to identify the direct causal relation of a given actions. I will
            show you the vision observations while performing a sequence of actions in order.
            I need you to choose the actions that directly depend on the target action.
            You will receive a list of images with number and your should return the number of observations corresponding to the causal related actions.
            """


            # template to identify dependency of the future actions
            prompt = f"""
            "You are a capable agent designed to infer causal relationship in multi-step embodied decision-making. 
            Your goal is to predict the direct causal-dependent actions of a specific action from a given series of actions in egocentric-view observations. In short, you will need to identify the actions which would be failed if the target action is missing in the sequence.\n\n
            The **Visual Observations** is already in execution order and their labels are (1, 2, 3, etc).\n\n
            ## Your Task\n
            You will be provided with a sequence of **Visual Observations** of an agent completing a specific task.  Each image is extracted in the order of the action sequence.(labeled 1, 2, 3, etc.) **Target Images** Target images will be given and you need to identify the action in the target images. To extract the images of causal-related actions, you must follow the sequence of actions provided below.\n\n
            1.  Understand the action of each **Visual Observations**.\n
            2.  Identify the **Target Action** of the **Target Images** from the **Visual Observations**. Remember, an action could have multiple target images which are extracted during action execution. If multiple target images are given, the target action should be identified by combining the images in order.\n
            3.  Find the direct causal-dependent actions related to the  **Target Action**. **You should identify the actions that would be failed if the target action is missing**.  For example, if the target action is "open the cabinet", then action "grasp object_A inside the cabinet" is directly causal-dependent on the target action. But the following action, such as "slice object_A" is not directly causal-related to "open the cabinet"\n
            4.  Next, identify all the images corresponding to the direct causal-dependent actions.\n
            5.  Return all the image labels. You can return an empty list if you think no actions are directly dependent on the target action.\n
            ## Output Format\nYour response **must be only** a Python list of integers representing the correct direct causal-dependent image labels. Do not include any other text, reasoning, or explanation.\n\n
            **Example:** If you determine the direct causal-dependent images are "image_1", "image_2", "image_3", your output must be:\n
            `[1, 2, 3]`\n\n
            You can output as many labels as there are direct causal-related actions.\n
            Target Images: {test_images_idx}
            Now please provide your answer in the requested format.\n
            """

            # template to predict what would happen given the missing steps
            template = f"""
            "You are a capable agent designed to infer causal relationship in multi-step embodied decision-making. 
            Your goal is to predict the direct causal-dependent actions of a specific action from a given series of actions in egocentric-view observations. In short, you will need to what would be affected if the target action is missing in the sequence.\n\n
            The **Visual Observations** is already in execution order and their labels are (1, 2, 3, etc).\n\n
            ## Your Task\n
            You will be provided with a sequence of **Visual Observations** of an agent completing a specific task.  Each image is extracted in the order of the action sequence.(labeled 1, 2, 3, etc.) **Target Images** Target images will be given and you need to identify the action in the target images. To extract the images of causal-related actions, you must follow the sequence of actions provided below.\n\n
            1.  Understand the action of each **Visual Observations**.\n
            2.  Identify the **Target Action** of the **Target Images** from the **Visual Observations**. Remember, an action could have multiple target images which are extracted during action execution. If multiple target images are given, the target action should be identified by combining the images in order.\n
            3.  Reason of what would happen if the **Target Action** is missing in this action series. **You should identify the actions that would be affected if the target action is missing**.  For example, if the target action is "open the cabinet", then action "grasp object_A inside the cabinet" would be failed because the door is still close.\n
            ## Output Format\nYour response **must be only** a Python list of index representing the observations of the affected actions. Also provide a reason.\n\n
            **Example:** If you determine the affected actions' observations are "image_1", "image_2", "image_3", your output must be:\n
            `index:[1, 2, 3]\n
             reason:"reason to explain what would happen if the target action is missing in this action series"`\n
            Target Images: {test_images_idx}
            Now please provide your answer in the requested format.\n
            """

            # for i in range(5):
            #     try:
            #         answer = gpt(
            #             api_key='',
            #             prompt=prompt,
            #             image_file=image_file,
            #             image_url_list=image_url_list,
            #             model='gpt-4o-mini',
            #             max_output_tokens=512,)
            #         answer = answer.replace('`', '').replace('python', '').replace('\n','')
            #         answer  = answer.lstrip().rstrip()
            #         if not answer.endswith(']'):
            #             answer += ']'
            #         answer = ast.literal_eval(answer)
            #         print(answer)
            #         break
            #     except:
            #         print(f"Rate limit hit, retrying in {5}s...")
            #         time.sleep(5)
            #
            # results.append({
            #             "task_name":task_name,
            #             "target_action": action,
            #             "answer": answer,
            #             "answer_url":[idx_to_image_name(int(ans)) for ans in answer],
            #             "expected_answer":answer_observation,
            #             "model":"gpt-40-mini",
            #         })

            answer, reason = qwen("", prompt, image_url_list)
            answer = ast.literal_eval(answer)

            results.append({
                "task_name":task_name,
                "target_action": action,
                "answer": answer,
                "answer_url":[idx_to_image_name(int(ans)) for ans in answer],
                "expected_answer":answer_observation,
                "model":"qwen3-vl-plus",
                "reason":reason
            })

            print("answer:", answer)
            print("selected action name: " , action)
            print("test images label: ", test_images_idx)
            print("test images original label:", test_images)
            print("expected answer:", answer_observation)
            print("model answer: ", [idx_to_image_name(int(ans)) for ans in answer] )
    #
    with open(os.path.join('./results', 'missing_key_steps_results_qwen_3_vl_plus_all.json'), 'w') as json_file:
        json.dump(results, json_file, indent=4)
