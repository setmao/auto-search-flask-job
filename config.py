configs = [
    {
        "platform_name": "cakeresume",
        "platform_url": "https://www.cakeresume.com/jobs?q={}&page={}",
        "jobs_list_element": 'soup.findAll("div", class_="job")',
        "job_link_element": 'job.find("a", "job-link").get("href")',
        "job_name_element": 'job.find("a", "job-link").text',
        "job_update_time_element": 'job.find("span", "update-section").text',
        "company_name_element": 'job.find("h5", "page-name").find("a").text',
        "company_link_element": 'job.find("h5", "page-name").find("a").get("href")',
    },
    {
        "platform_name": "104",
        "platform_url": "https://www.104.com.tw/jobs/search/?&jobsource=2018indexpoc&keyword={}&order={}",
        "jobs_list_element": 'soup.find_all("article",class_="js-job-item",attrs={"data-jobsource": re.compile(r"(.*list.*|2018.*)")})',
        "job_link_element": 'job.find_all("a", class_="js-job-link")[0]["href"].replace("//","")',
        "job_name_element": 'job.get("data-job-name")',
        "job_update_time_element": 'job.find("span",class_="b-tit__date").text.strip()',
        "company_name_element": 'job.get("data-cust-name")',
        "company_link_element": 'job.find_all("a")[1].get("href").replace("//","")',
    }
]
