import pandas as pd

# pd.read_html 은 HTML에서 <table></table> 태그를 찾아 자동으로 dataframe 형식으로 만들어 준다.
code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]

# 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

# 우리가 필요한 것ㄷ은 회사명과 종목코드이기 때문에 필요없는 column 제외
code_df = code_df[['회사명','종목코드']]

# 한글로된 컬럼명을 영어로 바꿔준다.

code_df = code_df.rename(columns ={'회사명':'name','종목코드':'code'})
print(code_df.head())

