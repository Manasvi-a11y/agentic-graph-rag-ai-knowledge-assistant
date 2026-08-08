import re

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from config import settings
from llm.prompt import SYSTEM_PROMPT


class LLMGenerator:

    def __init__(self):

        self.llm = ChatGroq(

            api_key=settings.GROQ_API_KEY,

            model=settings.GROQ_MODEL,

            temperature=0

        )

    def generate(self, query, documents, history=None):

        context = ""

        sources = set()

        for doc in documents:

            if hasattr(doc, "page_content"):

                context += doc.page_content + "\n\n"

                if "filename" in doc.metadata:

                    sources.add(doc.metadata["filename"])

        history_text = ""

        if history:
            history_lines = []
            for message in history:
                sender = message.get("sender")
                text = message.get("text")
                if sender is not None and text is not None:
                    history_lines.append(f"{sender.capitalize()}: {text}")
            history_text = "\n".join(history_lines)

        prompt = ChatPromptTemplate.from_messages(

            [

                ("system", SYSTEM_PROMPT),

                (

                    "human",

                    """

Conversation History:

{history}

Context:

{context}

Question:

{question}

"""

                )

            ]

        )

        chain = prompt | self.llm

        answer = chain.invoke(

            {

                "history": history_text,

                "context": context,

                "question": query

            }

        )

        cleaned_answer = re.sub(
            r"(?m)^[ \t]*(Source:.*|Note:.*)\s*$",
            "",
            answer.content,
        )
        cleaned_answer = re.sub(r"\n{2,}", "\n\n", cleaned_answer).strip()

        return {

            "answer": cleaned_answer,

            "sources": list(sources)

        }