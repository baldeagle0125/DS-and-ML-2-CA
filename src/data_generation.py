# Author: Ihor Melashchenko
# Student ID: C00290950

"""Synthetic dataset generation utilities for semester 2 portfolio notebooks."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class DatasetConfig:
    """Configuration for synthetic student engagement data generation."""

    n_students: int = 600
    random_seed: int = 42


def generate_student_dataset(config: DatasetConfig = DatasetConfig()) -> pd.DataFrame:
    """Create a synthetic dataset with behavioral and academic engagement signals."""
    rng = np.random.default_rng(config.random_seed)
    n = config.n_students

    weekly_logins = np.clip(rng.normal(loc=9, scale=3, size=n), 1, None)
    avg_session_minutes = np.clip(rng.normal(loc=18, scale=6, size=n), 3, None)
    timetable_views = np.clip(rng.normal(loc=16, scale=6, size=n), 0, None)
    notification_click_rate = np.clip(rng.beta(a=2.5, b=3.0, size=n), 0.01, 0.99)
    attendance_rate = np.clip(rng.normal(loc=0.82, scale=0.12, size=n), 0.35, 1.0)
    assignment_submission_rate = np.clip(rng.normal(loc=0.78, scale=0.16, size=n), 0.25, 1.0)
    gpa = np.clip(rng.normal(loc=2.7, scale=0.7, size=n), 0.8, 4.0)

    engagement_score = (
        0.22 * (weekly_logins / np.max(weekly_logins))
        + 0.16 * (avg_session_minutes / np.max(avg_session_minutes))
        + 0.12 * (timetable_views / np.max(timetable_views))
        + 0.10 * notification_click_rate
        + 0.20 * attendance_rate
        + 0.20 * assignment_submission_rate
    )

    dropout_risk_prob = np.clip(1.05 - (0.9 * engagement_score + 0.25 * (gpa / 4.0)), 0.02, 0.98)
    dropout_risk = rng.binomial(n=1, p=dropout_risk_prob)

    return pd.DataFrame(
        {
            "weekly_logins": weekly_logins.round(2),
            "avg_session_minutes": avg_session_minutes.round(2),
            "timetable_views": timetable_views.round(2),
            "notification_click_rate": notification_click_rate.round(3),
            "attendance_rate": attendance_rate.round(3),
            "assignment_submission_rate": assignment_submission_rate.round(3),
            "gpa": gpa.round(2),
            "engagement_score": engagement_score.round(3),
            "dropout_risk": dropout_risk,
        }
    )


def save_dataset(path: str, config: DatasetConfig = DatasetConfig()) -> None:
    """Generate and save dataset as CSV to the given path."""
    df = generate_student_dataset(config=config)
    df.to_csv(path, index=False)
