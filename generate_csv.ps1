$data = @()

# Calibre
$calibre = @(
    "Quick Start Guide", "The Chrysanthemum and the Sword: Patterns of Japanese Culture", "The Time Machine", 
    "The Great Gatsby", "The Brothers Karamazov", "all quiet on the western front", 
    "Oedipus King of Thebes / Translated into English Rhyming Verse with Explanatory Notes", 
    "Notre-Dame de Paris", "An Inquiry into the Nature and Causes of the Wealth of Nations", 
    "Crime and Punishment", "War and Peace", "The Sorrows of Young Werther", 
    "Andersen's Fairy Tales", "Anna Karenina", "Pride and Prejudice", 
    "Jane Eyre: An Autobiography", "무기체계 발달", "The Mysterious Affair at Styles", 
    "Wuthering Heights", "Oliver Twist", "Heart of Darkness", "Sense and Sensibility", 
    "Don Quixote", "Treasure Island", "Les Miserables", 
    "The Strange Case of Dr. Jekyll and Mr. Hyde", "The Count of Monte Cristo, Illustrated", 
    "A Tale of Two Cities", "The War of the Worlds", "Around the World in Eighty Days", 
    "Twenty Thousand Leagues under the Sea", "A Journey to the Centre of the Earth", 
    "The Mysterious Island", "전쟁과 경제"
)
foreach ($t in $calibre) { $data += New-Object PSObject -Property @{ App = "Calibre"; Title = $t } }

# YES24
$yes24 = @(
    "역사를 바꾼 신무기", "상도", "상도 1  : 천하제일상", "전장을 지배한 무기전 전세를 뒤바꾼 보급전", 
    "살림지식총서", "서양 무기의 역사 - 살림지식총서 249", "경제학 혁명", "회의주의자를 위한 경제학", 
    "Around the World in Eighty Days. Junior Deluxe Edition", 
    "Five Weeks in a Balloon / Or, Journeys and Discoveries in Africa by Three Englishmen", 
    "A Journey into the Interior of the Earth", "The Mysterious Island", 
    "Twenty Thousand Leagues under the Sea", "대한민국 금융 잔혹사", 
    "경관의 피 : 블랙 앤 화이트 시리즈 060", "탈세의 세계사 : 세금은 세계의 역사를 어떻게 바꾸었는가", 
    "돈의 물리학 : 돈이 움직이는 방향과 속도를 예측하다", "공작:이중스파이 흑금성의 시크릿파일", 
    "공작 1 : 이중스파이 흑금성의 시크릿파일", "공작 2 : 무간도에 갇힌 이중스파이", 
    "안티프래질 Antifragile", "가루전쟁", "돈의 역사", "50대 사건으로 보는 돈의 역사", 
    "밤은 노래한다 (개정판)", "필립 K. 딕 걸작선", 
    "안드로이드는 전기양의 꿈을 꾸는가? - 필립 K. 딕 걸작선 12", "절대적이며 상대적인 리더십의 물리학", 
    "기업과 경영: 욕망의 역사", "수학, 인문으로 수를 읽다", 
    "슈뢰딩거의 파동방정식 인문학적으로 접근하기(개정판)", "인간실격", "인간실격 1권", 
    "[고화질] 블랙 잭", "블랙 잭(BLACK JACK) 01권", "흑치상지 (현진건 장편소설)", 
    "고구려가 왜 북경에 있을까", "탄금", "삶의 정도", "완전론", 
    "전쟁의 판도를 바꾼 전염병 - 살림지식총서 276", "파동의 법칙 : 푸리에에서 양자까지"
)
foreach ($t in $yes24) { $data += New-Object PSObject -Property @{ App = "YES24"; Title = $t } }

# Aladin
$aladin = @(
    "케이든 선", "별세계 사건부 : 조선총독부 토막살인", "스타십 트루퍼스 - 환상문학전집 27", 
    "[고화질] 전원 옥쇄하라! 01", "[고화질] 전원 옥쇄하라! 02", "[고화질] 클레이모어 04", 
    "[고화질] 클레이모어 02", "[고화질] 클레이모어 01", "[고화질] 요르문간드 01", "그림자 1", 
    "[고화질] 클레이모어 06", "[고화질] 클레이모어 05", "[고화질] 클레이모어 09", 
    "[고화질] 클레이모어 12", "[고화질] 클레이모어 11", "[고화질] 클레이모어 10", 
    "[고화질] 클레이모어 07", "[고화질] 클레이모어 08", "[고화질] 클레이모어 03", 
    "[고화질] 클레이모어 14", "[고화질] 클레이모어 13"
)
foreach ($t in $aladin) { $data += New-Object PSObject -Property @{ App = "Aladin"; Title = $t } }

# Bookcube
$bookcube = @("동태적 거시경제학 -성장과 변동-")
foreach ($t in $bookcube) { $data += New-Object PSObject -Property @{ App = "Bookcube"; Title = $t } }

$data | Select-Object App, Title | Export-Csv -Path "c:\Users\kkmin\Desktop\ebook\ebook_list.csv" -NoTypeInformation -Encoding UTF8
