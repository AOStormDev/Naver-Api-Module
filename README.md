# Naver_Api_Module

## 네이버 Api를 쉽게 사용할수 있도록 모듈로 처리하였습니다.

`
pip install pynaver_api
`

종류는
```
블로그
뉴스
책
성인 검색어 판별
백과사전
영화
카페글
지식iN
지역
오타변환
웹문서
이미지
쇼핑
전문자료
단축Url
```
입니다. 그리고 샘플 코드는
```py
from Naver_Api.Api import Naver
import asyncio

client_id = "네이버 Api 클라이언트 ID"
client_secret = "네이버 Api 클라이언트 시크릿"

N = Naver(client_id, client_secret)


async def Console():
    print(await N.ShortUrl(url="https://freeai.me"))


asyncio.run(Console())
```
요청했을때 따로 처리 한것 없이 바로 json 파일로 나오기 때문에 잘 정리하셔서 쓰시면 되겠습니다.
크레딧에 제 이름을 남겨주세요.
ex) 도움 : STORM#2856
