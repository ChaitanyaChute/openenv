import pytest

from env.environment import DataCleaningEnv


def test_reset_default():
    env = DataCleaningEnv()
    obs = env.reset()
    assert obs.task_id == "task1_easy"
    assert obs.step == 0
    assert obs.max_steps == 20
    assert len(obs.table_preview.rows) > 0
    assert "remove_duplicates" in obs.valid_actions


def test_reset_task2():
    env = DataCleaningEnv()
    obs = env.reset(task_id="task2_medium")
    assert obs.task_id == "task2_medium"
    assert obs.step == 0


def test_reset_task3():
    env = DataCleaningEnv()
    obs = env.reset(task_id="task3_hard")
    assert obs.task_id == "task3_hard"


def test_reset_unknown_task():
    env = DataCleaningEnv()
    with pytest.raises(ValueError):
        env.reset(task_id="nonexistent_task")


def test_issues_detected_on_reset():
    env = DataCleaningEnv()
    obs = env.reset(task_id="task1_easy")
    assert len(obs.issues_detected) > 0
