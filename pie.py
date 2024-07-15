#nlp_helper.py

import openai
from openai import OpenAI 
import os
from langchain_core.prompts.chat import ChatPromptTemplate

openai.api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI()
def get_git_command(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    command = response.choices[0].message.content.strip()
    if '```' in command:
        command = command.split('```')[1].strip()
    return command
#git_commands.py

import git

def execute_git_command(command: str):
    try:
        repo = git.Repo('.')  # Assumes you're running this in a Git repository
        result = repo.git.execute(command.split())
        return result
    except Exception as e:
        return str(e)




# cli.py
import click
from nlp_helper import get_git_command
from git_commands import execute_git_command
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@click.command()
@click.argument('input_text', nargs=-1)
def cli(input_text):
    prompt = " ".join(input_text)
    git_command = get_git_command(f"Translate this to a Git command: {prompt}")
    #click.echo(f"Executing: {git_command}")
    result = execute_git_command(git_command)
    #click.echo(result)

if __name__ == '__main__':
    cli()




#dockerfile

# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy only the poetry.lock and pyproject.toml files to the working directory
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the working directory
COPY . /app/

# Set the default command to run the CLI
CMD ["poetry", "run", "python", "cli.py"]



#docker-compose.yml

version: '3.7'

services:
  git-cli:
    build: .
    environment:
      - OPENAI_API_KEY
    volumes:
      - /Users/gaashdavid/git/GitCLI:/app
    working_dir: /app
    entrypoint: ["poetry", "run", "python", "cli.py"]



