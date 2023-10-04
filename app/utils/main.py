from typing import Type, Union, TypeVar, Optional
from importlib import import_module


class ModelNotFound(Exception):
    pass


T = TypeVar('T')


def get_model_version(api_version: str, model_name: str) -> Union[Type[T], None]:
    """
    Get the specified model version, or fallback to the base version if the specified API version doesn't exist.

    Args:
        api_version (str): The API version (e.g., 'v1', 'v2').
        model_name (str): The name of the model.

    Returns:
        Union[Type[T], None]: The model class, or None if the model is not found.

    Raises:
        ModelNotFound: If the specified model version or the base version doesn't exist.
    """
    try:
        model_module = import_module(f'app.{api_version}.models.{model_name}')
        model_class = getattr(model_module, model_name)
        return model_class
    except ImportError:
        try:
            model_module = import_module(f'app.models.{model_name}')
            model_class = getattr(model_module, model_name)
            return model_class
        except ImportError:
            raise ModelNotFound(f"Model '{model_name}' not found in API version '{api_version}' or base version.")