"""Create `Person` class and save 5 random people to JSON.

Usage:
    python module2/saeed_module2_4.py

This will create a `people.json` file next to this module containing
5 randomly generated people with fields: name, number, location, job_title.
"""
from dataclasses import dataclass, asdict
import json
import os
import random
from typing import List


@dataclass
class Person:
    name: str
    number: str
    location: str
    job_title: str


def _sample_phone() -> str:
    # generate a simple 10-digit phone number string
    return f"+1{random.randint(200_000_0000, 999_999_9999)}"


def generate_random_people(n: int = 5) -> List[Person]:
    names = [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve",
        "Frank",
        "Grace",
        "Hank",
        "Ivy",
        "Jack",
    ]
    locations = ["New York", "London", "Paris", "Berlin", "Tokyo", "Sydney"]
    jobs = [
        "Software Engineer",
        "Data Analyst",
        "Product Manager",
        "Designer",
        "QA Engineer",
        "System Administrator",
    ]

    people: List[Person] = []
    for _ in range(n):
        person = Person(
            name=random.choice(names),
            number=_sample_phone(),
            location=random.choice(locations),
            job_title=random.choice(jobs),
        )
        people.append(person)
    return people


def save_people_json(people: List[Person], path: str | None = None) -> str:
    """Save list of Person to JSON file. Returns the file path.

    If `path` is None, writes to `people.json` in the same directory as this file.
    """
    if path is None:
        base = os.path.dirname(__file__)
        path = os.path.join(base, "people.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(p) for p in people], f, ensure_ascii=False, indent=2)

    return path



    people = generate_random_people(5)
    out_path = save_people_json(people)
    print(f"Wrote {len(people)} people to {out_path}")
