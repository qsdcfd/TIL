#!/usr/bin/env python
# coding: utf-8

# git: 기록해두고 관리할 수 있는 버전 관리 시스템
# github: 시공간의 제약없이 협업할 수 있는 온라인 시스템.
# github commit 하기 & branch 이름바꾸기 입니다.
# 다 lms에 있는 내용인데, 요점정리랑, branch 이름 바꾸는 내용 첨가했어요
# 제가 branch 다른이름으로 올리는게 궁금해서 지금까지 찾아봐서... 다른 공부를 못했으니 공유라도 하려구요..!
# 
# 
# 순서
# - github 가입
# 
# - 폴더 생성
# 1. bash에서 git을 할 폴더 생성 / 선택 ( mkdir 폴더이름)
# 2. cd 폴더이름
# 
# - git 준비단계 : 3,4,5번은 폴더 외부에서 해도 무관)
# 3. git config --global user.email "이메일\@주소"
# 4. git config --global user.name "username"
# 5. git config -l(L소문자) : 3, 4번 잘 되었는지 확인, 실수 있으면 수정 가능
# 
# - 기록 시작
# 6. git init (: git 시작, ls -a 로 확인하면 .git 생김)
# 7. git status 로 상태 확인해보며 진행 가능, 현재는 commit 할게 없다고 뜰것. 
#    On branch master 혹은 On branch main이라고 뜰건데,(다른이름도 뜨게 설정가능) 아직 조정안됨.
# 8. echo "HelloHello :)" >\> README.md 등 뭐든지 만듬. vim으로 만들어도 되고 뭐든지됩니다.
# 9. git status 쳐보면 commit 할지 선택되지 않은 파일이 있다고 알려줌.
# 10. git add "filename" 해서 하나씩 골라서 원하는 것만 commit가능 : git add . 을 치면 현재 변동사항 전부 commit하고 싶다는 표현.
# 11. git commit -m "하고 싶은 아무말(commit에대한 설명)"
# 
# - github연동
# 가입 username, repository 생성완료
# 12. token생성 
# 참조 : [https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
# 13. 혹시 git status 치시면, On branch master로 뜨시는 분 있으실텐데, 
#      이대로 진행하시면 github에는 branch 기본값이 main으로 되어있기 때문에,
#      master라는 branch가 하나 더 생기고 거기에 기록됩니다. 
#      상관없으시면 그대로 진행하셔도 되지만, 싫으시다면,
#      git branch -M main 으로 branch이름을 변경 가능합니다. 
#      git status로 잘 되었나 확인가능
# 14. git remote add origin repository주소
#      ex) git remote add origin https://github.com/\~\~\~\~/\~\~.git
# 15. 바로 올리셔도 되지만 git config credential.helper. store 를 먼저 치고 하시면, 
#      할때마다 token을 입력 안하셔도 됩니다.
# 16. git push origin main(아니면 다른 branch이름/ 본인의 branch이름으로 쳐야 작동)
#      후에 나오는 username 치고 password에 token 번호 치면 됩니다. 저는 복붙이 안되서 하나하나...
# 
