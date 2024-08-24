#!/bin/bash

# Makefile

# Configuration
#MODEL="facebook/opt-125m"
#MODEL=facebook/opt-350m
#MODEL="facebook/opt-1.3b"
MODEL="facebook/opt-2.7b"
DATASET_PATH="/home/tristan/benchmark_datasets/ShareGPT_V3_unfiltered_cleaned_split.json"
NUM_PROMPTS=20
REPEAT_COUNT=10
INPUT_LENGTH_RANGE="128:256"

# Target: run-cache
run-cache:
	python benchmark_prefix_caching.py \
	            --model $(MODEL) \
		            --dataset-path $(DATASET_PATH) \
			            --enable-prefix-caching \
				            --num-prompts $(NUM_PROMPTS) \
					            --repeat-count $(REPEAT_COUNT) \
						            --input-length-range $(INPUT_LENGTH_RANGE)
# Target: run-nocache
run-nocache:
	python benchmark_prefix_caching.py \
		        --model $(MODEL) \
			        --dataset-path $(DATASET_PATH) \
				        --num-prompts $(NUM_PROMPTS) \
					        --repeat-count $(REPEAT_COUNT) \
						        --input-length-range $(INPUT_LENGTH_RANGE)

