USER = ""
PASS = ""

session = requests.session()

#ログイン
#デベロッパーツールで
login_info ={
    "username: "",
    "password: "",
}

url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res= session.post(url_login,data=login_info)
#エラーなら例外を発生させる
res.raise_for_status()

soup=BeautifulSoup(res.text,"html.parser")
a = soup.select_one(".islogin a")
print(a)
if a is None:
  print("マイページが取得できませんでした")
  quit()

#相対URLを絶対URLに変換
url_mypage = urljoin(url_login,a.attrs["href"])
print("マイページ",url_mypage)

#マイページにアクセス
res = session.get(url_mypage)
res.raise_for_status()

#お気に入りの詞のタイトルを列挙
soup= BeautifulSoup(res.text,"html.parser")
links = soup.select("#favlist li > a")
for a in links:
  href = a.attrs["href"]
  title = a.get_text()
  print("-",title,">",href)
