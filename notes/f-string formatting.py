"""
이 문서는 사실 아래 링크 내용을 내가 해석하고 정리한것이다. 내가 이해하기 쉬울려고...
https://docs.python.org/3/reference/lexical_analysis.html#f-strings
아래는 파이썬 문법에 해석에 유용했던 정보들이다.
https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form
https://en.wikipedia.org/wiki/Parsing_expression_grammar

formatted string literal, 혹은 f-string이라고 불리는 이번 문서에서 배울 내용은, 사실 그냥 string이라는 변수를 만드는 하나의 도구다.
string literal이라는 용어 자체가 string이라는 variable을 생성하는 여러 방식들을 일컫는 말이다.
예를 들어, 우리가 (파이썬에서) 흔히 사용하는 string 형성 방식인
x = 'foo'
도 string literal 중 하나이다.

즉 f-string은 이렇게 string을 만드는 방식 중에 하나로, 파이썬에서 제공되는 도구 중 하나다. 
3.6 ver 부터 지원되며, 3.6ver 이상에서는 이 방식을 권고한다.

'f' 혹은 'F'를 앞에 붙임으로써 사용하기 대문에 f-string이라고 불린다(...)
이 f-string 의 가장 큰 특징은 replacement field가 있다는 것이다.
replacement field란, 중괄호({})로 구별된 공간 안의 특정 표현식(expression)을 말한다.
이 replacement field를 run-time 때 계산을 함으로써 string을 표현하는 literal로, 이 때문에 다른 string literal과는 차별된 특징을 가진다.
왜냐면 일반적으로 string literal은 expression을 계산하는 형식이 아닌 그저 상수 값이기 때문.

일단 시작 방식은 f'...'이며, {}안에 있지 않은 모든 character들은 그냥 literally, 즉 그대로 입력을 해버린다.
이 부분을 파이썬 문법에서는 literal_char로 정의했다.
말그대로 {}안에 있지 않은 모든 character은 literally로 표현한다.
예를 들어 구 string formatting 방식 중 하나인 %를 이용한 방식에서는 %를 %%로 표현해야 했으나, 여기서는 그럴 필요 없이 그냥 % 하나만 f'...' 안에 넣으면 %로 나온다.
구체적 예시로는
"""
a = 35
print(f'{a}%')
"""
의 경우 출력은 "35%"로 나오게 된다.
단 '{{' 나 '}}'의 경우 '{' 랑 '}'로 표시된다. 얘네가 유일한 예외다.

문서의 문법에서 보면 f-string이
f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
로 정의되어 있는것을 볼 수 있는데
여기서 '|' 는 Extended Backus form 에서 '또는'을 나타낸다고 생각하면 편하다.
즉 위 f-string은 literal char이나 '{{' 나 '}}' 나 replacement field로 이루어져있다는 것이다.

replacement_field는 다음과 같이 정의된다.
replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
일단 '{'로 replacement field가 시작된다.
이후 f_expression이 들어가며, '='가 선택적으로 들어가고([]이 '선택적으로'를 뜻한다. '또는'과는 다른 느낌이니 참고)
역시나 선택적으로 '!', conversion이 들어가고 ':', format_spec이 들어가며
이후에 '}'로 마무리가 된다. 여기서 '!'이 있으면 conversion이 꼭 필요하고, ':'이 있으면 format_spec이 꼭 필요하다.

즉 replacmenet field는 {} 안에 f_expression이 필수로 들어가면서, 선택적으로 '=', conversion, format_spec으로 구성되는 녀석이다.

'='의 역할은 바로 해당 replacment_field 에서 참조한 변수가 뭔지를 나타내는데 사용될 수 있다.
그 방식은 다음과 같다.

"""
a = 35
print(f'{a=}')
"""
의 경우 출력은 "a=35"로 나오게 된다.
이렇게 어떤 변수가 이용되었는지 알려주거나, 그냥 변수 표현하려고 이걸 사용하면 된다. 이것은 ver 3.8.부터 된다.

'!'를 사용하면 conversion을 사용할 수 있게 된다. 이는 뭐냐면
conversion        ::=  "s" | "r" | "a"
으로 구성되어 있다. 즉 s, r, a의 형태로 변환을 시킬 수 있다는 것이다.
s는 str()이라는 method를 사용해서 변수를 string으로 변환시키는 것이다.
r은 repr()이라는 method를 사용해서 변수를 string으로 변환시키는 것이다. 예를 들어

"""
print(f"He said his name is {name!r}.")
print(f"He said his name is {repr(name)}.")
"""
위 두 줄의 코드는 똑같은 문장을 인쇄하는데, 이것은 바로
"He said his name is 'Fred'."
의 형식으로 출력이 나온다.

여기서 알 수 있는 것이 하나 있는데, {} 안에다가 expression을 집어넣을 경우 그걸 그대로 실행할 수 있다는 것이다.
다만 일반적인 expression 실행 방식과 차이점이 몇가지가 있다.
1. 빈 expression은 허용이 안된다.
즉 중괄호 안이 텅텅 비어 있으면 안된다. 무언가가 있어야한다.
literal_char에서도 정의가 나오는데, Null값은 예외로 둔다. 즉 빈 값은 받지 않는다는 것이다.
2. lambda, := 의 경우에는 그 자체가 또 괄호로 감싸져있어야하며, 괄호 없이 사용될 수가 없다.
예를들어 lambda를 굳이 쓸거면
"""
f'{(lambda x: x*2)(3)}'
"""
의 형식으로 써야하지
"""
f'{lambda x: x*2}'
"""
로 쓰면 안된다는 것이다.
근데 애초에 저렇게 왜 쓸까

좀 삼천포로 갔는데, 다시 돌아오자면, a의 경우에는 ascii()를 적용한 거랑 같은 결과가 나온다.
참고로 str()은 말그대로 string object를 return하는 함수고
repr()의 경우에는 str()과 일반적으로 비슷하나, 특정 종류의 변수에 대해서는 변수 type, 변수의 address 등 추가 정보를 denote 하는 경우가 있다.
ascii()의 경우에는 repr()이랑 거의 동일한데, non-ascii 변수의 경우에는 escape를 시도한다.

format_spec의 경우에는 예전의 string formatting처럼 string의 표현 방식을 구체적으로 지정할 수 있게 도와준다.
https://docs.python.org/3/library/string.html#formatspec
위 링크를 참고하면 format_spec에 사용되는 변수들을 알 수 있다.
이건 그냥 읽으면 되기도 하고, 너무 길기도 하고, 집에 가면 문서로도 따로 있으니까 여기서는 생략하고 나중에 문서로 만들든가 하겠다.

이정도면 다 해결되었으며 몇가지 특이한 예시만 좀 들겠다.
"""
line = "The mill's closed"
f"{line = }"
f"{line = :20}"
f"{line = !r:20}"
"""
이것들의 결과는 다음과 같다.

'line = "The mill's closed"'
'line = "The mill's closed   "'
'line = "The mill's closed"' 

보면 첫줄, 둘째줄의 차이는 공백의 차이며
사실 첫째와 세번째의 경우 '='을 사용하면 차이가 실질적으로 거의 없다는 것을 나타낸다고 볼 수 있다.
다만 r의 특이 case에 해당되는 변수라면... 차이가 생길 수도 있지요.
