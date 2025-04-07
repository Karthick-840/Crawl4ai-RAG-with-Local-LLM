from settings import parse_arguments,process_urls_argument,create_filename_from_url, setup_logger
from AI_web_scrapping import Crawl4aiWebScraper
import os

if __name__ == "__main__":

    #urls = ["https://langchain-ai.github.io/langgraph","https://docs.smith.langchain.com/","https://python.langchain.com/","https://ai.pydantic.dev/","https://docs.crawl4ai.com/","https://www.llamaindex.ai/"]
 
    args = parse_arguments()
    url = process_urls_argument(args.url)
    url_mapping = {u: create_filename_from_url(u) for u in url}
    get_all_pages = args.get_all_pages

    main_log_statement = f"\nParsed Arguments (from settings.py):\n Task at hand:  URL: {url_mapping} combinations will be saved in respective .MD files where we Get all sub pages is {get_all_pages}"

    check_requirements = Crawl4aiWebScraper.verify_dependencies()
    if check_requirements[0]:
        for url, filename in url_mapping.items():
            logger = setup_logger(filename)
            logger.info(main_log_statement)
            logger.info(f"Crawl4AI dependencies CHECK:{check_requirements}")
            logger.info(f"Now processing: {url} to be saved to {filename}")
            scraper = Crawl4aiWebScraper(url,filename,get_all_page=get_all_pages, logger=logger)
            scraper.web_to_markdown()
            logger.info("Script finished.")
    