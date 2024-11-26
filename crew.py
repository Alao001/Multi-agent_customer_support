from crewai import Crew
from agents import support_agent, support_quality_assurance_agent
from tasks import inquiry_resolution, quality_assurance_review

crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=True,
  memory=True,
)

