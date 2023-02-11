### Reverved words or keyword of the language

키워드는 파이썬에서 사용목적이 이미 정해져 있는 단어로 예약어라고 부릅니다. 그래서 다른 용도로 사용이 불가능합니다.   
키워드는 다음과 같습니다.  
<code>
import keyword

reverved_word =keyword.kwlist #kwlist
for i in range(0, len(reverved_word)):
    print("[{:^10}]".format(reverved_word[i]), end="")
    if( (i+1)%5 ==0):
        print("\n")
       
</code>

[False     ] [None      ] [True      ] [and       ] [as        ] 
[assert    ] [break     ] [class     ] [continue  ] [def       ] 
[del       ] [elif      ] [else      ] [except    ] [finally   ] 
[for       ] [from      ] [global    ] [if        ] [import    ] 
[in        ] [is        ] [lambda    ] [nonlocal  ] [not       ] 
[or        ] [pass      ] [raise     ] [return    ] [try       ] 
[while     ] [with      ] [yield     ] 

