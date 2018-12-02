개인프로젝트 계획 설명

네이버 영화 사이트에 기재된 영화 예매 순위 (1~10위)와 예매율을 각 순위에 해당하는 영화의 개봉일, 관람객 평점, 평론가 평점과 함께 출력한다.

<부가설명>
1. 네이버 영화 사이트: https://movie.naver.com/movie/sdb/rank/rreserve.nhn 에서 ‘예매 랭킹 Top 10’의 영화 예매 순위와 예매율을 출력한다.

2. 영화의 개봉일, 관람객 평점, 평론가 평점은 위의 url의 ‘예매 랭킹 Top 10’에서 각 순위 옆에 기재된 영화명을 클릭하면 연결되는 url 사이트
(예시: https://movie.naver.com/movie/bi/mi/basic.nhn?code=154255) 에서 뽑아와 출력한다.


[데이터 전처리 시나리오]

출력하고자 하는 내용이 포함되어있는 부분을 slicing 하여 변수에 저장한 다음, 역시 slicing 하여 필요한 부분을 가공하여 출력한다. 

<부가설명>
1. https://movie.naver.com/movie/sdb/rank/rreserve.nhn 에서 각 순위에 해당하는 데이터 부분을 find를 이용해 slicing 하여 변수에 저장한 뒤 영화명, 예매율에 해당하는 부분을 slicing 하고 가공하여 출력한다.

2. 영화의 개봉일, 관람객 평점, 평론가 평점에 대한 데이터를 얻기 위해서 https://movie.naver.com/movie/sdb/rank/rreserve.nhn 에서 각 순위에 해당하는 데이터 부분을 (살짝 작은 범위로) 새로 slicing 하여 변수에 저장하고, 이 부분에서 find로 '/movie/bi/mi/basic.nhn?code=' 를 찾아 slicing으로 필요한 부분까지 뽑아낸다.

3. 위의 2.에서 뽑아낸 것을 'https://movie.naver.com' 의 뒷부분에 더해주어 최종적으로 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=154255' 와같은 url을 만들어 변수에 저장한다.

4. 위의 3.에서 저장한 url에서 개봉일, 관람객 평점, 평론가 평점에 해당하는 부분을 각각 slicing을 활용해 변수에 저장한 후 역시 slicing하여 필요한 부분만 가공하여 출력한다.

+) 관람객 평점, 평론가 평점을 출력 할 때에는 에러가 나지 않게 하기 위해, 에러가 발생할 수 있는 요인 (관람객 평점 혹은 평론가 평점이 사이트에 입력이 안되어 있는 경우 등)을 파악하여 if 조건문을 둔다. 
