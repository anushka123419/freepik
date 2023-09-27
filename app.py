import requests
from anticaptchaofficial.recaptchav2proxyless import *
import json
import re
from flask import Flask, request
import urllib3
from urllib.parse import unquote
import urllib.parse
from pymongo import MongoClient
from twocaptcha import TwoCaptcha

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

myclient = MongoClient(
    "mongodb+srv://mysteriouscoder:mysteriouscoder@cluster0.agkearu.mongodb.net/?retryWrites=true&w=majority")
db = myclient["freepik"]
Collection = db["counter"]
session = requests.Session()
app = Flask(__name__)

# Replace this with your pCloud API access token
API_ACCESS_TOKEN = "otGUZzTBLD10Yy1fZcBRFykZzEjpJwaEHNpSDN6cIiOjCuF7cgvV"

def geturlid(url):
    array = re.findall(r'[0-9]+', url)
    for ii in range(0, len(array)):
        check = array[ii]
        lks = len(check)
        if lks > 4:
            return check
        else:
            continue

def capchatokengenerate():
    url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdvWJ8gAAAAAAXyyM14R9ry2XGaseLJI014nJo_&co=aHR0cHM6Ly93d3cuZnJlZXBpay5jb206NDQz&hl=en&v=vP4jQKq0YJFzU6e21-BGy3GP&size=invisible&cb=vjhupymd7ce8"
    r1 = requests.get(url)
    #print(r1.text)

    ftu = re.search(r'id="recaptcha-token" value="(.*?)">', r1.text).group(1)
    #print(ftu)

    headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "content-type": "application/x-www-form-urlencoded"

    }

    url2 = "https://www.google.com/recaptcha/api2/reload?k=6LdvWJ8gAAAAAAXyyM14R9ry2XGaseLJI014nJo_"
    payload = "v=vP4jQKq0YJFzU6e21-BGy3GP&reason=q&c="+ftu+"&k=6LdvWJ8gAAAAAAXyyM14R9ry2XGaseLJI014nJo_&co=aHR0cHM6Ly93d3cuZnJlZXBpay5jb206NDQz=en&size=invisible&chr=%5B50%2C7%2C61%5D&vh=339445566&bg=!wsSgxMEKAAQeHtUQbQEHDwHvhqIlDjUqfVHOoXfiB2na59kS4H7F380OyJU3plBf4ajm3SgKq2FrfvUq06rXbbrTg_w5RweSZtdwzrTgOaGWnbejesSozUk_9qLSojWLYWH599hyV4DmFQG_XXI0FoZifkhg-yZVXF_8BL4CdNIkZC3kBqaZUyydT_gqm5vh4KCjTrI56fC_7mHjldA8Mfo7un5RxbUivTEPyCYtYe4UMFbKMuUItc2-kpHAGzVVg1m_piWuoIjBSG8GsYzAfT5dvqRvvApeIxpKqHyanXcJWd-0Pw1kwXI0yggGQYA_0qXxdN0bmrhmHTsHYZs8_lZeXqpfedRIXfYIz9X3nSwpPJFVO8a5Y_BxOyqARf4gGKCKPc409JDyJAmaRIwM51hp4dZVVIR2h9Wz7CobnWPrGlOOBlFORsIxasLejLof5pfjrlJHcI-hU23bDvTTxXvrGUNpxlD7ZfJpkBK0lklo8mhK5FcmpxJSfO0XaxhUUJWwi0yuJAa6Of7uuvtFgOVpTTX1ZAkcK3dtWED1dBf8Ls6SDZdRJVqfrzfErXiQViWcinuf7K4Qxym_s_s4mRGfEOqw3qBLH0NrDHZ9jSfQshLBUQfmOBy2mNLSia0NudzEexDn0NhHgjzo9x6v0wuzMJaEBTHMEbb6o6ItndF-nAFF3Kdne9J99VafXCW6VwN87I4yLzc-QLVfsS6ETf_JWCAxdobeBf9MgHUruRf4n0i7Yzv2a_vipoAirDSAwu41jWVwfP4zCh2Ndc9T62Em6PH-db6aAPJDIc1wW4aIdMnn1720prgOpT90h9QLdY3BtS_v1hNGOXFf-e7xy0Cl4P-hMggx1_H1eQqthmHCDuBKPCnGGx5kKe0JtIfBXk30Eb2sw7kR7LEYqhrWLMKZHWTCxf36CvEJ1lanrjSqgAxWIW-HMqH4BOZgGtKYaJ3xHsPC1M4sJH9uJYoe2FXOQCialJDRtUiBlK_H1o9Nhwj-SpeMOR-pDErno5z0vS37sSoGN8T1NDk1n6_hbuTB0CtF0eSsPmbvfrPSEEqZvWYLG2OktNwPSHqDIFKvCNu5dnKtitUsiJjubkchS7u4Oj0IvUxvTQ"
    r2 = requests.post(url=url2, data=payload, headers=headers, verify=False)


    finaltoken = re.search(r'rresp","(.*?)"', r2.text).group(1)
    return finaltoken
def capchabypass2():
    twocaptcha = TwoCaptcha("2611d430a7facc26c0e844af2f15e16f")
    result = twocaptcha.recaptcha(sitekey='6LfEmSMUAAAAAEDmOgt1G7o7c53duZH2xL_TXckC',
                                       url='https://id.freepikcompany.com/v2/log-in?client_id=freepik',
                                       version='v3').get('code')

    return result

def capchabypass():
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("18613ff26acda86e699c1ccfbd733430")
    solver.set_website_url("https://id.freepikcompany.com/v2/log-in?client_id=freepik")
    solver.set_website_key("6LfEmSMUAAAAAEDmOgt1G7o7c53duZH2xL_TXckC")
    solver.set_soft_id(0)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        print("g-response: " + g_response)
        return g_response
    else:
        print("task finished with error " + solver.error_code)

def upload_file_to_pcloud(dwnresp, ids):

    file_content = dwnresp
    upload_url = "https://api.pcloud.com/uploadfile"

    headers = {
        "Authorization": f"Bearer {API_ACCESS_TOKEN}",
    }

    file_name = ids

    files = {
        'file': (file_name, file_content),
    }

    response = requests.post(upload_url, headers=headers, files=files, stream=True, verify=True)

    if response.status_code == 200:
        upload_result = response.json()
        file_id = upload_result['metadata'][0]['fileid']
        print(f"File uploaded successfully. File ID: {file_id}")

        # Generate share link
        share_link_url = "https://api.pcloud.com/getfilepublink"
        share_data = {
            "access_token": API_ACCESS_TOKEN,
            "fileid": file_id
        }

        share_response = requests.get(share_link_url, params=share_data, verify=False)
        share_result = share_response.json()
        share_link = share_result['link']
        return share_link

    else:

        print(f"Failed to upload file. Status code: {response.status_code}")

def loginfreepik(link):
    print(link)
    myvl = link.split("/")
    slug = myvl[2]

    if "freepik" in slug:
        imageid = geturlid(link)
        tk2 = capchatokengenerate()

        apikey = "VuqP6URUZjWD9zCEI57CHWviZdgimx"

        url = urllib.parse.quote(link)

        apiurl = "https://vip.neh.tw/api/stockinfo/null/null?apikey=" + apikey + "&url=" + url
        vpireq = requests.get(url=apiurl)
        jk = json.loads(vpireq.text)
        dupimage = jk["data"]["image"]

        realimagename = jk["data"]["name"]
        if realimagename == '':
            id = jk["data"]["id"]
            exts = jk["data"]["ext"]
            if "," in exts or 'multiple formats' in exts:
                realimagename = id + "." + "zip"
            else:
                realimagename = id + "." + exts

        finalid = realimagename

        urlgetfileid = 'https://api.pcloud.com/search'

        # Define headers for the request
        headers = {
            "Authorization": "Bearer {}".format(API_ACCESS_TOKEN)
        }

        # Define parameters for the request
        params = {
            "query": finalid
        }

        response = requests.get(urlgetfileid, headers=headers, params=params)
        rksns = json.loads(response.text)
        val = rksns['total']
        if val > 0:
            fileidfinal = rksns['items'][0]['fileid']

            share_link_url = "https://api.pcloud.com/getfilepublink"
            share_data = {
                "access_token": API_ACCESS_TOKEN,
                "fileid": fileidfinal
            }

            share_response = requests.get(share_link_url, params=share_data, verify=False)
            share_result = share_response.json()
            print("File Taken From CLOUD")
            share_link = share_result['link']
            return json.dumps(
                {'status': 'true', 'result': {'download': share_link}, 'filetaken': 'File Taken From out Cloud'})
        else:

            max_retries = 2
            retry_delay = 1  # Retry delay in seconds
            for retry in range(max_retries):
                results = Collection.find()
                for document in results:
                    specific_value = document["count"]

                if specific_value == 0:
                    urllogin = "https://id-api.freepikcompany.com/v2/login?client_id=freepik"

                    headers = {
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
                        "Connection": "keep-alive",
                        "Content-Length": "1730",
                        "content-type": "application/json",
                        "Host": "id-api.freepikcompany.com",
                        "Origin": "https://id.freepikcompany.com",
                        "Referer": "https://id.freepikcompany.com/",
                        "sec-ch-ua-mobile": "?1",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-site",
                        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
                    }
                    token = capchabypass2()
                    body = """{\"email\":\"arlene.camilo@gmail.com\",\"password\":\"areca1986\",\"recaptchaToken\":\"""" + str(
                        token) + """\",\"lang\":\"en-US\"}"""
                    resp = session.post(url=urllogin, data=body, headers=headers)
                    res = json.loads(resp.text)
                    print(resp.text)
                    reidrect = res['data']['redirectUrl']
                    nxthead = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                    finalre = reidrect.replace("\/", "/")
                    r1 = session.get(url=finalre, headers=nxthead)
                    # print(r1.text)


                    dwnreqhead = {
                        "Host": "www.freepik.com",
                        "Connection": "keep-alive",
                        "X-Requested-With": "xmlhttprequest",
                        "sec-ch-ua-mobile": "?0",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                        "Accept": "*/*",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Dest": "empty",
                        "Referer": "https://www.freepik.com/premium-photo/portrait-happy-young-asian-woman-standing-isolated-against-white-wall-studio-looking-camera-shows-how-copy-space-points_21317862.htm?log-in=email",
                    }
                    session.get(url="https://www.freepik.com/xhr/logged-user-data", headers=dwnreqhead)
                    session.get(url="https://www.freepik.com/xhr/register-download/2740363?type=regular",
                                headers=dwnreqhead)
                    session.get(url="https://www.freepik.com/xhr/validate", headers=dwnreqhead)
                    urldown = "https://www.freepik.com/xhr/download-url/" + str(imageid) + "?token=" + str(
                        tk2)
                    r6 = session.get(url=urldown, headers=dwnreqhead)
                    dwn = json.loads(r6.text)
                    check = dwn['success']
                    downloadurl = dwn['url']
                    nxthead = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }

                    dwnresp = session.get(url=downloadurl, headers=nxthead)
                    file_content = dwnresp.content
                    news = upload_file_to_pcloud(file_content, realimagename)
                    my_json_string = json.dumps({'status': 'true', 'result': {'download': news}})

                    update_operation = {
                        "$set": {"count": 1}}
                    result = Collection.update_one({}, update_operation)

                    return my_json_string

                elif specific_value > 0:
                    specific_value += 1
                    if specific_value == 6:
                        update_operation = {
                            "$set": {"count": 0}}
                        result = Collection.update_one({}, update_operation)
                    else:
                        update_operation = {
                            "$set": {"count": specific_value}}
                        result = Collection.update_one({}, update_operation)

                    dwnreqhead = {
                        "Host": "www.freepik.com",
                        "Connection": "keep-alive",
                        "X-Requested-With": "xmlhttprequest",
                        "sec-ch-ua-mobile": "?0",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                        "Accept": "*/*",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Dest": "empty",
                        "Referer": "https://www.freepik.com/premium-photo/portrait-happy-young-asian-woman-standing-isolated-against-white-wall-studio-looking-camera-shows-how-copy-space-points_21317862.htm?log-in=email",
                    }
                    session.get(url="https://www.freepik.com/xhr/logged-user-data", headers=dwnreqhead)
                    session.get(url="https://www.freepik.com/xhr/register-download/2740363?type=regular",
                                headers=dwnreqhead)
                    session.get(url="https://www.freepik.com/xhr/validate", headers=dwnreqhead)
                    urldown = "https://www.freepik.com/xhr/download-url/" + str(imageid) + "?token=" + str(
                        tk2)
                    r6 = session.get(url=urldown, headers=dwnreqhead)
                    dwn = json.loads(r6.text)
                    check = dwn['success']
                    downloadurl = dwn['url']
                    nxthead = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }

                    dwnresp = session.get(url=downloadurl, headers=nxthead)
                    file_content = dwnresp.content
                    news = upload_file_to_pcloud(file_content, realimagename)
                    my_json_string = json.dumps({'status': 'true', 'result': {'download': news}})
                    return my_json_string


@app.route('/newfreepik2', methods=['GET'])
def newfree():
    args = request.args
    url = args.get('url')
    dwnlnk = loginfreepik(url)
    return dwnlnk

if __name__ == "__main__":
    app.run()




