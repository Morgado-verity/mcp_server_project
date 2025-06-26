from typing import Callable

def tool(name: str, input_model: type, output_model: type):
    def decorator(func: Callable):
        func._tool_info = {
            "name": name,
            "description": func.__doc__ or "",
            "input_model": input_model,
            "output_model": output_model,
        }
        return func
    return decorator
