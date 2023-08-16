from llmserver import LlmServer
from rich import print as rprint

if __name__ == '__main__':
    server = LlmServer()
    server.initialize(tools=["serpapi", "llm-math","wikipedia","terminal"], agent="zero-shot-react-description")
    
    while True:
        inp = input('Enter your message: ')
        rprint(f'[bold purple] {server.get_response(inp)} [bold purple]')
        