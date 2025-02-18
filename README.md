# kbostadium

* 한국 프로야구 구단 전 구장 리뷰 및 시설 정보 제공 웹 프로젝트


### USE
```
$ info-sta --help

 Usage: info-sta [OPTIONS] KEYWORD

╭─ Arguments ───────────────────────────────────────────────────────╮
│ *    keyword      TEXT  [default: None] [required]                │
╰───────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────╮
│ --asc     --no-asc             [default: no-asc]                  │
│ --rcnt                INTEGER  [default: 10]                      │
│ --help                         Show this message and exit.        │
╰───────────────────────────────────────────────────────────────────╯

$ info-sta 좌석수 --asc

         구단     좌석수
0   키움 히어로즈  16,670
1   NC 다이노스  17,891
2     KT 위즈  18,700
3    한화 이글스  20,007
4  KIA 타이거즈  20,500
5   롯데 자이언츠  22,758
6   SSG 랜더스  23,000
7    LG 트윈스  23,750
8    두산 베어스  23,750
9   삼성 라이온즈  24,000

$ info-sta 좌석

잘못된 열 이름입니다. 유효한 열 이름은 구단, 경기장명, 주소, 완공연도, 건축면적, 좌석수 입니다.

-- 
$ info-kbo --help

 Usage: info-kbo [OPTIONS] KEYWORD

╭─ Arguments ────────────────────────────────────────────────────────╮
│ *    keyword      TEXT  [default: None] [required]                 │
╰────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                        │
╰────────────────────────────────────────────────────────────────────╯

$ info-kbo "KT 위즈"

      구단       경기장명                                주소                       완공연도 건축면적 좌석수
4  KT 위즈  수원케이티위즈파크  경기도 수원시 장안구 경수대로 893, 종합운동장(야구장)  1988  13,356  18,700

$ info-kbo KT위즈

잘못된 구단 이름입니다. 유효한 구단 이름은 삼성 라이온즈, 한화 이글스, LG 트윈스, 두산 베어스, KT 위즈, 롯데 자이언츠, 키움 히어로즈, KIA 타이거즈, SSG 랜더스, NC 다이노스  입니다.
```


### Provided Content
* 경기장별 기본 정보 / 현재 검색 가능 정보 : 경기장명, 주소, 완공연도, 건축면적, 좌석수

-> 정보 별 검색 or 구단 별 검색 가능

* Not now

-> 경기장별 교통 정보
  
-> 경기장별 음식 및 편의 시설 정보

-> 경기장별 좌석 정보

-> 경기장별 별점 후기

-> 사용자 방문 기록 및 선호도를 기반으로 한 다음 경기 추천

### Web
* streamlit 구연 중
* https://kbostadium-jiwon1118.streamlit.app/

### DEV
```bash
$ git clone ...
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pytest
```
* http://data.prosports.or.kr/page/statistic/stadium 
