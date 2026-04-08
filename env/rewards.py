from __future__ import annotations


def compute_reward(action_type: str, context: dict) -> float:
    """
    Intermediate reward shaping.
    Final episode reward comes from the grader (called at submit).
    """
    if action_type == "fill_missing":
        filled = context.get("filled", 0)
        return round(min(0.08 * filled, 0.30), 4)

    if action_type == "standardize_values":
        replaced = context.get("replaced", 0)
        return round(min(0.06 * replaced, 0.25), 4)

    if action_type == "remove_duplicates":
        removed = context.get("removed", 0)
        return round(min(0.15 * removed, 0.30), 4)

    if action_type == "remove_row":
        return 0.05

    if action_type == "convert_type":
        return 0.15

    if action_type == "clip_outliers":
        clipped = context.get("clipped", 0)
        return round(min(0.10 * max(clipped, 1), 0.30), 4)

    return 0.0
