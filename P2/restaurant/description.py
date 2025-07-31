# pip install pandas
import pandas as pd     # Importing pandas for data manipulation
df = pd.read_csv('restaurant_reviews.csv')

def generate_description(row):
    name = row['ID']

    def generate_desc_from_score(score):
        if score < 20: return f"매우 나쁩니다({score}점)."
        elif score < 40: return f"나쁩니다({score}점)."
        elif score < 60: return f"보통입니다({score}점)."
        elif score < 80: return f"좋습니다({score}점)."
        else: return f"매우 좋습니다({score}점)."

    description = f"{name}의 리뷰는 다음과 같습니다.\n"
    description += f"- 음식 평점은 {generate_desc_from_score(row['Taste'])}\n"
    description += f"- 분위기 평점은 {generate_desc_from_score(row['Ambiance'])}\n"
    description += f"- 서비스 평점은 {generate_desc_from_score(row['Service'])}\n"
    description += f"- 메뉴 다양성 평점은 {generate_desc_from_score(row['Menu_variety'])}\n"
    description += f"- 위생 평점은 {generate_desc_from_score(row['Hygienic'])}\n"
    description += f"- 가격 대비 가치는 {'높습니다.' if row['Worth_the_price'] == 'yes' else '낮습니다.'}\n"
    description += f"- 비건 옵션이 {'있습니다.' if row['Vegan_options'] == 'yes' else '없습니다.'}\n"
    description += f"- 흡연 구역이 {'있습니다.' if row['Smoking_area'] == 'yes' else '없습니다.'}\n"
    description += f"- 주차장이 {'있습니다.' if row['Parking'] == 'yes' else '없습니다.'}\n"
    description += f"- 반려동물 동반 가능{'합니다.' if row['Pet_friendly'] == 'yes' else '하지 않습니다.'}\n"

    return description

# apply the function to each row and create a new column
df['Description'] = df.apply(generate_description, axis=1)
df.to_csv('restaurant_reviews_with_descriptions.csv', index=False)
