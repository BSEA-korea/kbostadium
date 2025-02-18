import pandas as pd
import typer

data = {
    "구단": ["삼성 라이온즈", "한화 이글스", "LG 트윈스", "두산 베어스", "KT 위즈", "롯데 자이언츠", "키움 히어로즈", "KIA 타이거즈", "SSG 랜더스", "NC 다이노스"],
    "경기장명": ["대구 삼성 라이온즈파크", "대전 한화생명 이글스파크", "서울 잠실 야구장", "서울 잠실 야구장" , "수원케이티위즈파크", "부산 사직야구장", "서울고척스카이돔", "광주-기아 챔피언스", "인천SSG 랜더스필드", "창원NC파크"],
    "주소": ["대구광역시 수성구 야구전설로 1, 대구삼성라이온즈파크", "대전광역시 중구 대종로 373", "서울특별시 송파구 올림픽로 25, 서울종합운동장(야구장)", "서울특별시 송파>구 올림픽로 25, 서울종합운동장(야구장)", "경기도 수원시 장안구 경수대로 893, 종합운동장(야구장)", "부산광역시 동래구 사직로 45, 사직야구장", "서울특별시 구로구 경인로 430, >고척스카이돔", "광주광역시 북구 서림로 10, 무등종합경기장", "인천광역시 미추홀구 매소홀로 618, 문학경기장(야구장)","경상남도 창원시 마산회원구 삼호로 63, 창원NC파크"],
    "완공연도": ["2016", "1964", "1982", "1982", "1988", "1985", "2015", "2014", "2002", "2019"],
    "건축면적": ["22,666", "5,761", "20,741", "20,741", "13,356", "9,867", "29,120", "16,065", "22,932", "12,567"],
    "좌석수": ["24,000", "20,007", "23,750", "23,750", "18,700", "22,758", "16,670", "20,500", "23,000", "17,891"],
}


def info_kbo(keyword: str) -> pd.DataFrame:
    # 데이터프레임 생성
    df = pd.DataFrame(data)
    
    # 유효한 구단 이름인지 확인
    if keyword in df["구단"].values:
        # 해당 구단의 데이터 가져오기
        fdf = df[df["구단"] == keyword]
        return fdf
    else:
        return f"잘못된 구단 이름입니다. 유효한 구단 이름은 {', '.join(df['구단'])} 입니다."

# 출력 함수
def print_info_kbo(keyword: str):
    rdf = info_kbo(keyword)
    print(rdf)

# Typer 실행 함수
def entry_point2():
    typer.run(print_info_kbo)
