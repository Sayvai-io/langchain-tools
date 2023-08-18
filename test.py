from llmserver import LlmServer
from rich import print as rprint

if __name__ == '__main__':
    server = LlmServer()
    server.initialize_agent(tools=["serpapi", "llm-math","wikipedia","terminal", "human"], agent="zero-shot-react-description")
    # server.initialize_llm()
    
    while True:
        inp = input('Enter your message: ')
        rprint(f'[bold purple] {server.get_response(inp)} [bold purple]')
        