# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                               | job_title                                                                                | update_time   |
|---:|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|:--------------|
|  1 | [思納捷科技股份有限公司](https://www.104.com.tw/company/1a2x6bk977?jobsource=jolist_c_relevance) | [前端工程師(Python)](https://www.104.com.tw/job/7g8nn?jobsource=jolist_c_relevance)           | 11/19         |
|  2 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_c_relevance)  | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_c_relevance)             | 11/29         |
|  3 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_c_relevance)     | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_c_relevance) | 11/30         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-12-02    |

### Platform - CakeResume


|    | company                                                                      | job_title                                                                                                                           | update_time          |
|---:|:-----------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
|  1 | [A10 Networks 睿科網路科技有限公司](https://www.cakeresume.com/companies/a10-networks) | [Sr Full-Stack Web Developer](https://www.cakeresume.com/companies/a10-networks/jobs/full-stack-web-developer-1992f2)               | Updated 2 months ago |
|  2 | [Dr. Right 精準關懷 - 搶鏡創意股份有限公司](https://www.cakeresume.com/companies/dr-right) | [後端工程師 Backend Engineer](https://www.cakeresume.com/companies/dr-right/jobs/back-end-engineer-9098f2)                               | Updated 3 days ago   |
|  3 | [Proto Research Inc](https://www.cakeresume.com/companies/proto-cx)          | [Backend Developer (Python)](https://www.cakeresume.com/companies/proto-cx/jobs/backend-developer-python)                           | Updated 3 Months ago |
|  4 | [玉山商業銀行股份有限公司](https://www.cakeresume.com/companies/esunbank)                | [後端工程師 Back-end Enginee](https://www.cakeresume.com/companies/esunbank/jobs/back-end-enginee)                                       | Updated 6 days ago   |
|  5 | [瞬聯科技股份有限公司](https://www.cakeresume.com/companies/cienet)                    | [Cloud Service 軟體工程師](https://www.cakeresume.com/companies/cienet/jobs/cloud-service-software-engineer)                             | Updated 3 Months ago |
|  6 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)           | [Python Flask網站開發工程師(台北)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-web-development-engineer-taipei)   | Updated 3 Months ago |
|  7 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)           | [Python Flask網站研發工程師(台中)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-website-r-amp-d-engineer-taichung) | Updated 3 Months ago |
|  8 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                  | [Backend Developer (Junior & Senior)](https://www.cakeresume.com/companies/tsaitung/jobs/backend-developer-junior-senior)           | Updated 10 days ago  |



# Getting started
## Setup Development Environment
▍Method 1 - Python Built-in venv

- Create your virtual environment
```
$ python3 -m venv venv
```
- And enable virtual environment
```
$ . venv/bin/activate
```
- Install requirements
```
$ pip install -r requirements.txt 
```

▍Method 2 - Poetry
- Install requirements
```
$ poetry install
```
- And enable virtual environment
```
$ poetry shell
```

## Setup Keyword & Run

Setup Your Keyword in [main.py](./main.py#L88)
```
if __name__ == "__main__":
    keyword = "flask"
    crawler = JobCrawler(keyword)
    crawler.run()
```

Run Crawler
```
$ python3 main.py
```

# Contributors
PRs are welcome!

This project exists thanks to all the people who contribute.

<a href="https://github.com/hsuanchi/auto-search-flask-job/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hsuanchi/auto-search-flask-job"/>
</a>
