# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                        | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:--------------|
|  1 | [伊諾科技有限公司](https://www.104.com.tw/company/1a2x6bkxph?jobsource=2018indexpoc)                | [(真摯徵求) Python後端工程師](https://www.104.com.tw/job/70asp?jobsource=2018indexpoc)                    | 7/08          |
|  2 | [同步科技股份有限公司](https://www.104.com.tw/company/1a2x6ble88?jobsource=2018indexpoc)              | [後端工程師](https://www.104.com.tw/job/76q8x?jobsource=2018indexpoc)                                 | 6/24          |
|  3 | [德義資訊股份有限公司](https://www.104.com.tw/company/oe84aqo?jobsource=2018indexpoc)                 | [Backend 系統開發工程師](https://www.104.com.tw/job/7awmz?jobsource=2018indexpoc)                       | 7/06          |
|  4 | [易勝資訊股份有限公司](https://www.104.com.tw/company/1a2x6bj8og?jobsource=2018indexpoc)              | [Python後端開發工程師(DevOps整合平台)](https://www.104.com.tw/job/7asvo?jobsource=2018indexpoc)             | 7/08          |
|  5 | [米約科技有限公司](https://www.104.com.tw/company/1a2x6bl97m?jobsource=2018indexpoc)                | [Python工程師](https://www.104.com.tw/job/6zey2?jobsource=2018indexpoc)                             | 7/08          |
|  6 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=2018indexpoc)                 | [Python Flask網站研發工程師(台中)](https://www.104.com.tw/job/6kf9h?jobsource=2018indexpoc)               | 6/28          |
|  7 | [英屬開曼群島商萬里雲互聯股份有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bk5cu?jobsource=2018indexpoc) | [Solution Architect (Presales) 解決方案架構師](https://www.104.com.tw/job/6c62k?jobsource=2018indexpoc) | 7/08          |
|  8 | [華翰物產實業股份有限公司](https://www.104.com.tw/company/10xb8hsw?jobsource=2018indexpoc)              | [資深資料科學家(Senior Data Scientist)](https://www.104.com.tw/job/72vx2?jobsource=2018indexpoc)        | 7/08          |
|  9 | [萊鎂醫療器材股份有限公司](https://www.104.com.tw/company/bkgh1dc?jobsource=2018indexpoc)               | [雲端應用工程師](https://www.104.com.tw/job/791cq?jobsource=2018indexpoc)                               | 6/30          |

### Platform - 1111


|    | company                                              | job_title                                          | update_time   |
|---:|:-----------------------------------------------------|:---------------------------------------------------|:--------------|
|  1 | [億力資訊股份有限公司](https://www.1111.com.tw/corp/54937860/) | [python工程師](https://www.1111.com.tw/job/97374762/) | 2021-07-06    |
|  2 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/)     | 2021-07-06    |

### Platform - CakeResume


|    | company                                                                               | job_title                                                                                                                           | update_time          |
|---:|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
|  1 | [Cathay Financial Holdings 國泰金控](https://www.cakeresume.com/companies/cathayholdings) | [軟體開發工程師 Python Software Engineer(數數發中心, DDT)](https://www.cakeresume.com/companies/cathayholdings/jobs/f5c69a)                     | Updated 3 Months ago |
|  2 | [Proto Research Inc](https://www.cakeresume.com/companies/proto-cx)                   | [Backend Developer (Python)](https://www.cakeresume.com/companies/proto-cx/jobs/backend-developer-python)                           | Updated 4 days ago   |
|  3 | [玉山商業銀行股份有限公司](https://www.cakeresume.com/companies/esunbank)                         | [後端工程師 Back-end Enginee](https://www.cakeresume.com/companies/esunbank/jobs/back-end-enginee)                                       | Updated 3 Months ago |
|  4 | [瞬聯科技股份有限公司](https://www.cakeresume.com/companies/cienet)                             | [Cloud Service 軟體工程師](https://www.cakeresume.com/companies/cienet/jobs/cloud-service-software-engineer)                             | Updated 3 Months ago |
|  5 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站開發工程師(台北)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-web-development-engineer-taipei)   | Updated 3 Months ago |
|  6 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站研發工程師(台中)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-website-r-amp-d-engineer-taichung) | Updated 3 Months ago |
|  7 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [Backend Developer (Junior & Senior)](https://www.cakeresume.com/companies/tsaitung/jobs/backend-developer-junior-senior)           | Updated a day ago    |



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
