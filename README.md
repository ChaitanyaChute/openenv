---
title: Data Cleaning OpenEnv Benchmark
emoji: 🧹
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
tags:
  - openenv
---

# 🧹 Data Cleaning OpenEnv Benchmark

A multi-task benchmark where LLM agents clean real-world messy tabular datasets using a structured action API.

## Why This Matters

Data cleaning consumes 60–80 % of analyst time in practice. This benchmark evaluates whether LLM agents can autonomously detect and fix data quality issues such as duplicates, missing values, format inconsistencies, and outliers without human guidance.

## Tasks

| ID | Difficulty | Description |
|----|-----------|-------------|
| `task1_easy` | Easy | Remove exact duplicates, fill missing emails and ages, standardise country names |
| `task2_medium` | Medium | Normalise mixed date formats, convert price strings to float, fix category typos |
| `task3_hard` | Hard | Resolve duplicate user IDs, clip session outliers, fix invalid bounce rates |

Each task is independently graded on a `0.0–1.0` scale with partial credit.

## Action Space

| Action | Required Fields |
|--------|----------------|
| `fill_missing` | `column`, `strategy` (`mean`/`median`/`mode`/`constant`), `value` when needed |
| `standardize_values` | `column`, `mapping` |
| `remove_duplicates` | None |
| `remove_row` | `row_id` |
| `convert_type` | `column`, `target_type` |
| `clip_outliers` | `column`, `lower`, `upper` |
| `submit` | None |

## Observation Space

Each step the agent receives `table_preview`, `schema_info`, `issues_detected`, `cleaning_log`, `valid_actions`, `step`, and `max_steps`.

## Reward Design

Correct cleaning actions receive positive intermediate rewards, wasted actions receive small penalties, invalid actions receive a larger penalty, and `submit` returns the final grader score.

## Setup & Local Run

```bash
git clone https://huggingface.co/spaces/AnkushRaheja/data-cleaning-benchmark
cd data-cleaning-benchmark
pip install -r requirements.txt
uvicorn app:app --port 7860
```

## Run Baseline

```bash
export API_BASE_URL="https://api.groq.com/openai/v1"
export MODEL_NAME="meta-llama/llama-4-scout-17b-16e-instruct"
export HF_TOKEN="$GROQ_API_KEY"
export TASK_ID="task1_easy"
python inference.py
```

## Docker

```bash
docker build -t data-cleaning-benchmark .
docker run -p 7860:7860 \
  -e API_BASE_URL="https://api.groq.com/openai/v1" \
  -e MODEL_NAME="meta-llama/llama-4-scout-17b-16e-instruct" \
  -e HF_TOKEN="$GROQ_API_KEY" \
  data-cleaning-benchmark
```

## Baseline Scores

| Task | Score |
|------|-------|
| task1_easy | 0.99 |
| task2_medium | 0.90 |
| task3_hard | 0.97 |

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/reset` | Start new episode `{"task_id": "task1_easy"}` |
| POST | `/step/{session_id}` | Submit action and receive reward |
| GET | `/state/{session_id}` | Full internal state |
| GET | `/tasks` | List all tasks |
