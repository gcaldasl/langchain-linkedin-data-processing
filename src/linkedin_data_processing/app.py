from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile

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
linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/gcaldasl/", mock=True)

res = chain.invoke(input={"information": linkedin_data})

print(res)