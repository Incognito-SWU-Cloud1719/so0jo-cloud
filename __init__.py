#폴더 안에 있는 __init__.py는 소스코드가 여러개 일 경우 하나로 묶는 역할

# https://mmjourney.tistory.com/14


#import inspect
#import os
#import sys

    from ConfigHelper import ConfigHelper as Config
except ImportError as e:
    print(e," 추가할 수 없습니다.")
    exit(1)
