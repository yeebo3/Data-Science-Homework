import re
from collections import deque
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from requests.exceptions import RequestException


START_URL = "https://www.hzau.edu.cn/"
MAX_PAGES = 50
HEADERS = {"User-Agent": "Mozilla/5.0"}
PAGE_SUFFIXES = (".htm", ".html", ".jsp", ".php", ".asp", ".aspx", ".shtml")


def is_page_path(path):
    if path in ("", "/"):
        return True
    lower_path = path.lower()
    if lower_path.endswith(PAGE_SUFFIXES):
        return True
    name = lower_path.rsplit("/", 1)[-1]
    if name == "vurl":
        return False
    return "." not in name


def normalize_url(base_url, link):
    url = urljoin(base_url, link)
    url, _ = urldefrag(url)
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return None
    if not parsed.netloc.endswith("hzau.edu.cn"):
        return None
    path = parsed.path or "/"
    if not is_page_path(path):
        return None
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def get_links(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.encoding = response.apparent_encoding
    except RequestException:
        return []
    links = []
    for link in re.findall(r'href=["\'](.*?)["\']', response.text, re.IGNORECASE):
        normalized = normalize_url(url, link)
        if normalized and normalized not in links:
            links.append(normalized)
    return links


def crawl_dfs(start_url, max_pages):
    visited = []
    seen = {start_url}
    stack = [start_url]
    while stack and len(visited) < max_pages:
        url = stack.pop()
        visited.append(url)
        links = get_links(url)
        for link in reversed(links):
            if link not in seen:
                seen.add(link)
                stack.append(link)
    return visited


def crawl_bfs(start_url, max_pages):
    visited = []
    seen = {start_url}
    queue = deque([start_url])
    while queue and len(visited) < max_pages:
        url = queue.popleft()
        visited.append(url)
        links = get_links(url)
        for link in links:
            if link not in seen:
                seen.add(link)
                queue.append(link)
    return visited


def print_result(name, urls):
    print(name)
    for index, url in enumerate(urls, 1):
        print(f"{index}. {url}")


if __name__ == "__main__":
    dfs_result = crawl_dfs(START_URL, MAX_PAGES)
    bfs_result = crawl_bfs(START_URL, MAX_PAGES)
    print_result("DFS", dfs_result)
    print_result("BFS", bfs_result)
