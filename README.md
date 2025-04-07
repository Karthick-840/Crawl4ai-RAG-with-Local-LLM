# 🧠 Local LLM Knowledge Expansion with Crawl4AI 🚀

Local Large Language Models are missing the latest insights. 🧐 This little side quest tackles that head-on!

The goal here is to create a streamlined process for fetching up-to-date documentation from the web and use open-source embedding models to create Vector Database. Think of it as giving your local models a continuous knowledge boost! 💪

For Instance, I imparted **[PydanticAI](https://ai.pydantic.dev/)** documentation as RAG for my locally running **[StarCoder: A State-of-the-Art LLM for Code ](https://huggingface.co/blog/starcoder)** to do some cool **"vibe coding"** 🎶

The core of the web scraping process relies on **[Crawl4AI](https://github.com/unclecode/crawl4ai)**,🕷️. While I didn't build it myself, an impressive open-source framework to work with for LLM applications... 🤓

**Workflow**

1.  **Scrapes relevant documentation:** 
    - Provide a list of URLs (preferably start pages). 
    - It then uses `sitemap.xml` to get all URLS of the webpage and saves them as `.md` files.
    - Always respect the `robots.txt` best practices. *[Soon will be added]*

2.  **Enables embedding creation:** 
    - These Markdown files can then be used to build knowledge embeddings for Retrieval-Augmented Generation (RAG) applications, 
    - [IBM Granite-Embedding](https://www.ibm.com/granite/docs/models/embedding/) is used as it works sufficiently for many use-cases.
    - Interact in terminal within Ollama Framework like **[Gemma3](https://blog.google/technology/developers/gemma-3/)** model.
    ```bash
    ollama serve
    ollama run gemma3
    ```

**Installation: 🛠️**

1. *As a package📦*
    - Use `Poetry` for dependency management by refering to the `pyproject.toml`.
    ```bash
    poetry install
    poetry shell
    ```
    - Alternatively, install via `requirements.txt` file:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    pip install -r requirements.txt
    pip install .
    ```
2. *Running with Docker 🐳*

Navigate to the directory containing the `Dockerfile` and build the Docker image for a more isolated and reproducible running environment:

        ```bash
        docker build -t crawl4ai-doc-scraper .
        ```

**Running the Documentation Scraper ⚙️**

Once you have the environment set up (either locally or via Docker), you can run the `main.py` script to start scraping.

The script accepts the following arguments:

* `url_list`: A list of URLs to scrape documentation from.
* `-g get_all_pages true`: This flag tells Crawl4AI to crawl and scrape all sub-pages found on the initial URLs. If set to `false`, only the content of the initial URLs or start page will be scraped.

**Example Usage:**

```bash
# Local execution (after activating the virtual environment)
python3 main.py "[https://langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph)" "[https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)" -g true

# Docker execution (as shown in the Docker installation step)
docker run crawl4ai-doc-scraper python3 main.py --url "[https://langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph)" "[https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)" -g true
```




## License 📜

This project utilizes the MIT License. You are free to use, modify, and distribute it according to the terms of this license. See the `LICENSE` file for the full text.

## Contributing and Future Improvements 🌱

While this is a personal side quest, feel free to reach out if you have ideas or suggestions! Future improvements could include:

* More sophisticated content filtering during scraping.
* Automated embedding generation after scraping.
* Integration with specific local LLM workflows.

## Conclusion 🎉

This setup demonstrates a practical approach to keeping local LLMs informed with the latest web documentation. By leveraging the power of Crawl4AI and creating a consistent environment, we can enhance our learning, coding, and exploration with local AI models. Happy exploring! 🗺️