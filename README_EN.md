# Jsearch MCP Server

English | [简体中文](./README.md) | [繁體中文](./README_ZH-TW.md)

## 🚀 Quick Start with EMCP Platform

**[EMCP](https://sit-emcp.kaleido.guru)** is a powerful MCP server management platform that allows you to quickly use various MCP servers without manual configuration!

### Quick Start:

1. 🌐 Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)**
2. 📝 Register and login
3. 🎯 Go to **MCP Marketplace** to browse all available MCP servers
4. 🔍 Search or find this server (`bach-jsearch`)
5. 🎉 Click the **"Install MCP"** button
6. ✅ Done! You can now use it in your applications

### EMCP Platform Advantages:

- ✨ **Zero Configuration**: No need to manually edit config files
- 🎨 **Visual Management**: Easy-to-use GUI for managing all MCP servers
- 🔐 **Secure & Reliable**: Centralized API key and authentication management
- 🚀 **One-Click Install**: Rich selection of servers in MCP Marketplace
- 📊 **Usage Statistics**: Real-time service call monitoring

Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)** now to start your MCP journey!


---

## Introduction

This is an MCP server for accessing the Jsearch API.

- **PyPI Package**: `bach-jsearch`
- **Version**: 1.0.0
- **Transport Protocol**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-jsearch
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-jsearch bach_jsearch

# 或指定版本
uvx --from bach-jsearch@latest bach_jsearch
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-jsearch

# 运行（命令名使用下划线）
bach_jsearch
```

## Configuration

### API Authentication

This API requires authentication. Please set environment variable:

```bash
export API_KEY="your_api_key_here"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | API Key | Yes |




### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "jsearch": {
      "command": "uvx",
      "args": ["--from", "bach-jsearch", "bach_jsearch"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Note**: Replace `E:\path\to\jsearch\server.py` with the actual server file path.


## 可用工具

此服务器提供以下工具:


### `job_search`

Search for jobs posted on any public job site across the web on the largest job aggregate in the world (Google for Jobs). Extensive filtering support and most options available on Google for Jobs.

**端点**: `GET /search`


**参数**:

- `query` (string) *必需*: Free-form jobs search query. It is highly recommended to include job title and location as part of the query, see query examples below. Examples: web development jobs in chicago marketing manager in new york via linkedin

- `page` (string): Page to return (each page includes up to 10 results). Default: 1 Allowed values: 1-50

- `num_pages` (string): Number of pages to return, starting from page. Default: 1 Allowed values: 1-50 Note: requests for more than one page and up to 10 pages are charged x2 and requests for more than 10 pages are charged 3x.

- `country` (string): Country code of the country from which to return job postings. Please note that this parameter must be set in order to get jobs in a specific country, for example, to query for software developer jobs in Berlin, one should add country=de to the request - e.g. query=software+developers+in+berlin&country=de. Default: us Allowed values: See https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

- `language` (string): Language code in which to return job postings. Leave empty to use the primary language in the specified country (country parameter). Note that each country supports certain languages. In case a language not supported by the specified country is used, it is likely that no results will be returned. Allowed values: See https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes

- `date_posted` (string): Find jobs posted within the time you specify. Default: all Allowed values: all, today, 3days, week, month

- `work_from_home` (string): Example value: 

- `employment_types` (string): Find jobs of particular employment types, specified as a comma delimited list of the following values: FULLTIME, CONTRACTOR, PARTTIME, INTERN.

- `job_requirements` (string): Find jobs with specific requirements, specified as a comma delimited list of the following values: under_3_years_experience, more_than_3_years_experience, no_experience, no_degree.

- `radius` (string): Return jobs within a certain distance from location as specified as part of the query (in km). This internally sent as the Google \"lrad\" parameter and although it might affect the results, it is not strictly followed by Google for Jobs.

- `exclude_job_publishers` (string): Exclude jobs published by specific publishers, specified as a comma (,) separated list of publishers to exclude. Example: BeeBe,Dice

- `fields` (string): A comma separated list of job fields to include in the response (field projection). By default all fields are returned. Example: employer_name,job_publisher,job_title,job_country



---


### `job_details`

Get all job details, including additional information such as: application options / links, employer reviews and estimated salaries for similar jobs.

**端点**: `GET /job-details`


**参数**:

- `job_id` (string) *必需*: Job Id of the job for which to get details. Batching of up to 20 Job Ids is supported by separating multiple Job Ids by comma (,). Note that each Job Id in a batch request is counted as a request for quota calculation.

- `country` (string): Country code of the country from which to return job posting. Default: us Allowed values: See https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

- `language` (string): Language code in which to return job postings. Leave empty to use the primary language in the specified country (country parameter). Allowed values: See https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes

- `fields` (string): A comma separated list of job fields to include in the response (field projection). By default all fields are returned. Example: employer_name,job_publisher,job_title,job_country



---


### `job_salary`

Get estimated salaries / pay for a jobs around a location by job title and location. The salary estimation is returned for several periods, depending on data availability / relevance, and includes: hourly, daily, weekly, monthly, or yearly.

**端点**: `GET /estimated-salary`


**参数**:

- `job_title` (string) *必需*: Job title for which to get salary estimation.

- `location` (string) *必需*: Free-text location/area in which to get salary estimation.

- `location_type` (string): Specify the type of the location you are looking to get salary estimation for additional accuracy. Allowed values: ANY, CITY, STATE, COUNTRY Default: ANY

- `years_of_experience` (string): Get job estimation for a specific experience level range (years). Allowed values: ALL, LESS_THAN_ONE, ONE_TO_THREE, FOUR_TO_SIX, SEVEN_TO_NINE, TEN_TO_FOURTEEN, ABOVE_FIFTEEN Default: ALL

- `fields` (string): A comma separated list of job salary fields to include in the response (field projection). By default all fields are returned. Example: job_title,median_salary,location



---


### `company_job_salary`

Get estimated job salaries/pay in a specific company by job title and optionally a location and experience level in years.

**端点**: `GET /company-job-salary`


**参数**:

- `company` (string) *必需*: The company name for which to get salary information (e.g. Amazon).

- `job_title` (string) *必需*: Job title for which to get salary estimation.

- `location` (string): Free-text location/area in which to get salary estimation.

- `location_type` (string): Specify the type of the location you are looking to get salary estimation for additional accuracy. Allowed values: ANY, CITY, STATE, COUNTRY Default: ANY

- `years_of_experience` (string): Get job estimation for a specific experience level range (years). Allowed values: ALL, LESS_THAN_ONE, ONE_TO_THREE, FOUR_TO_SIX, SEVEN_TO_NINE, TEN_TO_FOURTEEN, ABOVE_FIFTEEN Default: ALL



---



## 技术栈

- **FastMCP**: 快速、Pythonic 的 MCP 服务器框架
- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

This server is automatically generated by [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) tool.

Version: 1.0.0
