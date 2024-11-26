from crewai_tools import ScrapeWebsiteTool
                         
                         
docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://huggingface.co/docs/hub/index"
)                        