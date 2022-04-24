# html 기본
## 1. html 틀
```html
<!DOCTYPE html>     
<!--문서의 html 버전을 지정-->

<html lang="en">    
<!--문서의 전체 범위-->

<head>      
<!--문서의 정보를 나타내는 범위-->
<!--웹페이지의 제목, 설명, 사용할 파일 위치, 스타일 같은 보이지 않는 정보를 작성하는 범위-->
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>     
    <!--브라우저 탭에 표시되는 html 문서의 제목 정의-->
    
    <link rel="stylesheet" href="./css/main.css">   
    <!--main.css와 연결해주는 코드, rel : 가져올 문서와 관계(필수 속성)-->
    
    <script src="./js/main.js"></script>    
    <!--자바스크립트 연결 --> 

</head>
<body>      
<!--문서의 구조를 나타내는 범위-->
<!--사용자 화면을 통해 보여지는 로고, 헤더, 메뉴, 버튼 등 웹페이지의 보여지는 구조를 작성하는 범위-->
    
</body>
</html>
```

<br/><br/>

## 2. 글자와 상자
* 요소가 화면에 출력되는 특성, 크게 2가지로 구분


* 인라인(Inline) 요소 
  * 글자를 만들기 위한 요소들
  * 가로 세로 너비를 지정할 수 없음
  * 요소의 크기따라 결정 됨
  * 하위(자식) 요소로 블록 요소를 가질 수 없음

* 블록(Block) 요소 
  * 상자(레이아웃)를 만들기 위한 요소들
  * 가로 세로 너비를 지정할 수 있음
  * 자식(하위) 요소로 인라인, 블록 요소 둘 다 가질 수 있음


<br><br/>

## 3. html 태그
* `<태그 속성 = "값">내용</태그>`


### (1) div 태그
* 블록 요소
* 특별한 의미가 없는 구분을 위한 요소



### (2) h1 태그
* 블록 요소
* 제목을 의미하는 요소

### (3) p 태그
* 블록 요소
* 문장을 의미하는 요소

### (4) img 태그
* 인라인 요소
* `src = "삽입할 이미지 경로"`
* `alt = "삽입할 이미지의 이름"` 

```html
<body>
    <div>
        <h1>오늘의 날씨</h1>
        <p>중부 집중호우, 남부는 열대야, 12호 태풍 북상 중..</p>
        <img src = "img/weather.jpg" alt = "12호 태풍"/>
    </div>
</body>
```

<br/>

### (5) ul, ol, li 태그
* 블록 요소
* `ul`
  * 순서가 필요없는 목록의 집합을 의미
* `ol`
  * 순서가 필요한 목록의 집합을 의미
* `li`
  * 목록 내 각 항목

```html
<body>
  <ul>
    <li>사과</li>
    <li>딸기</li>
    <li>수박</li>
  </ul>  
</body>
```

<br/>

### (6) a 태그
* 인라인 요소
* 다른/같은 페이지로 이동하는 하이퍼링크를 지정하는 요소
* `target = "_blank"` : 새 탭에 열지 결정하는 속성, 기본값은 현재 탭
```html
<a href="https://www.naver.com/" target = "_blank">naver</a>
```

<br/>


### (7) span 태그
* 인라인 요소
* 특별한 의미가 없는 구분을 위한 요소

```html
<body>
  <p>
    <span>동해물과</span>백두산이 마르고 닳도록
  </p>
</body>
```

<br/>


### (8) br 태그
* 인라인 요소
* 줄바꿈 요소

### (9) input 태그
* 인라인-블록 요소
* 사용자가 데이터를 입력하는 요소
* `type="입력받을 데이터의 타입"`
* `placeholder = "어떤 인풋값이 와야하는지 힌트 제공"`

```html
<input type="text" placeholder = "이름을 입력해주세요!">
```

<br/>


### (10) label 태그
* 인라인 요소
* 라벨 가능 요소(input)의 제목
* `<input type="checkbox" or "radio">` 태그를 자식으로 두는 경우가 많음
* label을 부모로 두면 텍스트 클릭만으로 체크박스 활성화

```html
<label>
  <input type="checkbox"> Apple
</label>
<label>
  <input type="checkbox"> Banana
</label>
```
* `type="radio"` : 사용자에게 체크 여부를 그룹에서 1개만 입력 받음
* `name="그룹 이름"`
```html
<label>
  <input type="radio" name="fruits"> Apple
</label>
<label>
  <input type="radio" name="fruits"> Banana
</label>
```

<br/><br/>


## 4. 태그의 class와 id
* `<태그 class="이름"></태그>`
  * 요소를 지칭하는 중복 가능한 이름
  * css에서 .이름{}으로 코드 지정
* `<태그 id="이름"></태그>`
  * 요소를 지칭하는 고유한 이름
  * css에서 #이름{}으로 코드 지정