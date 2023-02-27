import random
import string

import pytest

from mafia_allocation import Allocator


@pytest.fixture
def allocator() -> Allocator:
    random_list = [
        "".join(random.choices(string.ascii_letters, k=random.randint(3, 8)))
        for _ in range(10)
    ]
    return Allocator(random_list, "test")
