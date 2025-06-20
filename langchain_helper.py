import os

from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureOpenAI, AzureChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("OPENAI_API_BASE"),
        openai_api_version=os.getenv("OPENAI_API_VERSION"),
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        deployment_name="gpt-4o",
        temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet, {pet_color} in color, and I want a cool name for it. "
                 "Suggest me five cool names for my pet. Only list the names without additional explanations or numbering."
                 "(1., 2., 3., ...) without any extra explanation."
    )

    name_chain = prompt_template_name | llm

    response = name_chain.invoke({'animal_type': animal_type, 'pet_color': pet_color}).content

    # # Split the comma-separated names to get a clean list
    # names = [name.strip() for name in response.split(",")]

    return response

if __name__ == "__main__":
    print(generate_pet_name("cat", "black"))