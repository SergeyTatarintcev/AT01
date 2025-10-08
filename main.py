def count_vowels(text):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for ch in text if ch in vowels)