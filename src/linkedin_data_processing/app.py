from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from linkedin_data_processing.agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from linkedin_data_processing.output_parsers import summary_parser
from third_parties.linkedin import scrape_linkedin_profile

def scrape_linkedin(name: str) -> str:
  linkedin_username = linkedin_lookup_agent(name=name)
  if linkedin_username:
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    summary_template = """
    Given the information {information} about a person from I want you to create:
    1. a short summary
    2. three interesting facts about them

    \n{format_instructions}
    """

    prompt = PromptTemplate(
      input_variables=["information"],
      template=summary_template,
      partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    chain = prompt | llm | summary_parser
    res = chain.invoke(input={"information": linkedin_data})

if __name__ == "__main__":
  scrape_linkedin(name="Jonathan Costa Prova Fácil")