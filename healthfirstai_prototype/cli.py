from healthfirstai_prototype.generate import get_user_meal_plans
from healthfirstai_prototype.nutrition_agent import start_json_agent
from healthfirstai_prototype.transform import (
    delete_all_vectors,
    get_all_foods,
    insert_all_vectors,
)

import click


@click.group()
def cli():
    pass


@cli.command()
def get_meal_plan():
    """
    Get a meal plan from the database
    """
    click.echo("Getting meal plan")
    meal_plan = get_user_meal_plans(1)  # NOTE: We are getting the meal plan for user 1
    click.echo(meal_plan)
    click.echo("Finished search")


@cli.command()
def test_json_agent():
    """
    Tests the JSON agent to answer questions about a meal plan
    """
    click.echo("Getting meal plan")
    meal_plan_json = get_user_meal_plans(1)
    click.echo("Starting agent")
    agent = start_json_agent(meal_plan_json)
    click.echo("Running agent")

    user_input = "What are the ingredients in my dinner?"
    click.echo(f"User Input: {user_input}")
    output = agent.run(user_input)
    click.echo(f"Output: {output}")

    user_input = "What is the protein content of my dinner?"  # NOTE: JSON currently does not contain macro + micro values
    click.echo(f"User Input: {user_input}")
    output = agent.run(user_input)
    click.echo(f"Output: {output}")

    user_input = "Please edit the above JSON object so that you replace the protein bar with something less sweet but equally protein rich"  # NOTE: Limited to reading the JSON file. We will likely go for another agent
    click.echo(f"User Input: {user_input}")
    output = agent.run(user_input)
    click.echo(f"Output: {output}")

    click.echo("Finished search")


@cli.command()
def reinsert_vectors():
    """
    Delete all vectors in nutrition_vectors and insert new vectors
    """
    click.echo("Reinserting nutrition vectors")
    delete_all_vectors()
    click.echo("Deleted all old vectors")
    foods = get_all_foods()
    click.echo("Queried and got all foods")
    insert_all_vectors(foods)
    click.echo("Inserted new food vectors")
    click.echo("Finished search")


if __name__ == "__main__":
    cli()
