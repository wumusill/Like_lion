# css 기본 문법

## 1. css 선택자
* css 선언 방식 : 내장 방식, 링크 방식, 인라인 방식, @import 방식 
* 선택자는 스타일 적용 범위
* 선택자 종류
   1. 기본 선택자 
   2. 복합 선택자 
   3. 가상 클래스, 가상 요소, 속성

<br>

* css 스타일 상속
  * 부모(조상) 요소에 속성을 걸어주면 자식(후손) 요소에게 적용 됨 
  * 모두 상속 되는 것은 아니다.

<br>


* 선택자 우선순위
  * 점수가 높은 선언이 우선, 점수가 같으면 가장 마지막에 해석된 선언이 우선
  * 요소를 구체적으로 지목할수록 점수가 높다.



```css
선택자{
    속성 : 값;
    속성 : 값;
} 
```

<br>

### (1) 기본 선택자
* `*{}` : 전체 선택자
* `tag{}` : 태그 선택자
* `.class{}` : 클래스 선택자
* `#id{}` : id 선택자

```html
<span class = 'orange'>오렌지</span>
<span id = 'orange'>오렌지</span>
```

```css
*{
    width:100px;
}

span{
    width:100px;
}

.orange{
    width:100px;
}

#orange{
    width:100px;
}
```

<br>

### (2) 복합 선택자
#### a. 일치 선택자
* `span.orange{}`
* 각각의 선택자를 붙여씀
* 태그 선택자는 맨 앞에 쓴다.

#### b. 자식 선택자
* `ul > .orange{}`

#### c. 하위(후손) 선택자
* `div .orange{}`
* '띄어쓰기'가 선택자의 기호
* 자식 선택자보다 많이 쓰임 


<br>


### (3) 가상 선택자

* `a:hover{}` : 마우스 커서가 올라가 있을 때 선택 됨
```css
div{
  width:100px;
  height:100px;
  background-color:orange;
  transition:1s;
}

div:hover{
  width:300px;
  height:300px;
}
```


<br><br>

## 2. css 속성 

### (1) width, height
* 요소의 가로/세로 너비
* auto : 브라우저가 너비를 계산
* 단위 : px, vw, em etc 

<br>

### (2) margin
* 요소의 외부 여백(공간)을 지정하는 단축 속성
* 0: 외부 여백 없음
* auto : 브라우저가 여백을 계산 (가운데 정렬)  
* 단위 : px, vw, em, etc
* margin 속성
    * `margin: 10px;` : 4방위 여백
    * `margin: 10px 20px;` : 상하 좌우
    * `margin: 상 좌우 하;`
    * `margin: 상 우 하 좌;` : 시계방향
 
 * `margin-(top, bottom, left, right):`로 방향 지정 가능

```html
 <div class = "con">
  <div class = 'item'></div>
  <div class = 'item'></div>
  <div class = 'item'></div>
</div>
```
```css
.item{
  width:100px;
  height:100px;
  background-color:orange;
  margin-bottom:20px;   /* 아래쪽 여백 */
  margin:10px 20px 30px;    /* 상 좌우 하 여백 */
}
```

<br>

### (3) padding
* 요소의 내부 여백(공간)을 지정하는 단축 속성 
* 0 : 내부 여백 없음
* 단위 : px, vw, em, etc
* 값의 개수에 따라 여백의 방향, 속성에 방향 지정 방법 `margin`과 동일
 
<br>

### (4) border
* 요소의 테두리 선을 지정하는 단축 속성
* `border:선-두께 선-종류 선-색상;`
* `border-방향:`
* `border-radius:` 모서리를 둥글게 깎음 
```css
.item{
  width:100px;
  height:100px;
  background-color:orange;
  margin-bottom:10px;
  border:2px solid green;
  border-radius:5px;
}
```

<br>


### (5) box-sizing
* 요소의 크기 계산 기준을 지정
* `content-box` : 요소의 내용으로 크기 계산 `(default)`
* `border-box` : 요소의 내용 + padding + border로 크기 계산

```html
<div class="item first"></div>
<div class="item"></div>
```
```css
.item{
  width:100px;
  height:100px;
  background-color:orange;
  margin:10px;
}

.item.first{
  border:10px solid red;
  padding:20px;
  box-sizing:border-box;
}
```

<br>


### (6) overflow
* 요소의 크기 이상으로 내용이 넘쳤을 때, 보여짐을 제어하는 단축 속성
* `overflow:visible;` : 넘친 내용을 그대로 보여줌 `(default)`
  
```html
<div class="parent">
  <div class="child"></div>
</div>
```

```css
.parent{
  width:200px;
  height:150px;
  background-color:royalblue;
  margin:20px;
  overflow:hidden;
}
.child{
  width:300px;
  height:100px;
  background-color:orange;
}
```

<br>

### (7) display
* 요소의 화면 출력(보여짐) 특성 
```html
<span>hello world!</span>
```

```css
body{
  margin:20px;
}
span{
  width:120px;
  height:30px;
  background-color:royalblue;
  color:white;
  display:block;
}
```

<br>

### (8) opacity
* 요소의 투명도 결정
* 1 `(default)` : 불투명
* 0 ~ 1 소수로 설정

```html
<span>hello world!</span>
```
```css
body{
  margin:20px;
}
span{
  width:120px;
  height:30px;
  background-color:royalblue;
  color:white;
  opacity:0.5;
}
```

<br>


### (9) background

```html
<div></div>
```
```css
div{
  width:200px;
  height:200px;
  background-color:orange;
  background-image:url("이미지 경로");
  background-size:200px;    /* 이미지 사이즈 조절 */
  background-repeat:no-repeat;  /* 바둑판 배열 끄기 */
  background-position:center;   /* 이미지 가운데 정렬 */
}
```

<br>

### (9) transition, 전환
* transition: 속성명 **지속시간** 타이밍함수 대기시간;

```html
<div></div>
```
```css
div{
  width:100px;
  height:100px;
  background-color:orange;
  transition:2s;
}
div:hover{
  width:300px;
  height:300px;
  background-color:royalblue;
}
```

<br>


### (10) transform, 변환

* transition 과 함께 사용된다.

```html
<div class="con">
  <div class="item">AB</div>
</div>
```
```css
body{
  padding:100px;
}

.con{
  width:100px;
  height:100px;
  background-color:royalblue;
}
.item{
  width:100px;
  height:100px;
  background-color:orange;
  transform:rotate(45deg) scale(1.3);
}
```

```css
.item{
  width:100px;
  height:100px;
  background-color:orange;
  transition:1.5s;
}
.item:hover{
 transform:rotate(45deg) scale(1.3);
 }
```