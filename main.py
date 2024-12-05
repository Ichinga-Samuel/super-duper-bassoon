from typing import Self
from os import environ

from dotenv import load_dotenv, dotenv_values


class Config:
    _instance: Self

    # you can add type hints here if you want
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    my_secret: str
    my_constant: float

    def __new__(cls, *args, **kwargs):
        if getattr(cls, '_instance', None) is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.load_dotenv(**kwargs)
            cls._initialized = True
            return cls._instance

        cls._instance.set_attributes(**kwargs)
        return cls._instance

    def __getattr__(self, item):
        attr = environ.get(item)
        setattr(self, item, attr) if attr is not None else None
        return attr

    def set_attributes(self, **kwargs):
        [setattr(self, key, value) for key, value in kwargs.items()]

    def load_dotenv(self,**kwargs):
        params = ["dotenv_path", "stream", "verbose", "override", "interpolate", "encoding"]
        params = {key: kwargs.pop(key) for key in params if key in kwargs}
        load_dotenv(**params)
        values = kwargs | dotenv_values()
        self.set_attributes(**values)


env = Config(my_constant=3.14)
print(env.AWS_ACCESS_KEY_ID, env.AWS_SECRET_ACCESS_KEY, env.my_secret, env.my_constant, env.PATH)
