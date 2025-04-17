import pandas as pd
import random

# 定义特征和标签的取值
ages = ["20-30", "30-40", "40-50", "50+"]
genders = ["男", "女"]
emotions = ["开心", "平静", "难过"]
ad_categories = [
    "时尚产品_运动风格_正能量广告",
    "实用产品_优雅风格_正能量广告",
    "高端产品_运动风格_治愈广告",
    "时尚产品_优雅风格_常规广告",
    "实用产品_简约风格_常规广告",
    "高端产品_优雅风格_治愈广告"
]

# 简单的推荐逻辑
def assign_ad_category(age, gender, emotion):
    if age == "20-30" and emotion == "开心":
        return "时尚产品_运动风格_正能量广告" if gender == "男" else "时尚产品_优雅风格_正能量广告"
    elif age == "30-40" and emotion == "开心":
        return "实用产品_优雅风格_正能量广告" if gender == "女" else "实用产品_简约风格_常规广告"
    elif age == "40-50" and emotion == "难过":
        return "高端产品_运动风格_治愈广告" if gender == "男" else "高端产品_优雅风格_治愈广告"
    elif age == "50+":
        return "高端产品_简约风格_正能量广告" if emotion == "开心" else "高端产品_优雅风格_治愈广告"
    else:
        return random.choice(ad_categories)

# 生成 100 行数据
data = []
for _ in range(100):
    age = random.choice(ages)
    gender = random.choice(genders)
    emotion = random.choice(emotions)
    ad_category = assign_ad_category(age, gender, emotion)
    data.append([age, gender, emotion, ad_category])

# 保存为 CSV
df = pd.DataFrame(data, columns=["age", "gender", "emotion", "ad_category"])
df.to_csv("data/ad_data.csv", index=False)
print("训练数据已保存到 data/ad_data.csv")