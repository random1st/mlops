import requests
import multiprocessing as mp

def parse_url(url):
    data = requests.get(url).json()
    print(data)
    return data


def main():
    url = "https://api.ipify.org?format=json"
    try:
        data = parse_url(url)
        print(f"Your IP address is: {data['ip']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import time
    start = time.time()

    pool = mp.Pool(processes=10)
    urls = ["https://api.ipify.org?format=json"] * 20

    results = pool.map(parse_url, urls)

    pool.close()
    pool.join()


    print(f"Execution time: {time.time() - start:.2f} seconds")