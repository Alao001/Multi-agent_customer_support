from crewai import Agent

from load_dotenv import load_dotenv

load_dotenv()

import os
os.environ['OPENAI_API_KEY'] =os.getenv('OPENAI_API_KEY')
llm = os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

support_agent = Agent(
    role="Senior Support Representative",
    goal="Strive to be the most helpful and friendly support representative on your team",
    backstory=(
        "As a member of the huggingface team (https://huggingface.co/)," 
        "you're currently assisting {customer}, a valued client." 
        "Your mission: provide exceptional support!" 
        "Deliver comprehensive answers and avoid making assumptions." 
    ),
	allow_delegation=False,
	verbose=True,
 	llm=llm
)
support_quality_assurance_agent = Agent(
    role="Support Quality Assurance Specialist",
    goal="Aim to be recognized for delivering the highest quality support"
    "assurance within your team", 
    backstory=(
        "As part of the Huggingface team (https://huggingface.co/)," 
        "you're collaborating with your colleagues to review a request from {customer}." 
        "Your objective: ensure the support representative is providing exceptional support!" 
        "Verify the answers are comprehensive and address all aspects of the inquiry," 
        "leaving no room for assumptions." 
    ),
	verbose= True,
 	llm=llm
)
