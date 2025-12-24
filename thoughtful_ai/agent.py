from knowledge_base.knowledge import AGENT_QA
from knowledge_base.retrieval import find_best_match
from clients.openai_client import call_openai

class ThoughtfulAIAgent:
    def __init__(self, qa_dataset=AGENT_QA):
        self.qa_dataset = qa_dataset

    def get_response(self, user_question):
        answer = find_best_match(user_question, self.qa_dataset)
        if answer:
            return answer
        """
        Fallback to OpenAI if no results are found as requested.
        Personally, I don't think we should call OpenAI yet, since it only provides free ChatGPT
        unless we refine the prompt carefully.
        """
        return call_openai(user_question)