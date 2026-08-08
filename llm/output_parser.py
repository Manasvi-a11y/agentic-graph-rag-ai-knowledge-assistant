class OutputParser:

    def format(self, result):

        answer = result["answer"]

        sources = result["sources"]

        output = answer

        if sources:

            output += "\n\nSources:\n"

            for source in sources:

                output += f"- {source}\n"

        return output