from src.parser.pdf_parser import extract_text_from_pdf
from src.agent.controller import run_agent
from src.learning.trainer import learning_loop

text = extract_text_from_pdf("data/sample.pdf")

score = learning_loop(run_agent, text)

print("Learning Score:", score)
