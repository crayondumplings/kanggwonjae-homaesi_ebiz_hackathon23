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
