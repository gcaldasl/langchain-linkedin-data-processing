from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from linkedin_data_processing.agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

def scrape_linkedin(name: str) -> str:
  linkedin_username = linkedin_lookup_agent(name=name)
  if linkedin_username:
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    summary_template = """
    Given the information {information} about a person from I want you to create:
    1. a short summary
    2. three interesting facts about them
    """

    prompt = PromptTemplate(
      input_variables=["information"],
      template=summary_template
    )

    chain = prompt | llm

    res = chain.invoke(input={"information": linkedin_data})

    print(res.content)

if __name__ == "__main__":
  scrape_linkedin(name="Jonathan Costa Prova Fácil")