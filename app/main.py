from dotenv import load_dotenv
import os
from src.export_files import create_tables

from llama_parse import LlamaParse

load_dotenv()


documents = LlamaParse(
    result_type="markdown",
    parsing_instruction="This document contains text and tables, I'd like to get just the tables from the text.",
).load_data(r"data\resultado.pdf")


for i, page in enumerate(documents):
    with open(fr"data\page{i+1}.md", "w", encoding="utf-8") as f:
        f.write(page.text)

create_tables()