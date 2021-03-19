# Section01
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# 가상환경(독립된 공간) => 하나의 컴퓨터에서 다양한 프로젝트를 진행할 때, 자신이 원하는 디양한 python 환경을 사용하기 위해 여러가지 가상환경을 이용하여 사용
# python3 -m venv [가상환경명]

# 외부 설치 패키지
# pip install [패키지명]4

# 외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '4': 100, '2': 88}

# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4*' '))
