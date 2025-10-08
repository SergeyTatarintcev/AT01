import pytest
from main import count_vowels

@pytest.mark.parametrize("text, expected", [
    ("аеёиоуыэюя", 10),          # только гласные
    ("бвгджзйклмнпрстфхцчшщ", 0), # только согласные
    ("Привет, Мир!", 3),          # смешанные + прописные
    ("Hello World", 3),           # латиница
    ("", 0),                      # пустая строка
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected