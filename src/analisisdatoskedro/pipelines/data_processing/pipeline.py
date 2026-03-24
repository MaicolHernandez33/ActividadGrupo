from kedro.pipeline import Node, Pipeline

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            Node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            Node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            Node(
                func=create_model_input_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )

from .nodes import combine_players
from kedro.pipeline import Pipeline, node

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=combine_players,
            inputs=[
                "players_15",
                "players_16",
                "players_17",
                "players_18",
                "players_19",
                "players_20",
            ],
            outputs="players_all",
            name="combine_players_node",
        ),
    ])

