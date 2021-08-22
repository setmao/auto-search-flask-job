# Auto searching jobs

## Jobs include `flask` in Taiwan 

 ![image](./doc/plot_img.jpg)


### Platform - 104


|    | company                                                                                     | job_title                                                                                                    | update_time   |
|---:|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|:--------------|
|  1 | [吉音資訊有限公司](https://www.104.com.tw/company/10uhacsw?jobsource=jolist_d_relevance)            | [高薪徵PHP程式開發人才(專案聘請 2-3年職(視情況再延長 ;Cable或電信業))](https://www.104.com.tw/job/2j2kp?jobsource=jolist_d_relevance) | 8/12          |
|  2 | [新加坡商威兆科技有限公司台灣分公司](https://www.104.com.tw/company/1a2x6bjqez?jobsource=jolist_d_relevance) | [Junior IT Developer (助理 IT 程式設計師)](https://www.104.com.tw/job/7bely?jobsource=jolist_d_relevance)           | 7/15          |
|  3 | [漢康生技股份有限公司](https://www.104.com.tw/company/1a2x6blf97?jobsource=jolist_d_relevance)        | [細胞培養工藝開發研究員/副研究員/助理研究員](https://www.104.com.tw/job/7cccb?jobsource=jolist_d_relevance)                      | 8/17          |
|  4 | [紅門互動股份有限公司](https://www.104.com.tw/company/oh4m67k?jobsource=jolist_d_relevance)           | [Python Flask網站開發工程師(台北)](https://www.104.com.tw/job/6xtfl?jobsource=jolist_d_relevance)                     | 8/18          |
|  5 | [萊泀有限公司](https://www.104.com.tw/company/1a2x6blg3t?jobsource=jolist_d_relevance)            | [Python (Django、Flask)程式設計師](https://www.104.com.tw/job/7cs5e?jobsource=jolist_d_relevance)                  | 8/16          |

### Platform - 1111


|    | company                                              | job_title                                      | update_time   |
|---:|:-----------------------------------------------------|:-----------------------------------------------|:--------------|
|  1 | [長青資訊股份有限公司](https://www.1111.com.tw/corp/71694811/) | [後端工程師](https://www.1111.com.tw/job/85012186/) | 2021-08-20    |

### Platform - CakeResume


|    | company                                                                               | job_title                                                                                                                           | update_time          |
|---:|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|:---------------------|
|  1 | [Cathay Financial Holdings 國泰金控](https://www.cakeresume.com/companies/cathayholdings) | [軟體開發工程師 Python Software Engineer(數數發中心, DDT)](https://www.cakeresume.com/companies/cathayholdings/jobs/f5c69a)                     | Updated a month ago  |
|  2 | [Proto Research Inc](https://www.cakeresume.com/companies/proto-cx)                   | [Backend Developer (Python)](https://www.cakeresume.com/companies/proto-cx/jobs/backend-developer-python)                           | Updated a month ago  |
|  3 | [玉山商業銀行股份有限公司](https://www.cakeresume.com/companies/esunbank)                         | [後端工程師 Back-end Enginee](https://www.cakeresume.com/companies/esunbank/jobs/back-end-enginee)                                       | Updated 12 days ago  |
|  4 | [瞬聯科技股份有限公司](https://www.cakeresume.com/companies/cienet)                             | [Cloud Service 軟體工程師](https://www.cakeresume.com/companies/cienet/jobs/cloud-service-software-engineer)                             | Updated 3 Months ago |
|  5 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站開發工程師(台北)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-web-development-engineer-taipei)   | Updated 3 Months ago |
|  6 | [紅門互動股份有限公司](https://www.cakeresume.com/companies/eagleeye-5332f1)                    | [Python Flask網站研發工程師(台中)](https://www.cakeresume.com/companies/eagleeye-5332f1/jobs/python-flask-website-r-amp-d-engineer-taichung) | Updated 3 Months ago |
|  7 | [菜蟲農食股份有限公司](https://www.cakeresume.com/companies/tsaitung)                           | [Backend Developer (Junior & Senior)](https://www.cakeresume.com/companies/tsaitung/jobs/backend-developer-junior-senior)           | Updated a month ago  |



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
