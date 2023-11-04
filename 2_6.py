# 파이썬의 re 모듈을 불러온다. 이 모듈은 정규 표현식을 사용하여 문자열을 처리하는 데 사용된다.
import re

# count_spanish_characters라는 함수를 정의한다. 이 함수는 입력 문자열을 받아서 스페인어 알파벳으로 변환하고, 변환된 문자열의 길이를 반환한다.
def count_spanish_characters(input_string):
    # re.sub 함수를 사용하여 입력 문자열에서 확장 문자를 찾아 원래의 스페인어 알파벳으로 변환한다.
    # 'a,'는 'á', 'e,'는 'é', 'i,'는 'í', 'o,'는 'ó', 'u,'는 'ú', 'n~'는 'ñ', 'u..'는 'ü'로 변환된다.
    input_string = re.sub(r'a,|e,|i,|o,|u,|n~|u\.\.', lambda m: {'a,':'á', 'e,':'é', 'i,':'í', 'o,':'ó', 'u,':'ú', 'n~':'ñ', 'u..':'ü'}[m.group()], input_string)
    
    # replace 함수를 사용하여 문자열에서 공백을 제거하고, len 함수를 사용하여 문자열의 길이를 구한다.
    # 이렇게 하면 스페이스를 제외한 문자의 개수를 얻을 수 있다.
    count = len(input_string.replace(" ", ""))
    
    # 변환된 문자열과 그 길이를 반환한다.
    return input_string, count

# 예시
# "espan~afu,tbol" 문자열을 변환하고, 변환된 문자열의 길이를 출력한다.
converted_string, count = count_spanish_characters("espan~afu,tbol")
print(f"변환된 문자열: {converted_string}, 문자 개수: {count}")
