<h1 align="center"> WEBSCRAPING APP</h1>

### Stack: `python, django, scrapy, javascript, jquery, chartjs`

<br>

## ** SCRIPT TO RUN **

### Cron

- To manage and execute spider scheduling in parallel.
  ![Dashboard](screenshots/cron.png)

### Bash

- To execute all spiders manually. Run `xspider`
  ![Dashboard](screenshots/xspider.png)

### Per site example

- To selectively target specific sites for a particular spider manually. <br>
  `scrapy crawl edealer -a url=https://www.stockiechrysler.com/`

### Per template/spider example

- To manually execute a spider or multiple spiders <br>
  `python runspider.py -s edealer` <br>
  `python runspider.py -s all`

<br>

## ** BACK END **

### Dashboard

![Dashboard](screenshots/be_dashboard.png)

### Target Sites

![Dashboard](screenshots/be_sites.png)

### Spider logs

![Dashboard](screenshots/be_spiderlogs.png)

<br>

## ** FRONT END **

### Dashboard

![Dashboard](screenshots/fe_dashboard.png)

### Target Sites

![Dashboard](screenshots/fe_project.png)

### Target Site Info

![Dashboard](screenshots/fe_site_info.png)

### Target Site Scrapes

![Dashboard](screenshots/fe_site_scrape.png)

### Target Site Scrape Details

![Dashboard](screenshots/fe_site_scrape_imgs.png)

### API

![Dashboard](screenshots/fe_api.png)

### API - Postman Example

![Dashboard](screenshots/fe_api_postman.png)

### API - Curl/Httpie Example

![Dashboard](screenshots/fe_api_curl_httpie.png)

### Help

![Dashboard](screenshots/fe_help.png)

<br>

## ** ADDT'L NOTES **

I recorded an 8-minute screen capture video showcasing the app's initial deployment in April 2022 from the client's perspective.

[Screenshare link](https://drive.google.com/file/d/1y5J7UsepRDqGu0v0K8vlH_uiHZwExoZy/view?usp=sharing)
