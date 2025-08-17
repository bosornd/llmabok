import dotenv
dotenv.load_dotenv()

from enum import Enum
class Color(Enum):
    RED    = "빨강"
    BLUE   = "파랑"
    YELLOW = "노랑"

from langchain.output_parsers import EnumOutputParser
output_parser = EnumOutputParser(enum=Color)
