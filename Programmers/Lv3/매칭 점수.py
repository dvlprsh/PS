'''
기본점수 : 검색어 등장 횟수
외부 링크 수 : 외부 페이지로 연결된 링크 개수
링크 점수 : 연결된 다른 웹페이지의 (기본점수 / 외부 링크수) 총 합
매칭점수 : 기본점수 + 링크점수
'''
#Solve
import re
def solution(word, pages):
    page_dict={} # url: (index, 기본점수, 외부링크 개수)
    connection = set() # (end, start)
    matching_point = [0 for _ in pages]
    meta_url_pattern = re.compile(r'<meta .*/>')
    outer_link_pattern = re.compile(r'<a.*?>')
    url_pattern = re.compile(r'https://[a-zA-Z0-9/.]*')
    for index, page in enumerate(pages):
        target = re.compile(word+'$', re.I)
        #body : 모든 html 태그, 특수문자 제거한 문자열
        body = re.split('[^a-zA-Z]', page)
        basic_point= len(list(filter(lambda x: target.match(x), body))) #기본점수
        matching_point[index] = basic_point
        meta_url = meta_url_pattern.search(page).group()
        url = url_pattern.search(meta_url).group() #현재 page url
        a_tags = outer_link_pattern.findall(page) #외부 링크
        for v in a_tags:
            link = url_pattern.search(v).group()
            connection.add((link, url))
        page_dict[url] = (index, basic_point, len(a_tags))
    for v in list(connection):
        if not v[0] in page_dict:
            continue
        else:
            matching_point[page_dict[v[0]][0]] += page_dict[v[1]][1] / page_dict[v[1]][2] 
    answer = 0
    max_point = 0
    for i, v in enumerate(matching_point):
        if v > max_point:
            max_point = v
            answer = i
    return answer
# 풀이 1 - 100점
import re
def solution(word, pages):
    page_dict={} # url: (index, 기본점수, 외부링크 개수)
    connection = set() # (end, start)
    matching_point = [0 for _ in pages]
    body_patten = re.compile(r'<body>.*</body>', re.DOTALL)
    meta_url_pattern = re.compile(r'<meta property="og:url".*?/>')
    outer_link_pattern = re.compile(r'<a.*?/a>')
    url_pattern = re.compile(r'https://[a-zA-Z0-9/.]*')
    #special_pattern = re.compile(r'<.*?> | [^a-zA-Z0-9]')
    for index, page in enumerate(pages):
        target = re.compile(word+'$', re.I)
        #body : 모든 html 태그, 특수문자 제거한 문자열
        body = re.split('[^a-zA-Z]', page)
        basic_point= len(list(filter(lambda x: target.match(x), body))) #기본점수
        matching_point[index] = basic_point
        meta_url = meta_url_pattern.search(page).group()
        url = url_pattern.search(meta_url).group() #현재 page url
        a_tags = outer_link_pattern.findall(page) #외부 링크
        for v in a_tags:
            link = url_pattern.search(v).group()
            connection.add((link, url))
        page_dict[url] = (index, basic_point, len(a_tags))
    for v in list(connection):
        if not v[0] in page_dict:
            continue
        else:
            matching_point[page_dict[v[0]][0]] += page_dict[v[1]][1] / page_dict[v[1]][2] 
    answer = 0
    max_point = 0
    for i, v in enumerate(matching_point):
        if v > max_point:
            max_point = v
            answer = i
    return answer
# 풀이 2 - 55점
import re
def solution(word, pages):
    page_dict={} # url: (index, 기본점수, 외부링크 개수)
    connection = set() # (end, start)
    matching_point = [0 for _ in pages]
    body_patten = re.compile(r'<body>.*</body>', re.DOTALL)
    meta_url_pattern = re.compile(r'<meta property="og:url".*/>') # **오답원인**
    outer_link_pattern = re.compile(r'<a.*/a>') # **오답원인**
    url_pattern = re.compile(r'https://[a-zA-Z0-9/.]*')
    #special_pattern = re.compile(r'<.*?> | [^a-zA-Z0-9]')
    for index, page in enumerate(pages):
        target = re.compile(word+'$', re.I)
        #body : 모든 html 태그, 특수문자 제거만 문자열
        body = re.split('<.*?>|[^a-zA-Z]', body_patten.search(page).group())
        basic_point= len(list(filter(lambda x: target.match(x), body))) #기본점수
        matching_point[index] = basic_point
        meta_url = meta_url_pattern.search(page).group()
        url = url_pattern.search(meta_url).group() #현재 page url
        a_tags = outer_link_pattern.findall(page) #외부 링크
        for v in a_tags:
            link = url_pattern.search(v).group()
            connection.add((link, url))
        page_dict[url] = (index, basic_point, len(a_tags))
    for v in list(connection):
        if not v[0] in page_dict:
            continue
        matching_point[page_dict[v[0]][0]] += page_dict[v[1]][1] / page_dict[v[1]][2] 

    return matching_point.index(max(matching_point))