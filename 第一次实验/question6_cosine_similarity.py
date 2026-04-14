import math


topic_weights = {
    "大数据": 1,
    "存储": 1,
    "采集": 1,
    "挖掘": 1,
    "特征": 1,
    "爬虫": 1,
    "平台": 1,
    "分布式": 1,
}

doc_weights = {
    "大数据": 1,
    "爬虫": 1,
    "采集": 1,
    "技术": 1,
}


def cosine_similarity(vector_a, vector_b):
    keys = set(vector_a) | set(vector_b)
    dot = 0
    norm_a = 0
    norm_b = 0
    for key in keys:
        a = vector_a.get(key, 0)
        b = vector_b.get(key, 0)
        dot += a * b
        norm_a += a * a
        norm_b += b * b
    return dot / (math.sqrt(norm_a) * math.sqrt(norm_b))


print(cosine_similarity(topic_weights, doc_weights))
