import re

def count_spanish_characters(input_string):
    # 확장 문자를 원래의 스페인어 알파벳으로 변환
    input_string = re.sub(r'a,|e,|i,|o,|u,|n~|u\.\.', lambda m: {'a,':'á', 'e,':'é', 'i,':'í', 'o,':'ó', 'u,':'ú', 'n~':'ñ', 'u..':'ü'}[m.group()], input_string)
    
    # 스페이스를 제외한 문자의 개수를 세기
    count = len(input_string.replace(" ", ""))
    
    return count

# 예시
print(count_spanish_characters("espan~afu,tbol"))  # 출력: 12
print(count_spanish_characters("si,aqui,esta"))  # 출력: 9

# re.sub 함수는 문자열에서 패턴을 찾아 다른 문자열로 대체하는 역할을 한다.
# 첫 번째 인자인 r'a,|e,|i,|o,|u,|n~|u\.\.'는 찾을 패턴을 나타낸다. 여기서는 확장 문자를 나타내는 문자열들을 찾는다.
# 두 번째 인자인 lambda m: {'a,':'á', 'e,':'é', 'i,':'í', 'o,':'ó', 'u,':'ú', 'n~':'ñ', 'u..':'ü'}[m.group()]는 찾은 패턴을 어떻게 대체할지를 정의한다. 여기서는 찾은 확장 문자를 해당하는 스페인어 알파벳으로 대체한다.
# 세 번째 인자인 input_string는 대체 작업을 수행할 원본 문자열이다.
# 이렇게 하면 input_string에서 확장 문자를 찾아 해당하는 스페인어 알파벳으로 대체한 후, 그 결과를 다시 input_string에 저장한다. 이 과정을 통해 원래의 스페인어 문장을 복원한다.
