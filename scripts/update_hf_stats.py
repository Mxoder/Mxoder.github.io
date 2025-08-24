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
        return 0


def save_stats_to_file(total_downloads, total_likes):
    """
    保存统计数据。
    """
    # data_dir = "_data"    # 保存到 Jekyll 的 _data 目录中
    data_dir = "."
    file_path = os.path.join(data_dir, "hf_stats.json")

    try:
        # os.makedirs(data_dir, exist_ok=True)  # 根目录总会存在

        with open(file_path, "w") as f:
            json.dump(
                {"total_downloads": total_downloads, "total_likes": total_likes},
                f,
                indent=2,
            )

        logger.info(f"数据已成功保存到 {file_path}")
    except Exception as e:
        logger.error(f"保存数据到文件时发生错误: {e}")


if __name__ == "__main__":
    total_downloads, total_likes = get_total_downloads_and_likes()
    save_stats_to_file(total_downloads, total_likes)
