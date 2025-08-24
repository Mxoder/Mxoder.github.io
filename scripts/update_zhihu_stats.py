# scripts/update_zhihu_stats.py

import os
import json
import requests
from loguru import logger

ZHIHU_USER_TOKEN = "mxode"  # 知乎用户 URL Token


def get_zhihu_stats():
    """
    通过知乎 API 获取用户的核心统计数据。
    """
    api_url = f"https://www.zhihu.com/api/v4/members/{ZHIHU_USER_TOKEN}?include=follower_count,favorited_count,voteup_count,thanked_count"

    # 从 Secrets 获取 Cookie
    zhihu_cookie = os.getenv("ZHIHU_COOKIE")
    if not zhihu_cookie:
        logger.error("未能从环境变量获取 ZHIHU_COOKIE，请求很可能会失败！")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Referer": f"https://www.zhihu.com/people/{ZHIHU_USER_TOKEN}",
        "Cookie": zhihu_cookie,  # 将 cookie 加入请求头
    }

    try:
        logger.info(f"正在从 API 获取数据: {api_url}")
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        data = response.json()
        logger.success("成功获取并解析知乎数据！")

        stats = {
            "followers": data.get("follower_count", 0),
            "favorites": data.get("favorited_count", 0),
            "voteups": data.get("voteup_count", 0),
            "thanks": data.get("thanked_count", 0),
        }
        return stats

    except requests.exceptions.RequestException as e:
        logger.error(f"请求知乎 API 时发生网络错误: {e}")
        logger.error(
            f"服务器返回内容: {response.text if 'response' in locals() else 'N/A'}"
        )
    except Exception as e:
        logger.error(f"处理数据时发生未知错误: {e}")

    # 如果任何环节出错，返回一组默认值
    return {"followers": 0, "favorites": 0, "voteups": 0, "thanks": 0}


def create_badge_json(label, message, color, file_path):
    """
    创建并保存一个符合 Shields.io endpoint 规范的 JSON 文件。
    """
    badge_data = {
        "schemaVersion": 1,
        "label": label,
        "message": str(message),
        "color": color,
    }

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(badge_data, f, indent=2, ensure_ascii=False)
        logger.info(f"成功生成徽章文件: {file_path}")
    except Exception as e:
        logger.error(f"保存文件 {file_path} 时发生错误: {e}")


if __name__ == "__main__":
    zhihu_stats = get_zhihu_stats()

    # 1. 为“关注者”创建徽章
    create_badge_json(
        label="Zhihu Followers",
        message=f"{zhihu_stats['followers']:,}",  # 使用千位分隔符
        color="blue",
        file_path="zhihu_followers_badge.json",
    )

    # 2. 为“赞同数”创建徽章
    create_badge_json(
        label="Zhihu Upvotes",
        message=f"{zhihu_stats['voteups']:,}",  # 使用千位分隔符
        color="green",
        file_path="zhihu_voteups_badge.json",
    )

    # 3. 为“收藏数”创建徽章
    create_badge_json(
        label="Zhihu Bookmarks",
        message=f"{zhihu_stats['favorites']:,}",  # 使用千位分隔符
        color="orange",
        file_path="zhihu_favorites_badge.json",
    )

    # 4. 为“感谢数”创建徽章
    create_badge_json(
        label="Zhihu Thanks",
        message=f"{zhihu_stats['thanks']:,}",  # 使用千位分隔符
        color="red",
        file_path="zhihu_thanks_badge.json",
    )
