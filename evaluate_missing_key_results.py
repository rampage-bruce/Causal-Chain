import json
import numpy as np

def evaluate_actions_k_verbose(answer, expected_actions, k=0.5):
    answer_set = set(answer)

    # ---- Flatten expected actions into a set ----
    expected_set = set()
    for action in expected_actions:
        expected_set.update(action)

    # ---- Precision (string-level) ----
    overlap = answer_set & expected_set
    precision = len(overlap) / len(answer_set) if len(answer_set) > 0 else 0.0

    # ---- k-existence (action-level) ----
    existed_count = 0
    not_existed_count = 0

    for action in expected_actions:
        if len(action) == 0:
            continue

        match_count = sum(1 for s in action if s in answer_set)
        ratio = match_count / len(action)

        if ratio >= k:
            existed_count += 1
        else:
            not_existed_count += 1

    return {
        "precision": precision,
        "overlap_count": len(overlap),
        "answer_count": len(answer_set),
        "existed_actions": existed_count,
        "not_existed_actions": not_existed_count
    }

if __name__ == "__main__":
    # Load the stored results

    file_name = "results/missing_key_steps_results_gpt4o_mini.json"
    with open(file_name) as json_file:
        data = json.load(json_file)


    results_statistics = []

    for task in data:
        print(task)
        correct_cnt = 0
        missing_cnt = 0
        answers = task["answer_url"]
        # answers = set(answers)
        task_name = task["task_name"]

        ground_truth = task["expected_answer"]

        report = evaluate_actions_k_verbose(answers, ground_truth, 1.0)
        results_statistics.append({"task_name": task_name,
                                   "precision": report["precision"],
                                   "overlap_count": report["overlap_count"],
                                   "answer_count": report["answer_count"],
                                   "existed_actions": report["existed_actions"],
                                   "not_existed_actions": report["not_existed_actions"]
                                   })
        # for action in ground_truth:
        #     if any(s in answers for s in action):
        #         correct_cnt+=1
        #     else:
        #         missing_cnt+=1
        #
        # results_statistics[task_name] = {"correct": correct_cnt, "missing": missing_cnt}
    total_recall = 0
    total_precision = 0
    for result in results_statistics:
        precision = result["precision"]
        print(result)
        recall  = result["existed_actions"]/(result["existed_actions"]+result["not_existed_actions"])
        total_recall += recall
        total_precision += precision
    print("overall recall: ", total_recall/len(results_statistics))
    print("overall precision: ", total_precision/len(results_statistics))



