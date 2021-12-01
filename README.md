# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                  | job_title                                                                                                                    | update_time   |
|---:|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [倫發科技有限公司](https://www.104.com.tw/company/1a2x6biyl9?jobsource=jolist_d_date)            | [開發運維工程師(Python) DevOps Engineer](https://www.104.com.tw/job/70v91?jobsource=jolist_d_date)                                  | 12/01         |
|  2 | [合翔資訊科技有限公司](https://www.104.com.tw/company/1a2x6blmxr?jobsource=jolist_d_date)          | [Python Backend 工程師](https://www.104.com.tw/job/7fif4?jobsource=jolist_d_date)                                               | 12/01         |
|  3 | [新加坡商蝦皮娛樂電商有限公司台灣分公司](https://www.104.com.tw/company/1a2x6blcz2?jobsource=jolist_d_date) | [Back-end Engineer Intern 後端工程師實習生 / Business Intelligence 數據分析部門](https://www.104.com.tw/job/7ecrl?jobsource=jolist_d_date) | 12/01         |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=jolist_d_relevance)     | [Python後端工程師](https://www.104.com.tw/job/76vbt?jobsource=jolist_d_relevance)                                                 | 11/29         |
|  5 | [普匯金融科技股份有限公司](https://www.104.com.tw/company/1a2x6bkhzg?jobsource=jolist_d_date)        | [python工程師](https://www.104.com.tw/job/7ark5?jobsource=jolist_d_date)                                                        | 12/01         |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)        | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=jolist_d_relevance)                                     | 11/30         |
|  7 | [雄獅資訊科技股份有限公司](https://www.104.com.tw/company/13kq7dpk?jobsource=jolist_d_date)          | [python工程師](https://www.104.com.tw/job/71rxc?jobsource=jolist_d_date)                                                        | 12/01         |

### Platform - 1111


|    | company                                                                          | job_title                                                          | update_time   |
|---:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------|
|  1 | [美超微電腦股份有限公司(Super Micro Computer, Inc.)](https://www.1111.com.tw/corp/9530088/) | [Software Engineer-TC21167](https://www.1111.com.tw/job/98544764/) | 2021-11-27    |

### Platform - CakeResume


|    | company                                                                      | job_title                                                                                                                           | update_time          |
|---:|:-----------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
|  1 | [A10 Networks 睿科網路科技有限公司](https://www.cakeresume.com/companies/a10-networks) | [Sr Full-Stack Web Developer](https://www.cakeresume.com/companies/a10-networks/jobs/full-stack-web-developer-1992f2)               | Updated 2 months ago |
|  2 | [Dr. Right 精準關懷 - 搶鏡創意股份有限公司](https://www.cakeresume.com/companies/dr-right) | [後端工程師 Backend Engineer](https://www.cakeresume.com/companies/dr-right/jobs/back-end-engineer-9098f2)                               | Updated 2 days ago   |
|  3 | [Proto Research Inc](https://www.cakeresume.com/companies/proto-cx)          | [Backend Developer (Python)](https://www.cakeresume.com/companies/proto-cx/jobs/backend-developer-python)                           | Updated 3 Months ago |
|  4 | [玉山商業銀行股份有限公司](https://www.cakeresume.com/companies/esunbank)                | [後端工程師 Back-end Enginee](https://www.cakeresume.com/companies/esunbank/jobs/back-end-enginee)                                       | Updated 5 days ago   |
|  5 | [瞬聯科技股份有限公司](https://www.cakeresume.com/companies/cienet)                    | [Cloud Service 軟體工程師](https://www.cakeresume.com/companies/cienet/jobs/cloud-service-software-engineer)                             | Updated 3 Months ago |
|  6 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)           | [Python Flask網站開發工程師(台北)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-web-development-engineer-taipei)   | Updated 3 Months ago |
|  7 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)           | [Python Flask網站研發工程師(台中)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-website-r-amp-d-engineer-taichung) | Updated 3 Months ago |
|  8 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                  | [Backend Developer (Junior & Senior)](https://www.cakeresume.com/companies/tsaitung/jobs/backend-developer-junior-senior)           | Updated 9 days ago   |



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
