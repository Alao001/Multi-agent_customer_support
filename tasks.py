from crewai import Task
from tools import docs_scrape_tool
from agents import support_agent, support_quality_assurance_agent







inquiry_resolution = Task(
    description=(
        "{customer} just reached out with a super important ask:\n"
	    "{inquiry}\n\n"
        "{customer} from {company} is the one that reached out. "
        "Leverage all your knowledge to provide the best possible support." 
        "Your response must be comprehensive, accurate,"
        "you must only answer questions related to your company" 
        "and address all aspects of the query."
		"Make sure to use everything you know "
    ),
    expected_output=(
        "A detailed and informative response that fully addresses the customer's query." 
        "Include references to any external sources or solutions used" 
        "Ensure the response is complete and leaves no unanswered questions." 
        "Maintain a helpful and friendly tone throughout."
    ),
	tools=[docs_scrape_tool],
    agent=support_agent,
)

quality_assurance_review = Task(
    description=(
        "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
        "Ensure that the answer is comprehensive, accurate, and adheres to the "
		"high-quality standards expected for customer support.\n"
        "Verify that all parts of the customer's inquiry "
        "have been addressed "
		"thoroughly, with a helpful and friendly tone.\n"
        "Check for references and sources used to "
        " find the information, "
		"ensuring the response is well-supported and "
        "make sure the answers provided is related to the company"
        "leaves no questions unanswered."
    ),
    expected_output=(
        "A final, detailed, and informative response "
        "ready to be sent to the customer.\n"
        "This response should fully address the "
        "customer's inquiry, incorporating all "
		"relevant feedback and improvements.\n"
		"Don't be too formal, we are a chill and cool company "
	    "but maintain a professional and friendly tone throughout."
    ),
    agent=support_quality_assurance_agent,
)