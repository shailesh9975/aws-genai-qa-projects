# utils/scoring.py

def evaluate_output(prompt, output):
    """
    Evaluate the model output for the given prompt.
    Returns a score as float.
    """
    expected = prompt.get('expected_answer')
    if expected and expected in output:
        return 1.0
    return 0.5

