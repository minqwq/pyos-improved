import requests
from tqdm import tqdm

def download_file_with_progress(url, file_name):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(file_name, 'wb') as file, tqdm(
        desc=file_name,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))
    print(f'Download complete as: {file_name}')

# 示例用法
print("fileget by copilot(AI)")
url = input("Example:https://www.minqwq.us.kg/pyosimproved/news/latest.txt\nFile location on that server: ")
file_name = input("Save this file as what name?: ")
download_file_with_progress(url, file_name)