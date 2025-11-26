"""
Jsearch MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.5.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.5.0"
__tag__ = "jsearch/1.5.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Jsearch\",\n    \"version\": \"1.5.0\",\n    \"description\": \"RapidAPI: letscrape-6bRBa3QguO5/jsearch\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://jsearch.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/search\": {\n      \"get\": {\n        \"summary\": \"Job Search\",\n        \"description\": \"Search for jobs posted on any public job site across the web on the largest job aggregate in the world (Google for Jobs). Extensive filtering support and most options available on Google for Jobs.\",\n        \"operationId\": \"job_search\",\n        \"parameters\": [\n          {\n            \"name\": \"query\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Free-form jobs search query. It is highly recommended to include job title and location as part of the query, see query examples below. Examples: web development jobs in chicago marketing manager in new york via linkedin\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Page to return (each page includes up to 10 results). Default: 1 Allowed values: 1-50\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"num_pages\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Number of pages to return, starting from page. Default: 1 Allowed values: 1-50 Note: requests for more than one page and up to 10 pages are charged x2 and requests for more than 10 pages are charged 3x.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"1\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"country\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Country code of the country from which to return job postings. Please note that this parameter must be set in order to get jobs in a specific country, for example, to query for software developer jobs in Berlin, one should add country=de to the request - e.g. query=software+developers+in+berlin&country=de. Default: us Allowed values: See https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"language\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Language code in which to return job postings. Leave empty to use the primary language in the specified country (country parameter). Note that each country supports certain languages. In case a language not supported by the specified country is used, it is likely that no results will be returned. Allowed values: See https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"date_posted\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Find jobs posted within the time you specify. Default: all Allowed values: all, today, 3days, week, month\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"work_from_home\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"employment_types\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Find jobs of particular employment types, specified as a comma delimited list of the following values: FULLTIME, CONTRACTOR, PARTTIME, INTERN.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"job_requirements\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Find jobs with specific requirements, specified as a comma delimited list of the following values: under_3_years_experience, more_than_3_years_experience, no_experience, no_degree.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"radius\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Return jobs within a certain distance from location as specified as part of the query (in km). This internally sent as the Google \\\\\\\"lrad\\\\\\\" parameter and although it might affect the results, it is not strictly followed by Google for Jobs.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"exclude_job_publishers\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Exclude jobs published by specific publishers, specified as a comma (,) separated list of publishers to exclude. Example: BeeBe,Dice\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"fields\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"A comma separated list of job fields to include in the response (field projection). By default all fields are returned. Example: employer_name,job_publisher,job_title,job_country\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/job-details\": {\n      \"get\": {\n        \"summary\": \"Job Details\",\n        \"description\": \"Get all job details, including additional information such as: application options / links, employer reviews and estimated salaries for similar jobs.\",\n        \"operationId\": \"job_details\",\n        \"parameters\": [\n          {\n            \"name\": \"job_id\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Job Id of the job for which to get details. Batching of up to 20 Job Ids is supported by separating multiple Job Ids by comma (,). Note that each Job Id in a batch request is counted as a request for quota calculation.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"country\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Country code of the country from which to return job posting. Default: us Allowed values: See https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"language\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Language code in which to return job postings. Leave empty to use the primary language in the specified country (country parameter). Allowed values: See https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"fields\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"A comma separated list of job fields to include in the response (field projection). By default all fields are returned. Example: employer_name,job_publisher,job_title,job_country\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/estimated-salary\": {\n      \"get\": {\n        \"summary\": \"Job Salary\",\n        \"description\": \"Get estimated salaries / pay for a jobs around a location by job title and location. The salary estimation is returned for several periods, depending on data availability / relevance, and includes: hourly, daily, weekly, monthly, or yearly.\",\n        \"operationId\": \"job_salary\",\n        \"parameters\": [\n          {\n            \"name\": \"job_title\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Job title for which to get salary estimation.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"location\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Free-text location/area in which to get salary estimation.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"location_type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the type of the location you are looking to get salary estimation for additional accuracy. Allowed values: ANY, CITY, STATE, COUNTRY Default: ANY\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"years_of_experience\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Get job estimation for a specific experience level range (years). Allowed values: ALL, LESS_THAN_ONE, ONE_TO_THREE, FOUR_TO_SIX, SEVEN_TO_NINE, TEN_TO_FOURTEEN, ABOVE_FIFTEEN Default: ALL\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"fields\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"A comma separated list of job salary fields to include in the response (field projection). By default all fields are returned. Example: job_title,median_salary,location\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/company-job-salary\": {\n      \"get\": {\n        \"summary\": \"Company Job Salary\",\n        \"description\": \"Get estimated job salaries/pay in a specific company by job title and optionally a location and experience level in years.\",\n        \"operationId\": \"company_job_salary\",\n        \"parameters\": [\n          {\n            \"name\": \"company\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"The company name for which to get salary information (e.g. Amazon).\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"job_title\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Job title for which to get salary estimation.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"location\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Free-text location/area in which to get salary estimation.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"location_type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Specify the type of the location you are looking to get salary estimation for additional accuracy. Allowed values: ANY, CITY, STATE, COUNTRY Default: ANY\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"years_of_experience\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Get job estimation for a specific experience level range (years). Allowed values: ALL, LESS_THAN_ONE, ONE_TO_THREE, FOUR_TO_SIX, SEVEN_TO_NINE, TEN_TO_FOURTEEN, ABOVE_FIFTEEN Default: ALL\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "jsearch.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://jsearch.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="jsearch",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "jsearch.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Jsearch MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()