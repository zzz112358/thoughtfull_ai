import difflib

def find_best_match(user_question, qa_dataset, cutoff=0.5):
    """
    Find the most similar question in the dataset to the user's query.
    - Returns the corresponding answer if a match is found; otherwise, returns None.
    - For the current small dataset, another approach could be including the Q&A directly in the LLM prompt(not implemented since it's not scalable).
    - Using difflib here for demonstration purposes; if the knowledge base grows, consider switching to a vector database for better retrieval performance.
    """

    questions = [item["question"] for item in qa_dataset]
    matches = difflib.get_close_matches(user_question, questions, n=1, cutoff=cutoff)
    if matches:
        for item in qa_dataset:
            if item["question"] == matches[0]:
                return item["answer"]
    return None