from bs4 import BeautifulSoup
import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': '*/*',
    'Accept-Language': 'am,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'x-amz-continuous-deployment-state=AYABeJvCF1kRTmb5cT6laiy1h8MAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxNTk1MzcxVEJNNTJaWDdPU09PAAEAAkNEABpDb29raWUAAACAAAAADP99PXzDGK%2FhsLSN+wAwu6LJzhXJ2BM%2Fud1sgnX44UmoKoiuH+%2FJgHpvI9CyH3W+lCyeAc8Bx1rxggY7xyB2AgAAAAAMAAQAAAAAAAAAAAAAAAAAAKSPqMC+asAKytdeGNIpwij%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwB4YBfszfw4XbnpbDuQQMNXc8qYExQkmxr0Q0KXc8qYExQkmxr0Q0KXc8qYExQkmxr0Q0KXc8qYExQkmxr0Q0KXc8qYExQkmxr0Q0KXc8qYExQkmxr0Q0KXc8qYExQkmxr0Q0KXc8qYExQkmxr0Q0K; zguid=24|%24d07fa068-d217-4ba8-b1a7-d334c8f5ee35; zjs_anonymous_id=%22d07fa068-d217-4ba8-b1a7-d334c8f5ee35%22; zjs_user_id=null; zg_anonymous_id=%227372e109-23ad-44f7-9829-92d5bd2136e7%22; AWSALB=hpQ+04WwFrnNbFVUdwSdYcBrQR1WfsMMuMnKZyE68MyvRISn/7eET6gxKyza+4DY4FTj8qqIgo+7SuWEhbB7aPgjlDgeLjHbYxUHjz7ThIB16v8Y0irfFhPsx9fW; AWSALBCORS=hpQ+04WwFrnNbFVUdwSdYcBrQR1WfsMMuMnKZyE68MyvRISn/7eET6gxKyza+4DY4FTj8qqIgo+7SuWEhbB7aPgjlDgeLjHbYxUHjz7ThIB16v8Y0irfFhPsx9fW; g_state={"i_p":1684243961033,"i_l":2}; search=6|1686753266877%7Crect%3D34.23976721511232%252C-83.61498936718749%252C33.680500896120115%252C-84.46093663281249%26rid%3D39051%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0939051%09%09%09%09%09%09; JSESSIONID=1A97E6743419B66AB8412C41138BACE4; zgsession=1|fb26e3f7-7830-4787-a48f-aba691491bd7',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    "searchQueryState": '{"pagination":{"currentPage": 1},"mapBounds":{"north":47.39322389636524,"east":-68.38852964279245,"south":10.739530633809519,"west":-122.52915464279243},"regionSelection":[{"regionId":39051,"regionType":6}],"isMapVisible":false,"filterState":{"isAllHomes":{"value":true},"sortSelection":{"value":"days"}},"isListVisible":true,"mapZoom":5}&wants={"cat1":["listResults"],"cat2":["total"]}',
} 
response = requests.get(
    'https://www.zillow.com/homes/for_sale',
    headers=headers,
    params=params
)
response2 = requests.get('https://www.finder.fi')
print(response2.content)
'''
soup = BeautifulSoup(response.content, "lxml")
links = soup.find_all("a", class_="property-card-link")
print(len(links))
for link in links:
    url = link.get("href")
    detail = requests.get(url, headers=headers, params=params)
    soup2 = BeautifulSoup(detail.content, "lxml")
    hisory = soup2.find_all('div', class_="hGwlRq")
    print(len(hisory))
    for h in hisory:
        print(h)
'''