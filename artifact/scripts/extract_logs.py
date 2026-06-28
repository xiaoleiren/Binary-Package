#!/usr/bin/env python3
"""
Extract CTFd logs into template format.

Usage:
    python3 extract_logs.py --ctfd-url http://localhost:8000 --api-key KEY --output ../data/
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

# Assume pandas is installed
try:
    import pandas as pd
except ImportError:
    print("pandas is required. Run: pip3 install pandas")
    sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser(description="Extract CTFd logs to CSV")
    parser.add_argument("--ctfd-url", required=True, help="CTFd instance URL")
    parser.add_argument("--api-key", required=True, help="CTFd admin API key")
    parser.add_argument("--output", default="../data/", help="Output directory")
    return parser.parse_args()

def extract_attempts(ctfd_url, api_key):
    """
    Fetch all submissions from CTFd and format as lab summary.
    This is a stub; replace with actual CTFd API calls.
    """
    # In practice, this would call CTFd API:
    # GET /api/v1/submissions?type=correct&count=1000
    # GET /api/v1/submissions?type=incorrect&count=1000

    # Placeholder data structure
    return {
        "Lab1": {"attempts": 2.8, "first_correct": 15, "total_submissions": 41},
        "Lab2": {"attempts": 3.6, "first_correct": 13, "total_submissions": 40},
        "Lab3": {"attempts": 3.3, "first_correct": 14, "total_submissions": 41},
        "Lab4": {"attempts": 8.2, "first_correct": 7, "total_submissions": 38},
    }

def generate_lab_summary(data, output_path):
    """Generate lab_summary_template.csv"""
    rows = []
    for lab, stats in data.items():
        rows.append({
            "lab_id": lab,
            "enrolled": 43,
            "submitted": stats["total_submissions"],
            "full_count": 0,  # Replace with actual data
            "full_percent": 0,
            "partial_count": 0,
            "partial_percent": 0,
            "no_submit_count": 43 - stats["total_submissions"],
            "no_submit_percent": 0,
            "mean_attempts": stats["attempts"],
            "median_attempts": 0,
            "max_attempts": 0,
            "mean_minutes": 0,
            "median_minutes": 0,
            "min_minutes": 0,
            "max_minutes": 0,
            "total_hint_clicks": 0,
            "students_using_hints_percent": 0,
        })

    df = pd.DataFrame(rows)
    df.to_csv(Path(output_path) / "lab_summary_template.csv", index=False)
    print(f"Generated lab_summary_template.csv")

def main():
    args = parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    data = extract_attempts(args.ctfd_url, args.api_key)
    generate_lab_summary(data, output_dir)

if __name__ == "__main__":
    main()