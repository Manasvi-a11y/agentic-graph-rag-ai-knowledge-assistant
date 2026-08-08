from retrieval.retriever import Retriever
from llm.generator import LLMGenerator
from llm.output_parser import OutputParser

retriever = Retriever()

generator = LLMGenerator()

parser = OutputParser()

docs = retriever.retrieve(

    "Explain LangChain"

)

result = generator.generate(

    "Explain LangChain",

    docs

)

print(

    parser.format(result)

)