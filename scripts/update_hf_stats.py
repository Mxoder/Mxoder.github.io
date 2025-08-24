# scripts/update_hf_stats.py

import os
import json
from huggingface_hub import HfApi
from loguru import logger

HF_USERNAME = "Mxode"


def get_total_downloads_and_likes():
    """
    获取指定 Hugging Face 用户的所有模型和数据集的总下载量和总点赞量。
    """
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        logger.warning("HF_TOKEN 环境变量未设置，将以非认证模式运行。")
        logger.warning("这可能导致无法获取到正确的下载数据。")

    try:
        api = HfApi(token=hf_token)

        # 获取所有模型信息
        models = api.list_models(
            author=HF_USERNAME, expand=["downloadsAllTime", "likes"]
        )
        model_downloads, model_likes = 0, 0
        for model in models:
            model_downloads += model.downloads_all_time
            model_likes += model.likes
        logger.info(f"用户 '{HF_USERNAME}' 的模型总下载量: {model_downloads}")
        logger.info(f"用户 '{HF_USERNAME}' 的模型总点赞量: {model_likes}")

        # 获取所有数据集信息
        datasets = api.list_datasets(
            author=HF_USERNAME, expand=["downloadsAllTime", "likes"]
        )
        dataset_downloads, dataset_likes = 0, 0
        for dataset in datasets:
            dataset_downloads += dataset.downloads_all_time
            dataset_likes += dataset.likes
        logger.info(f"用户 '{HF_USERNAME}' 的数据集总下载量: {dataset_downloads}")
        logger.info(f"用户 '{HF_USERNAME}' 的数据集总点赞量: {dataset_likes}")

        total_downloads = model_downloads + dataset_downloads
        logger.success(f"计算出的总下载量为: {total_downloads}")

        total_likes = model_likes + dataset_likes
        logger.success(f"计算出的总点赞量为: {total_likes}")

        return total_downloads, total_likes
    except Exception as e:
        logger.error(f"从 Hugging Face API 获取数据时发生错误: {e}")
        return 0, 0


def create_badge_json(label, message, color, file_path):
    """
    创建并保存一个符合 Shields.io endpoint 规范的 JSON 文件。
    """
    badge_data = {
        "schemaVersion": 1,
        "label": label,
        "message": str(message),  # message 必须是字符串
        "color": color,
    }

    try:
        with open(file_path, "w") as f:
            json.dump(badge_data, f, indent=2)
        logger.info(f"成功生成徽章文件: {file_path}")
    except Exception as e:
        logger.error(f"保存文件 {file_path} 时发生错误: {e}")


if __name__ == "__main__":
    total_downloads, total_likes = get_total_downloads_and_likes()

    # 为下载量创建一个徽章 JSON
    create_badge_json(
        label="HF Downloads",
        message=f"{total_downloads:,}",     # 使用千位分隔符
        color="blue",
        file_path="hf_downloads_badge.json",
    )

    # 为点赞数创建一个徽章 JSON
    create_badge_json(
        label="HF Likes",
        message=f"{total_likes:,}",         # 使用千位分隔符
        color="yellow",
        file_path="hf_likes_badge.json",
    )
