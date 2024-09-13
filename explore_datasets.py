"""
Total number of turns: 333709
Average number of turns: 3.5446279674969463

"""
import json
DATASET_PATH="/home/tristan/benchmark_datasets/ShareGPT_V3_unfiltered_cleaned_split.json"
# load the dataset
with open(DATASET_PATH, 'r') as f:
    dataset = json.load(f)
    print(f"Loaded dataset from {DATASET_PATH}")
    print(f"Number of prompts: {len(dataset)}")
    print(f"Sample prompt: {dataset[2]}")

    total_turns = 0
    # compute how many turns in each prompt and the average number of turns
    for prompt in dataset:
        turns = len(prompt["conversations"]) // 2
        total_turns += turns
    print(f"Total number of turns: {total_turns}")
    print(f"Average number of turns: {total_turns / len(dataset)}")