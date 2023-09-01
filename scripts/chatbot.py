import openai
import textwrap
from rich import print
from rich.console import Console
from rich.text import Text

openai.api_key = "EMPTY"
openai.api_base = "http://127.0.0.1:8080/v1"
console = Console()

MAX_WIDTH = 80  # Set maximum characters per line

def chat_prompt(user_input: str) -> str:
    return (
        'You\'re an AI assistant, respond politely and honestly to the USER.\n'
        'Only write one AI response.\n'
        f'USER: {user_input}\n'
        'AI: '
    )

def wrap_text(text, width=MAX_WIDTH, color=None):
    """Wrap text to the specified width."""
    wrapped_text = textwrap.fill(text, width)
    return f"[{color}]{wrapped_text}[/{color}]"


first_input = '''
Below is a simple SQL schema consisting of two tables: employees and departments. Your task is to write an SQL query that satisfies the given requirement.

-- employees table
CREATE TABLE employees (
  id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  salary INT,
  department_id INT
);

-- departments table
CREATE TABLE departments (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);

-- Sample data in employees table
INSERT INTO employees (id, first_name, last_name, salary, department_id) VALUES
(1, 'John', 'Doe', 60000, 1),
(2, 'Jane', 'Doe', 70000, 2),
(3, 'Sally', 'Smith', 50000, 3),
(4, 'Bill', 'Gates', 80000, 1),
(5, 'Elon', 'Musk', 90000, 2);

-- Sample data in departments table
INSERT INTO departments (id, name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Finance');

Requirement:
Write an SQL query to fetch the first_name, last_name, and salary of all employees who work in the "Engineering" department, sorted by salary in descending order.

Please provide the SQL query that fulfills this requirement. Write only the SQL Statements, nothing else.

SQL Statements: 
'''


while True:
    # Use rich to print the User's prompt in blue
    if first_input:
        user_input = first_input
    else:
        console.print("[blue]USER: [/blue]", end="")
        user_input = input()
    
    
    # Exit condition if user types 'exit'
    if user_input.lower() == 'exit':
        break
    
    completion = openai.Completion.create(
        model="../aila-llama2-13b-hf",
        prompt=chat_prompt(user_input),
        max_tokens=2048,
    )
    
    # Use rich to make the AI's response green and wrap it
    # ai_response = wrap_text(completion['choices'][0]['text'].strip(), color="green")
    ai_response = completion['choices'][0]['text'].strip()
    print(f"[red]AILA:[/red] {ai_response}")

    first_input = None

print("[yellow]Goodbye![/yellow]")
