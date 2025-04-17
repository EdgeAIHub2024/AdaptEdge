import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# 读取数据集
data = pd.read_csv("data/ad_data.csv")
X = pd.get_dummies(data[["age", "gender", "emotion"]])  # 转换为数值特征
y = data["ad_category"]

# 训练决策树
clf = DecisionTreeClassifier()
clf.fit(X, y)

# 保存模型
joblib.dump(clf, "models/ad_classifier.pkl")
print("模型已保存到 models/ad_classifier.pkl")