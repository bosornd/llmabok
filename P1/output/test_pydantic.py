from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(description="사용자의 이름")
    age: int = Field(description="사용자의 나이", gt=0) # > 0으로 설정, 양수만 허용

User(name="Alice", age="30")  # age는 int로 변환됨
User(name="Bob", age=-5)      # ValidationError 발생, age는 양수여야 함
