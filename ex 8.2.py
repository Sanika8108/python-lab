import re

def moderate_feedback(feedback, target_words):
    """
    Replace each target word in a feedback block with ***.

    Matching is case-insensitive and only replaces whole words.
    """
    if not target_words:
        return feedback

    # Escape words so regex characters in the target list are treated literally.
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in target_words) + r')\b'

    return re.sub(pattern, '***', feedback, flags=re.IGNORECASE)


# Example
feedback = """
The product is great, but the delivery was terrible.
The support team was rude and the service was awful.
"""

target_words = [
    "terrible",
    "rude",
    "awful"
]

filtered_feedback = moderate_feedback(feedback, target_words)

print(filtered_feedback)
