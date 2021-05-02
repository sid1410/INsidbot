import requests
from Resources.constants import headers, template, headers_tbs, tbs_end_template,tbs_template,step_html
import json
from bs4 import BeautifulSoup
from config import cookie

headers_tbs['cookie'] = cookie
headers['cookie'] = cookie

def fetch_like_and_dislikes(soup):
    entity_id_div = soup.find("div", {"class": "answer txt-small mod-parent-container"})
    entityID = entity_id_div.get("data-commentingid")
    url = "https://www.chegg.com/study/_ajax/contentfeedback/getreview?entityType=ANSWER&entityId={}".format(entityID)
    resp = requests.get(url=url, headers=headers)
    review_dict = json.loads(resp.text)
    review_count = review_dict.get("review_count")
    result = review_count.get("result")
    up = 0
    down = 0
    if not result:
        return up, down
    count_down = result.get("1")
    count_up = result.get("0")
    if count_up:
        if count_up.get("reviewValue") == "0":
            up = count_up.get("count")
        elif count_up.get("reviewValue") == "1":
            down = count_up.get("count")
    if count_down:
        if count_down.get("reviewValue") == "0":
            up = count_down.get("count")
        elif count_down.get("reviewValue") == "1":
            down = count_down.get("count")

    return up, down

def fetch_text_book_solution(answer_url):
    graph_ql = "https://www.chegg.com/study/_ajax/persistquerygraphql"


    token_url = "https://www.chegg.com/study/_ajax/global/init"


    resp = requests.post(token_url, headers=headers_tbs)
    if resp.status_code!=200 or not resp.text:
        return "Do not decrease"
    token_dict = json.loads(resp.text)
    token = token_dict.get("token")
    if not token:
        return "Do not decrease"

    url_parse = answer_url.split("-chapter-")[1]

    details = url_parse.split("-")

    isbn = details[4]
    chapterName = details[0]
    problemName = details[2]

    request1_payload = {"query":
                            {"operationName":"getTOC","variables":{"isbn13":isbn}
                             },
                        "token":token}
    resp = requests.post(graph_ql, headers=headers_tbs, data=json.dumps(request1_payload))
    if resp.status_code!=200 or not resp.text:
        return "Do not decrease"

    topic_of_content = json.loads(resp.text)

    chapter_dict = topic_of_content['data']['textbook_solution']['toc']['chapters']

    chapter_id = ""
    problem_id = ""
    for chapter in chapter_dict:
        if chapter['chapterName'] == chapterName:
            chapter_id = chapter['chapterId']
            for problem in chapter['problems']:
                if problem['problemName'].upper() == problemName.upper():
                    problem_id = problem['problemId']
                    break
            if problem_id :
                break

    if not problem_id or not chapter_id:
        return "Do not decrease"

    request2_payload = {"query":{"operationName":"getSolutionDetails",
                                 "variables":{"isbn13":isbn,
                                              "chapterId":chapter_id,"problemId":problem_id}
                                 },"token":token}

    resp = requests.post(graph_ql, headers=headers_tbs, data=json.dumps(request2_payload))

    sol_dict = json.loads(resp.text)

    problem = sol_dict['data']['textbook_solution']['chapter'][0]['problems'][0]

    problem_html = problem['problemHtml']
    steps = []

    solution = problem['solutionV2'][0]['steps']

    reviews = problem['solutions'][0]['reviews']
    up = reviews.get("positiveReviewCount") or 0
    down = reviews.get("negativeReviewCount") or 0

    final_html = tbs_template.format(problem_html)
    for index, step in enumerate(solution):
        final_html = final_html+step_html.format(str(index+1))+step['html']
    final_html=final_html+(tbs_end_template.format(up,down))

    return  final_html


def fetch_QandA(answer_url):
    resp = requests.get(answer_url, headers=headers)
    soup = BeautifulSoup(resp.content.decode('utf-8'), 'html.parser')

    for div in soup.find_all("div", {'class': 'hidden'}):
        div.decompose()
    for div in soup.find_all("span", {'class': 'transcribed-text'}):
        div.decompose()
    for div in soup.find_all("span", {'class': 'transcribed-image-text hidden'}):
        div.decompose()
    q_division = str(soup.find("div", {"class": "ugc-base question-body-text"}))
    a_division = str(soup.find("div", {"class": "answer-given-body ugc-base"}))

    if a_division == 'None':
        return "Do not decrease"

    count_upvote, count_downvote = fetch_like_and_dislikes(soup=soup)

    if (q_division.find('src="//"') == -1):
        q_division = q_division.replace('src="//', 'src="https://')
    if (a_division.find('src="//"') == -1):
        a_division = a_division.replace('src="//', 'src="https://')
    return template.format(q_division, a_division, count_upvote, count_downvote)


def fetch_answer(answer_url):

    if answer_url.find("/questions-and-answers/")!=-1:
        return fetch_QandA(answer_url)
    else:
        return fetch_text_book_solution(answer_url)
